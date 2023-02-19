""" Repeating actions

Repeating an action multiple times is what computers are really good at!
For this task you have the chance to show what you’ve learned about implementing repetition in code.
You are required to create a program that uses the while loop structure.
Write a program that always asks the user to enter a number.
When the user enters the negative number - 1, the program should stop requesting the user to enter a number.
The program must then calculate the average of the numbers entered excluding the - 1.
Make use of the while loop repetition structure to implement the program.
Use the trinket IDE below to write and test your code.
 """


next_input = 0
inputs = []
# ask the username to enter a number
while True:
    next_input = int(input('Please enter a number:'))
    if next_input == -1:
        break  # terminate a loop

    else:
        inputs.append(next_input)
# calculate the average of the numbers entered except -1
print(sum(inputs) / len(inputs))
