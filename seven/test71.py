car = input("What you want car?")

print("Let me see if I can find you a Subaru "+car)

people = input("How many people? ")
people = int(people)
if people > 8:
    print("No desk")
else:
    print("Please come in ")

number = input("Please input a number:")
number = int(number)

if number%10 == 0:
    print("数字 "+str(number)+" 是10的倍数")
else:
    print("数字 " + str(number) + " 不是10的倍数")