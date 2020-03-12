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
