users = ["admin","peter","Jack","Lily"]

for user in users:
    if "admin" in user:
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello "+user+",thank you for logging in again")

users = []
if users:
    for user in users:
        print("Hello"+user)
else:
    print("We need to find some users!")