
# file write:
# f = open('test.txt','w')
# f.write("hello world")
# f.close()

# append in previous file:
fa = open('test.txt','a')
fa.write('hello i am new text')

# file read:
file = open('test.txt','r')
print(file.read())