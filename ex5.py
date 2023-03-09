import math
import unittest
from unittest.mock import patch
from io import StringIO


def ex1(x1,y1,x2,y2):                                        #Calculate the distance between two points

    # Calculate the difference between the x-coordinates and y-coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the square of the differences
    dx_squared = dx ** 2
    dy_squared = dy ** 2

    # Calculate the sum of the squares and take the square root
    dist = math.sqrt(dx_squared + dy_squared)

    # Print the calculated distance
    return ("The distance between the two points is:", dist)


def ex2(string):                                             #Find the most frequent letter in a string
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return ((max(letter_count, key=letter_count.get)))


def ex3(number):                                             #Find the sum of the first n natural numbers
    sum = 0
    for i in range(number+1):
        sum += i
    return (sum)


def ex4(number):                                             #Find the sum of the digits of a number until it is a single digit
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    if sum <= 9:
        return sum
    else:
        return ex4(sum)


def ex5(number):                                             #Find the sum of the squares of the first n natural numbers
    if number > 0:
        sum = 0
        for i in range(1, number + 1):
            sum += i ** 2
        return (sum)
    else:
        return None


#Unit tests


class TestEx1(unittest.TestCase):
    def test_distance(self):
        self.assertAlmostEqual(ex1(0,0,3,4), ("The distance between the two points is:", 5))
        self.assertAlmostEqual(ex1(-1,-1,-4,-5), ("The distance between the two points is:", 5))
        self.assertAlmostEqual(ex1(0,0,0,0), ("The distance between the two points is:", 0))
        self.assertAlmostEqual(ex1(0,0,1,1), ("The distance between the two points is:", math.sqrt(2)))
        self.assertAlmostEqual(ex1(0,0,-1,-1), ("The distance between the two points is:", math.sqrt(2)))
        self.assertAlmostEqual(ex1(0,0,0,1), ("The distance between the two points is:", 1))
        self.assertAlmostEqual(ex1(0,0,1,0), ("The distance between the two points is:", 1))


class TestEx2(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(ex2("a"), "a")

    def test_empty_string(self):
        self.assertRaises(ValueError, ex2, "")

    def test_all_letters_same_frequency(self):
        self.assertEqual(ex2("abcdeee"), "e")

    def test_multiple_frequent_letters(self):
        self.assertEqual(ex2("aabbccddd"), "d")

    def test_ignore_case(self):
        self.assertEqual(ex2("aAbBcC"), "a")


class TestEx3(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(ex3(0), 0)

    def test_one(self):
        self.assertEqual(ex3(1), 1)

    def test_small_number(self):
        self.assertEqual(ex3(5), 15)

    def test_large_number(self):
        self.assertEqual(ex3(100), 5050)


class TestEx4(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(ex4(123), 6)
        self.assertEqual(ex4(54321), 6)
        self.assertEqual(ex4(999), 9)
        self.assertEqual(ex4(100), 1)

    def test_zero_input(self):
        self.assertEqual(ex4(0), 0)

    def test_single_digit_input(self):
        self.assertEqual(ex4(5), 5)


class TestEx5(unittest.TestCase):

    def test_ex5_1(self):
        self.assertEqual(ex5(1), 1)

    def test_ex5_5(self):
        self.assertEqual(ex5(5), 55)

    def test_ex5_10(self):
        self.assertEqual(ex5(10), 385)

    def test_negative_number(self):
        self.assertEqual(ex5(-1), None)


if __name__ == '__main__':
    unittest.main()