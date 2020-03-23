message1 = input("Tell me something,and I will repeat it back to you:")
print(message1)

promot = "\n Tell me something, and I will repeat it back to you:"
promot = "\n Enter 'quit' to end the program."
message = ""
while message != "quit":
    message = input(promot)
    if message != "quit":
        print(message)