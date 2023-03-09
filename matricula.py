import re

text = input()
pattern = r"\bE?[-]?\d{4}[-, ]?[A-Z]{3}"
results = re.findall(pattern, text)
for match in results:
    print(match)



