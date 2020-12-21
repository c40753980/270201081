books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for book in books:
  book_dict[book] = (len(book),len(set(book)))


for k,v in book_dict.items():
  print(k,'->',v)