friend = ["Katherine","Lily","Demon"]
print(friend)
print(friend[2]+" can't join")

friend[2] = "steven"
print(friend)
print("I find a big desk")

friend.insert(0,"Helln")
friend.insert(4,"Jack")
friend.insert(5,"Seamon")
print(friend)
print("----------------------------")

# 为什么pop 删除到数组为2 就不删除了
for friends in friend:
    pop_frinend = friend.pop()
    print(friend)
del friend[2]
del friend[1]
del friend[0]
print(friend)