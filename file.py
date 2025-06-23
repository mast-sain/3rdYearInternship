from os import close

# f=open("new1.text","w")
# f.write("baba tillu")
# f.close()
# f=open("new1",'r')


with open("new1.text",'r')as file:
 data=file.readline()
for line in data:
    word=line.split()
    print(word)