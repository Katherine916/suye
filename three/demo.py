friend = ["lily","jack","demon","helen"]
print(friend)

print(friend[0])


print(friend[0].title())

friend[2] = "steven"
print(friend)

friend.append("jack")
print(friend)

friend.insert(2,"demon")
print(friend)

del friend[2]
print(friend)

friend.remove("steven")
print(friend)

friend.pop()
print(friend)
