import markdown2
import re

with open("test_readme.md", "r") as f:
    lines = f.read()

article_pattern = re.compile(r"(?<=---)(?P<article>.*?)(?=---)",
                             re.DOTALL)  # Look ahead and look behind assertions are needed so that "---" before and after an article doesn't get consumd else regex matched will be skipping every other article.
title_pattern = re.compile(r"### " + chr(9654) + " (?P<title>.*?)\n")  # chr(9654) is '▶'
# code_to_setup_example_pattern = re.compile()
explanation_pattern = re.compile(r"Explanation:?\n(?P<explanation>.*)", re.DOTALL)
articles = article_pattern.findall(lines)


if articles:
    for article in articles:
        try:
            # print("ARTICLE :::\n", article)
            print("TITLE :::\n", title_pattern.search(article).group("title").strip())
            print("EXP :::\n", explanation_pattern.search(article).group("explanation").strip())
            print("\n\n\n\n")
        except:
            continue
