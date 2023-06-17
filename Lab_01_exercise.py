#(i) Write a Python program to swap 4 variables 
# a = 2
# b = 56
# c = 78
# d = 9

# a, b, c, d = d, c, b, a

# print('The value of a after swapping: {}'.format(a))
# print('The value of b after swapping: {}'.format(b))
# print('The value of c after swapping: {}'.format(c))
# print('The value of d after swapping: {}'.format(d))

#(ii)Write a Python program to convert temperatures to and from celsius
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit is: ",(fahrenheit))

#Excercise dictionaries
#(ii)Write a python script to concatenate following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

#Excercise list comprehension 
#(i) Write a list comprehension which from a list generates a 
# lowecased version of each string that has lentgh greater than five.
# fruits = ["APPLE", "BANANNA", "CHERRY", "KIWI", "MANGO"]
# newfruits=[]
# for x in fruits:
#     if len(x)>5:
#         newfruits.append(x.lower())  
#     else:
#         newfruits.append(x)  

# print(newfruits)

#(ii) Write a python program to print a specified list after removing the 0th, 4th and 5th elements
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)