import math

def ex1():                                             #Calculate the distance between two points
    # Prompt the user to input the coordinates
    x1 = float(input("Enter the x-coordinate of point 1: "))
    y1 = float(input("Enter the y-coordinate of point 1: "))
    x2 = float(input("Enter the x-coordinate of point 2: "))
    y2 = float(input("Enter the y-coordinate of point 2: "))

    # Calculate the difference between the x-coordinates and y-coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the square of the differences
    dx_squared = dx ** 2
    dy_squared = dy ** 2

    # Calculate the sum of the squares and take the square root
    dist = math.sqrt(dx_squared + dy_squared)

    # Print the calculated distance
    print("The distance between the two points is:", dist)

def ex2():                                             #Find the most frequent letter in a string
    string = input("Input string:")
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print((max(letter_count, key=letter_count.get)))


def ex3():                                             #Find the sum of the first n natural numbers
    number = int(input("Input a number:"))
    sum = 0
    for i in range(number+1):
        sum += i
    print (sum)

def ex4():                                             #Find the sum of the digits of a number until it is a single digit
    number = int(input("Input a number:"))
    sum = 0
    while number > 9:
        sum += number % 10
        number = number / 10
    print(int(sum))


def ex5():                                             #Find the sum of the squares of the first n natural numbers
    number = int(input("Input a number:"))
    sum = 0
    for i in range(1, number + 1):
        sum += i ** 2
    print(sum)

