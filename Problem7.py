s = input("Enter ")
c = s[::-1]
print (c)
complementary =""
com_rule={"T":"A", "A":"T","G":"C","C":"G"}
for i in c :
    complementary+= com_rule[i]
print (complementary)
