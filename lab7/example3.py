books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for book in books:
  book_dict[book] = (len(book),len(set(book)))


for k in book_dict:
  avg = (book_dict[k][0] + book_dict[k][1]) / 2
  book_dict[k] =  (book_dict[k][0],book_dict[k][1],avg)

for k in book_dict:
  print(k,'->',book_dict[k])
