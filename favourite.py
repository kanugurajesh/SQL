# import csv

# i = 0
# # titles = set()
# title = {}

# with open("apple_stocks.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         row = row["Date"].strip()
#         if row not in title:
#             title.update(row)
#         else:
#             title[title] += 1

# # the below code line is used to sort the number
# for titles in sorted(title):
#     print(titles)

import csv

titles = {}

with open("top_movies.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row = row["movie"].strip()
        if row not in titles:
            dictq = {f"{row}":0}
            titles.update(dictq)
        titles[row] += 1

def f(title):
    return titles[title]

# the below one are the lambda functions you can use this instead of the traditional functions
for title in sorted(titles,key=lambda title:titles[title],reverse=True):
    print(title,titles[title])
