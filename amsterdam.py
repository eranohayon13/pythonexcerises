def amsterdam(s):
    count = 0
    ls =s.lower()
    storagestring = ls.split(" ")
    for i in storagestring:
        if i == "am":
            count += 1
    return count