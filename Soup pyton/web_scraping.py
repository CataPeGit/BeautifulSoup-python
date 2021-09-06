from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type = "text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))


"""
tags = doc.find_all(text = re.compile("\$.*")) #,limit = 1) pt a limita
for tag in tags:
    print(tag.strip())

print()
print(tags)





url = " url goes here :) "

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text = "$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)



tags = doc.find_all("p")[0]

print(tags.find_all("b"))
"""
