#!/usr/bin/env python3

mylist1 = ["ssh", "http", "https"]
mylist2 = ["ssh", "http", "https"]

# ["ssh", "http", "https", "dns"]
mylist1.append("dns")
mylist2.append("dns")
print(mylist1)

# ["ssh", "http", "https", "dns", 22, 80, 443, 53]
numlist = [22, 80, 443, 53]
mylist1.extend(numlist)
print(mylist1)

# ["ssh", "http", "https", "dns", [22, 80, 443, 53]]
mylist2.append(numlist)
print(mylist2)

