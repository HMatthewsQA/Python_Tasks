def seven(string):
    count = 0
    string = string.lower()
    for x in string:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            count += 1
    return count