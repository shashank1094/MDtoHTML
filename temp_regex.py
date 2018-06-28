import re
code_text="""---

# 👀 Examples

## Section: Strain your brain!

### ▶ Strings can be tricky sometimes *

1\.
```py
>>> a = "some_string"
>>> id(a)
140420665652016
>>> id("some" + "_" + "string") # Notice that both the ids are same.
140420665652016
```
---

2\.
```py
>>> a = "wtf"
>>> b = "wtf"
>>> a is b
True
---

abc
"""

for i in re.findall("(?<=---).*?(?=---)",code_text,re.DOTALL):
    print(i,end="----------------------------------")