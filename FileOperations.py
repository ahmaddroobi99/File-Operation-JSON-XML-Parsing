fp = open("person.sql", "r")
# content = fp.read()
# print(content)

# content = fp.readlines()
# print(content)
#
# print("\n")
# content = fp.readlines()
# print(content)


# for i in fp:
#     print(i)


fp = open("input2.txt", "w+")
print(fp.tell())
fp.write("sample text file 1")
print(fp.tell())
fp.seek(0, 0)
print(fp.tell())
content = fp.read()
print(fp.tell())
print(content)
fp = open("input2.txt", "a+")
fp.write("hi" )


# tell => current fp position
# seek(offest , position ) => to change the fp position
