'''
Assignment #1

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 01_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch


'''
import math
import unittest


def exercise_example():
    # Create a variable y and set it to 5.

    # ------ Place code below here \/ \/ \/ ------

    y = 5  # Example of code you would add

    # ------ Place code above here /\ /\ /\ ------
    return y


def exercise01():
    # Create a variable x and set it to 5.

    # ------ Place code below here \/ \/ \/ ------
    
    #Not much to say here, just want to get in the habit of leaving comments.
    
    x = 5

    # ------ Place code above here /\ /\ /\ ------

    return x


def exercise02():
    # Create a string variable called name and set it to your first name.

    # ------ Place code below here \/ \/ \/ ------
    
    #Defined a variable as a string first before storing my name in it.
    #I know it's possible to just assign my name directly without declaring the type.
    
    name = str()
    name ="Austin"
    
    # ------ Place code above here /\ /\ /\ ------

    return name


def exercise03():
    # Create a string variable called sentence and assign it to an arbitrary sentence that contains at least 3 words

    # ------ Place code below here \/ \/ \/ ------

    #Didn't declare the variable as a string first.

    sentence ="This is a sentence."

    # ------ Place code above here /\ /\ /\ ------

    return sentence


def exercise04():
    # Create two string variables. The first variable is called first_name, the second is last_name. Set both variables to your first name and last name respectively.

    # ------ Place code below here \/ \/ \/ ------

    #Mostly a repeat of exercise2

    first_name = str()
    last_name = str()
    
    first_name ="Austin"
    last_name ="Chan"

    # ------ Place code above here /\ /\ /\ ------

    return first_name, last_name


def exercise05():

    # Repeate exercise 4 here and assign the datatype of the variable first_name to a variable called name_type

    # ------ Place code below here \/ \/ \/ ------

    #The only difference between this and exercise4 is that I checked the type of first name, as instructed.

    first_name = str()
    last_name = str()
    
    first_name ="Austin"
    last_name ="Chan"

    name_type = type(first_name)

    # ------ Place code above here /\ /\ /\ ------

    return first_name, last_name, name_type


def exercise06():
    # Assign 20 to the variable hours_worked, 15 to the variable wage_per_hour and the product of the two to variable total_pay

    # ------ Place code below here \/ \/ \/ ------

    #Assigned the two variables and then multiplied them together.

    hours_worked = 20
    wage_per_hour = 15
    
    total_pay = hours_worked * wage_per_hour

    # ------ Place code above here /\ /\ /\ ------
    return hours_worked, wage_per_hour, total_pay


def exercise07():
    # Create a variable wage and assign 17.0 to it. Print to the screen the datatype of wage. Create a second variable called doubled that prints to the screen 2 times wage
    # ------ Place code below here \/ \/ \/ ------

    #Used the print function to print the data type of wage and the value of doubled.

    wage = 17.0
    print(type(wage))
    
    doubled = wage * 2
    print(doubled)

    # ------ Place code above here /\ /\ /\ ------
    return wage, doubled


def exercise08():
    # Assign 5 to the variable quantity, 'hello' to the variable hello and a variable hello_repeated that holds a string that contains whatever is contained in the variable hello repeated quantity times

    # ------ Place code below here \/ \/ \/ ------

    #Strings can't be multiplied to each other, but strings and integers can be multiplied.
    #I think python just repeats the string however many times you multiply it.
    #So in this case, "hello" is repeated 5 times.

    quantity = 5
    hello = "hello"
    
    hello_repeated = hello * quantity

    # ------ Place code above here /\ /\ /\ ------

    return quantity, hello, hello_repeated


def exercise09():
    # Assign 10 to a variable qty, 5 to a variable price and the product of the two to a variable total_cost

    # ------ Place code below here \/ \/ \/ ------

    #Integers can be multiplied with each other, as expected.

    qty = 10
    price = 5
    
    total_cost = qty * price

    # ------ Place code above here /\ /\ /\ ------

    return qty, price, total_cost


def exercise10():
    # Create 5 variables named factorN where N is the numbers 1 to 5 and set them to 1 through 5, respectively. Create a variable called product that holds the product of the 5 variables

    # ------ Place code below here \/ \/ \/ ------

    #This probably would have been more elegant with a dictionary, but then factorN technically wouldn't be a variable.
    #Anyway, I used multiple variable assignment instead, which is easier than writing 5 lines.

    factor1, factor2, factor3, factor4, factor5 = 1, 2, 3, 4, 5

    product = factor1 * factor2 * factor3 * factor4 * factor5

    # ------ Place code above here /\ /\ /\ ------

    return factor1, factor2, factor3, factor4, factor5, product


def exercise11():
    # Create a variable pi and literally set it to pi 10 decimal places out

    # ------ Place code below here \/ \/ \/ ------

    #The way I did this was a little unconventional.
    #The round() function doesn't specify if you want to round up or down.
    #So instead I multiplied pi by 10^10, rounded down and then divided by 10^10.
    #This lets me round down with 10 decimal places.

    pi = math.floor((math.pi * (10 ** 10)))/(10 ** 10)

    # ------ Place code above here /\ /\ /\ ------
    return pi


def exercise12():
    # Create a variable called x and set it to 10. Then create a variable y that equals to x to the 7th power

    # ------ Place code below here \/ \/ \/ ------

    #The operator for exponents is **, as demonstrated below.

    x = 10
    y = x ** 7

    # ------ Place code above here /\ /\ /\ ------
    return x, y


def exercise13():
    # Create variables volume_sphere, r. Set r to 7 and calculate the volume of the sphere with r = 7 and assign it to volume_sphere

    pi = 3.14159
    # ------ Place code below here \/ \/ \/ ------

    #volume_sphere and radius are initialized here

    volume_sphere = float()
    r = 7
    
    #The formula for the volume of a sphere is 4/3*pi*radius^3
    
    volume_sphere = (4/3) * pi * (r ** 3)

    # ------ Place code above here /\ /\ /\ ------
    return pi, r, volume_sphere


def exercise14():
    # Create a variables area, length, height. Set length and height equal to 50 and 10.2 respectively. Assign area to the product of length and height, assign the variable area_type to the datatype of area

    # ------ Place code below here \/ \/ \/ ------

    #I noticed with this problem there was some weird rounding.
    #Instead of 510, python makes it 509.999999999 instead.
    #I wonder if it has anything to do with multiplying variables of different types.

    length = 50
    height = 10.2
    
    area = length * height
    area_type = type(area)

    # ------ Place code above here /\ /\ /\ ------
    return area, length, height, area_type


def exercise15():
    # Calculate the distance covered by a car moving at 80 miles per hour for 3 hours

    # ------ Place code below here \/ \/ \/ ------

    #When multiplying integers, it works properly as expected.

    speed_mph = 80
    duration = 3
    
    distance = speed_mph * duration

    # ------ Place code above here /\ /\ /\ ------

    return distance, speed_mph, duration


def exercise16():
    # Implement pythogorean thereom and find the length of hypotenuse c given sides a and b. Select any numbers for a and b. Use math.sqrt() for square root.

    # ------ Place code below here \/ \/ \/ ------

    #Classic 3,4,5 triangle.
    #Pythogorean theorem is a^2 + b^2 = c^2
    #To get c, just take the square root of (a^2 + b^2) 

    a = 3
    b = 4
    
    c = math.sqrt((a ** 2) + (b ** 2))

    # ------ Place code above here /\ /\ /\ ------
    return a, b, c


# ---------------------- Do not modify code below this line ----------------------

class TestAssignment1(unittest.TestCase):

    def test_exercise1(self):
        print('Testing exercise 1')
        self.assertEqual(exercise01(), 5)

    def test_exercise2(self):
        print('Testing exercise 2')
        self.assertTrue(isinstance(exercise02(), str))
        self.assertGreater(len(exercise02()), 1)

    def test_exercise3(self):
        print('Testing exercise 3')
        words = exercise03().split(' ')
        self.assertGreater(len(words), 2)

    def test_exercise4(self):
        print('Testing exercise 4')
        f, l = exercise04()
        self.assertTrue(isinstance(f, str))
        self.assertGreater(len(f), 0)
        self.assertTrue(isinstance(l, str))
        self.assertGreater(len(l), 0)

    def test_exercise5(self):
        print('Testing exercise 5')
        f, l, nt = exercise05()
        self.assertTrue(isinstance(f, str))
        self.assertGreater(len(f), 0)
        self.assertTrue(isinstance(l, str))
        self.assertGreater(len(l), 0)
        self.assertTrue(isinstance(nt, type))

    def test_exercise6(self):
        print('Testing exercise 6')
        h, w, p = exercise06()
        self.assertTrue(isinstance(h, int))
        self.assertTrue(isinstance(w, int))
        self.assertTrue(isinstance(p, int))
        self.assertEqual(h, p/w)

    def test_exercise7(self):
        print('Testing exercise 7')
        w, d = exercise07()
        self.assertTrue(isinstance(w, float))
        self.assertTrue(isinstance(d, float))
        self.assertEqual(w, 17.0)

    def test_exercise8(self):
        print('Testing exercise 8')
        q, h, hr = exercise08()
        self.assertTrue(isinstance(q, int))
        self.assertTrue(isinstance(h, str))
        self.assertTrue(isinstance(hr, str))
        self.assertEqual(hr, 'hellohellohellohellohello')

    def test_exercise9(self):
        print('Testing exercise 9')
        q, p, tc = exercise09()
        self.assertTrue(isinstance(q, int))
        self.assertTrue(isinstance(p, int))
        self.assertTrue(isinstance(tc, int))
        self.assertEqual(q, tc/p)

    def test_exercise10(self):
        print('Testing exercise 10')
        f1, f2, f3, f4, f5, p = exercise10()
        self.assertEqual(f1, 1)
        self.assertEqual(f2, 2)
        self.assertEqual(f3, 3)
        self.assertEqual(f4, 4)
        self.assertEqual(f5, 5)
        self.assertEqual(p, 120)

    def test_exercise11(self):
        print('Testing exercise 11')
        p = exercise11()
        self.assertEqual(p, 3.1415926535)

    def test_exercise12(self):
        print('Testing exercise 12')
        x, y = exercise12()
        self.assertEqual(x, 10)
        self.assertEqual(y, 10000000)

    def test_exercise13(self):
        print('Testing exercise 13')
        p, r, vs = exercise13()
        self.assertLess(vs, 1436.8)
        self.assertGreater(vs, 1436.7)
        self.assertEqual(r, 7)
        self.assertEqual(p, 3.14159)

    def test_exercise14(self):
        print('Testing exercise 14')
        a, l, h, at = exercise14()
        self.assertGreater(a, 509)
        self.assertLess(a, 510)
        self.assertEqual(l, 50)
        self.assertEqual(h, 10.2)
        self.assertTrue(isinstance(at, type))

    def test_exercise15(self):
        print('Testing exercise 15')
        di, s, du = exercise15()
        self.assertEqual(s, 80)
        self.assertEqual(du, 3)
        self.assertEqual(s, di / du)

    def test_exercise16(self):
        print('Not testing exercise 16')


if __name__ == '__main__':
    unittest.main()
