pizzas = ["chess","duck","beef","pepperoni"]
for pizza in pizzas:
    print(pizza)
    print("I like "+ pizza +"Pizza")
print("I really like pizza")

numbers = list(range(1,21))
for number in numbers:
    print(number)

big_number = list(range(1,1000001))
#for number in big_number:
#    print(number)

print(min(big_number))
print(max(big_number))
print(sum(big_number))

odd_number = list(range(1,21,2))
for number in odd_number:
    print(number)

three_number = list(range(3,31,3))
for number in three_number:
    print(number)

cube_number = []
for number in range(1,10):
    cube_number.append(number ** 3)
print(cube_number)

#列表解析的方式 生成一个列表
cube_numbers = [value**3 for value in range(1,10)]
print(cube_numbers)


my_pizza = ["pizza","falafel","carrot cake"]
friend_pizza = my_pizza[0:4]
my_pizza.append("ice cream")
friend_pizza.append("beef")

print(my_pizza)
print(friend_pizza)
for food in my_pizza:
    print(food)

for food in friend_pizza:
    print(food)