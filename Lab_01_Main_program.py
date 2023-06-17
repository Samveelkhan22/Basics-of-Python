# Program to find the sum of all even numbers in a list

def find_even_sum(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function
result = find_even_sum(numbers)

# Print the result
print("The sum of all even numbers in the list is:", result)

# Program to find the largest and smallest number in a tuple

def find_largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

# Tuple of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Call the function
largest, smallest = find_largest_smallest(numbers)

# Print the result
print("The largest number in the tuple is:", largest)
print("The smallest number in the tuple is:", smallest)

# Program to print the multiplication table of a number

def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Input from the user
table_num = int(input("Enter a number to print its multiplication table: "))

# Call the function
print_table(table_num)

# Program to print the Fibonacci series up to a given number

def print_fibonacci(num):
    a, b = 0, 1
    while b < num:
        print(b, end=", ")
        a, b = b, a + b

# Input from the user
fib_num = int(input("Enter a number to print the Fibonacci series up to: "))

# Call the function
print("The Fibonacci series up to", fib_num, "is:")
print_fibonacci(fib_num)

# Program to store and print the details of a person

def print_details(name, age, address, phone):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
    print("Phone:", phone)

# Dictionary to store the details of a person
person = {
    "name": "John Doe",
    "age": 30,
    "address": "123 Main St, Anytown, USA",
    "phone": "555-555-5555"
}

# Call the function
print_details(person["name"], person["age"], person["address"], person["phone"])