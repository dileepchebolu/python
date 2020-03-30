n = int(input())
phone = {}
for i in range(0,n):
    name = str(input())
    phone[name] = str(input())
for i in range(0,n):
    name = str(input())
    re = phone.get(name, "none")
    if re != "none":
        print("%s=%s"%(name,re))
        # #print({}={}.format("name", "re"))
    else:
        print("Not found")