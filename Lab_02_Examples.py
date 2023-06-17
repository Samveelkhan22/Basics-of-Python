#Example:01 Print karachi Pakistan 100 times in a separate line
# i = 1
# while(i<=100):
#     print("Karachi Pakistan")
#     i+= 1

#Another way of to solve this problem
# i = 100
# while(i>=1):
#     print("Karachi Pakistan")
#     i-=1

#Example:02 Take collection of number input from user. Print the total positive and negative number.
# pcount= 0
# ncount= 0
# count=int(input("How many numbers you want?: "))
# i = 1
# while(i<=count):
#     num = int(input("Enter a number:" ))
#     if(num>=0):
#         pcount+=1
#     else:
#         ncount+=1
#     i+=1
# print("positive: ",pcount)
# print("negative: ",ncount)

#Example:03 Fixed a letter from a to e and then ask the user to guess that letter until correct letter entered.
# value = 'c'
# userValue = input("Guess a number from a to e: ")
# while(userValue!=value):
#     print("Incorrect")
#     userValue=input("Guess a number from a to e: ")
# print("Welcome User")