users ={
    "aeinstein":{
        "first":"albert",
        "last":"einstein",
        "location":"princeton"
    },
    "mcurie":{
        "first":"marie",
        "last":"curie",
        "location":"paris",
    }
}

for username,userinfo in users.items():
    print("\nuserName :"+username)
    full_name = userinfo["first"]+" " +userinfo["last"]
    location = userinfo["location"]

    print("\n Full_Name: "+full_name)
    print("\n location is "+ location)