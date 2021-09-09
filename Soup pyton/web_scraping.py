from bs4 import BeautifulSoup
import requests 
import re

search_term = input("What product do you want to search for?") 

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_ = "list-tool-pagination-text")
pages = int(str(page_text).split("/")[-2].split(">")[-1][:1]) # we find the number of pages

items_found = {}

for page in range(1, pages + 1): # we loop trough all the pages
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    #we will filter the results ourselves so we make sure we get the right stuff
    items = div.find_all(text = re.compile(search_term))

    for item in items:
        parent = item.parent

        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = item.find_parent(class_ = "item-container")
        try:
            price = next_parent.find(class_ ="price-current").find("strong").string
            # we use this dictionary to store price and link
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            pass

# now we will sort the dictionary
# this means we have to convert it to a list first
# sort it and then convert back to dictionary

sorted_items = sorted(items_found.items(), key = lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0]) # the key/name
    print(f"${items[1]['price']}")
    print(items[1]['link'])
    print ("--------------------------")
    print()



"""
from bs4 import BeautifulSoup
import requests 

url = " HERE GOES THE URL "
results = requests.get(url).text
doc = BeautifulSoup(results, "html.parser")

tbody = doc.body
trs = tbody.contents

#print(trs[0].parent.name)

prices = {}

for tr in trs[:10]:
    name,price = tr.contents[1:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

print(prices)



from bs4 import BeautifulSoup
import re

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("input", type = "text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))



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
