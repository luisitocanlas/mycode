# read in the contents of a regular text file
# usernames.txt

# METHOD 1
# python needs to know what permissions does it have
# fileobj = open("usernames.txt", "r")
# read(), write(), readlines() all fileobj methods

# filecontents=fileobj.read()

# close open files when you're done!
# fileobj.close()

# print(filecontents)

# METHOD 2

# CONTEXT
with open("usernames.txt", "r") as fileobj:
    filecontents = fileobj.read()
# after indentation ends, files automatically closes!
print(filecontents)
    