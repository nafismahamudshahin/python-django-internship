# a for append and do not delete previous data
# r for read
# w for write and delete previous data


with open('test1.txt','a') as f1:
    f1.write("hello is am shahin\n")

with open('test1.txt','r') as read:
    print(read.read())