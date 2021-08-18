random_list = ['a', 0, 2]
for entry in random_list:
    try:
        print("The entry is ", entry)
        r = 1/int(entry)
    except:
        print("Oops! Exception raised")
        continue

    print("The reciprocal of", entry, "is", r)
