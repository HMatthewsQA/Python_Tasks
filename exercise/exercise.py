books = {"Harry Potter":"J.K. Rowling", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}

print(books["The Hobbit"])

mark = int(input('The mark you achieved: '))
#grade = int(mark)

if mark >= 85:
    print('Distinction')
elif mark >= 65:
    print('Pass')
else:
    print('Fail')

