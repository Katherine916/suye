new_users = ["Liky","Jack","Helen","Demon","Amy","Mick"]
curent_users = ["Liky","Jack","AMY"]

for user in new_users:
    if user in curent_users:
        print(user + "用户名已被使用，请重新输入")
    else:
         print(user + "用户未被使用")



