import markdown
import markdown2
import re

code_text = """* But why did the `is` operator evaluated to `False`? Let's see with this snippet.
  ```py
  class WTF(object):
    def __init__(self): print("I ")
    def __del__(self): print("D ")
  ```

  **Output:**"""

print("PROBLEM :: \n", markdown2.markdown(code_text))

pattern = re.compile(r"```py(?P<code>.*?)```", re.DOTALL)

code_only = pattern.search(code_text).group("code")

code_only = code_only.replace("\n", "\n\t")

print("SOLUTION :: \n", markdown2.markdown(code_only))

###################################################
# Replacing all code occurrences in the given string

code_only = pattern.sub(lambda m: (m.group("code")).replace("\n", "\n\t"), code_text)
print("ORIGINAL :: ", code_only)
print("SOLUTION :: \n", markdown.markdown(code_only))
