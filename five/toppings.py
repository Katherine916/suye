requested_toppong = 'mushroom'
if requested_toppong  != 'anchovies':
    print("hold the anchovies")


"""关键字 In"""

requested_toppong = ["mushroom","onions","pineapple"]
print("mushrooms" in requested_toppong)


requested_toppong = ["mushroom","extra cheese"]
if 'mushroom' in requested_toppong:
    print("adding mushrooms")
if 'pepperoni' in requested_toppong:
    print("adding pepperoni")
if 'extra cheese' in requested_toppong:
    print("Adding extra pepperoni")
print("\nFinished making your pizza!")


requested_toppong = ["mushroom","extra cheese"]

for topping in requested_toppong:
    print("adding pepperoni"+topping)
print("\nFinished making your pizza!")



requested_toppong = ["mushroom","extra cheese","green peppers"]
for topping in requested_toppong:
    if topping == "green peppers":
        print("Sorry,we are out of green peppers right now!")
    else:
        print("adding pepperoni" + topping)
print("\nFinished making your pizza!!!!!!!")



available_toppings = ["mushroom","olives","extra chess","green peppers"]
requested_toppongs = ["mushroom","french fish","extra chess"]

for requested_toppong in requested_toppongs:
    if requested_toppong in available_toppings:
        print("Adding"+requested_toppong)
    else:
        print("Sorry we don't have"+topping)
print("\nFinished making your pizza!")


