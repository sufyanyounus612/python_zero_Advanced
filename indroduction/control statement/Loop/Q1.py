start = int(input("Enter start = "))
stop = int(input("Enter stop = "))

skip = int(input("Number you want to skip = "))

if start >= stop:
    print("Invalid range: start should be less than stop")
else:
    for i in range(start, stop):
        if i == skip:
            continue
        print(i)