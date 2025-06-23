s={"a","b","c","d","e"}
print(s)
s1={1,2,3}
print(s1)
s.add("manish")
print(s)
s2=s.union(s1)
print(s2)
s1=set()
s2=set()
for i in range(7):
     s1.add(i)
for i in range(4,7):
    s2.add(i)
    s3=s1.intersection(s2)
    print(s3)
