'''
Assignment #2

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
import numpy as np
import requests as r

def exercise01():
    # Create a list called animals containing the following animals: cat, dog, crouching tiger, hidden dragon, manta ray

    # ------ Place code below here \/ \/ \/ ------
    
    #list as specified
    animals = ["cat", "dog", "crouching tiger", "hidden dragon", "manta ray"]

    # ------ Place code above here /\ /\ /\ ------

    return animals


def exercise02():
    # Repeat exercise 1 and loop through and print each item in the animal list by iterating through an index number and using range(). Set the variable len_animals to the length of the animal list.

    # ------ Place code below here \/ \/ \/ ------
    
    #This probably would have been more efficient with a list comprehension to print the animals with one line of code.
    animals = ["cat", "dog", "crouching tiger", "hidden dragon", "manta ray"]
    
    len_animals = len(animals)
    
    for i in range(0,len_animals):
        
        print(animals[i])

    # ------ Place code above here /\ /\ /\ ------

    return animals, len_animals


def exercise03():
    # Reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list
    countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
    the_fifth_element = -999

    # ------ Place code below here \/ \/ \/ ------
    
    #sort is a nice, built-in function for sorting. Reverse is set to true to sort in descending order.
    countdown.sort(reverse = True)
    
    #since python lists start at zero, the fifth element is actually at index 4
    the_fifth_element = countdown[4]
    # ------ Place code above here /\ /\ /\ ------

    return countdown, the_fifth_element


def exercise04(more_temperatures, iot_sensor_points, a, b, c, d, e):
    # This exercise function receives a list of temperatures and a dictionary of temperature data where the key is an arbitrary sequential number and the value is the temperature and a,b,c,d and e are each a single temperature reading
    # To Do:
    # 1. Add all of the items in more_temperatures to the temperatures list
    # 2. Add all of the temperature values in iot_sensor_points to the temperatures list
    # 3. Add a,b,c,d and e to the temperature list
    # 4. Organize the temperatures in descending order
    # 5. The samples list will contain every 5th reading from the final temperatures list i.e in list [1,2,3,4,5,6,7,8,9,10] samples would be [5,10]
    # 6. Do a shallow copy of samples into copy_of_samples
    # 7. Organize samples in ascending order

    temperatures = list(np.random.randint(-25, 25, size=10))
    samples = []
    copy_of_samples = []

    # ------ Place code below here \/ \/ \/ ------
    
    #since the iot_sensor points were in a numpy array, I changed them to a list so they can be appended to the temperatures list.
    iot_sensor_list = [iot_sensor_points[i] for i in range(1,len(iot_sensor_points) + 1)]
    
    #I put all the misc temperatures into one list to make it more concise
    misc_temps = [a,b,c,d,e]
    
    #I appended together temperatures, more temperatures, iot sensor list, and misc temps into one big list and then sorted them in reverse.
    temperatures = temperatures + more_temperatures.tolist() + iot_sensor_list + misc_temps
    temperatures.sort(reverse = True)
    
    #Starting at the fifth element, I took every subsequent fifth element and stored it in samples
    samples = temperatures[4::5]
    
    #I made a deep copy instead of a shallow copy because a shallow copy changes when you sort the original.
    copy_of_samples = [item for item in samples]
    
    #Sorting the original will not change the order of the deep copy.
    samples.sort()
    
    # ------ Place code above here /\ /\ /\ ------

    return samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples


def exercise05(n):
    # This function will find n factorial using recursion (calling itself) and return the solution. For example exercise05(5) will return 120. No Python functions are to be used.

    # ------ Place code below here \/ \/ \/ ------
    
    #Checking if n is a positive integer
    if type(n) != int or n < 0:
        return("Please enter a valid number.")
    
    #If n = 0, 1, then recursion is over.
    elif n == 1 or n == 0:
        
        return(1)
        
    #Recurse when n != 1 or 0
    else:
    
        output = n * exercise05(n-1)
    
        return output
    
    # ------ Place code above here /\ /\ /\ ------


def exercise06(n):
     # This function will receive an arbitrary list of numbers of arbitrary size and find the average of those numbers. The size of the list may vary. Find the method that requires the  least amount of code. Return back the length, sum of list and average of list

    # ------ Place code below here \/ \/ \/ ------
    
    #This could have been done in one line (average_n = sum(n)/len(n))
    #But I had to specify the sum and the length explicitly.
    sum_n = sum(n)
    length_n = len(n)
    
    average_n = sum_n/length_n

    # ------ Place code above here /\ /\ /\ ------
    return length_n, sum_n, average_n


def exercise07(n):
    # This function looks for duplicates in list n. If there is a duplicate False is returned. If there are no duplicates True is returned.

    # ------ Place code below here \/ \/ \/ ------
    
    #Set function finds unique items in a list.
    set_n = set(n)
    
    #Count the total number of items in the list n.
    len_n = len(n)
    
    #If there are no duplicates, the number of total items and the number of unique items should be the same. 
    output = len_n == len(set_n)
    
    return output
    
    # ------ Place code above here /\ /\ /\ ------

# Exercise 8
# Create a function called display_menu that receives an argument called menu. The function should do the following:
# 1. Verify that menu is in fact a tuple. If it isnt, return back -1.
# 2. Determine the number of elements in menu
# 3. Loops through menu & enumerate through to the a menu to the screen. The test case will describe what the menu items are. The enumeration should be generate by code and not hardcoded.
# 4. Using input(), asks the user to select a menu item by entering a number and hitting Enter 
# 5. Validates if the number entered is a valid menu option and asks user to retry if number is not valid or is not a number / int
# 6. An exit menu option should be added at the end of the displayed list of menu options allowing the user to exit selecting a menu causing the display_menu() function to return back the number of the last menu option chosen prior to exit and also return the length of menu
# 7. If a valid menu option is chosen, call a function named similarly to the menu option that prints the menu option chosen i.e. def buy_burger() prints('Burger bought!')
# 8. The menu options should repeatedly be displayed after each selection (and appropriate delegate function is called) until user selects exist

# ------ Place code below here \/ \/ \/ ------

#do_thing function takes a menu option tuple and prints "item bought!" or "item sold!" depending on the input.
#this function will be used later when specific menu items are called.
def do_thing(option):
    
    if option[0] == "Buy":
        print(option[1] + " bought!")
        
    elif option[0] == "Sell":
        print(option[1] + " sold!")
    
    return()


def display_menu(menu):
    
    #stores the number of items in the menu
    num_items = len(menu)
    
    #checks if the menu is a tuple
    if type(menu) != tuple:
        
        return -1, num_items
    
    #if item is a tuple, continue with rest of function
    else:
        
        #enumerates through the menu items provided from the menu object starting at 1.
        listed_menu = list(enumerate(menu,1))
        
        #creates a list of valid selections based on the first element of each tuple in the menu
        valid_selections = [str(listed_menu[i][0]) for i in range(len(listed_menu))]
        
        #appends an exit option to the valid selection list
        valid_selections.append("exit")
        
        #specifies the initial input as "Nothing" in case user exits menu immediately
        previous_input = "Nothing"
        
        
        #infinite loop that allows user to perform as many actions as they want until they type "exit"
        while True:
            
            #for loop to print menu options
            #this loop will print the menu options before the user has made a selection
            for i in range(len(listed_menu)):
                menu_option = "Press " + str(listed_menu[i][0]) + " to " + listed_menu[i][1]
                print(menu_option)
            
            #added exit condition instruction
            print("Type 'exit' to exit menu")
            
            
            #prompts user for input
            user_input = input()
            
            
            #if the input is not in the valid_selections list, function will prompt user to make a valid selection and continue the loop
            #also, the user's input will be stored before continuing the loop
            if (user_input not in valid_selections) == True:
                
                previous_input = user_input
                print("Please choose a valid menu item.")
                continue
            
            #if the input is valid, but is not "exit", then the user's input is stored and the menu option is fetched from the menu.
            #afterwards, the do_thing function is called, which prints "item bought!" or "item sold!" depending on the input
            #after the do_thing function completes, the loop continues again
            elif user_input != "exit":
                
                user_input = int(user_input)
                previous_input = int(user_input)
                
                option = listed_menu[user_input - 1][1].split()
                
                do_thing(option)
                
                continue
            
            #if the user writes "exit", the loop ends
            else:
                print("Exiting menu")
                break
            
            
        #the previous input and number of items are returned
        return previous_input, num_items

# ------ Place code above here /\ /\ /\ ------

def exercise09():
    # Compile a list of 10 random URLs of dog pics

    dogs = []
    url = 'https://random.dog/woof.json'
    dog_media = r.get(url=url)
    print(str(dog_media.content))
    
    # ------ Place code below here \/ \/ \/ ------
    
    #List comprehension that fetches the json file from the url and converts it to a string.
    #Afterwards, the string is sliced to only include the url.
    dogs = [str(r.get(url=url).content)[10:-3:1] for i in range(10)]

    # ------ Place code above here /\ /\ /\ ------

    return dogs

def exercise10(sentence):

    # Exercise10 receives an arbitrary string. Return the sentence backwards with the cases inverted and spaces an underscore _, i.e. HelLo returns OlLEh
    reversed = ''

    # ------ Place code below here \/ \/ \/ ------
    
    #First part reverses sentence
    #second part swaps the cases
    #third part replaces spaces with underscores
    reversed = sentence[::-1].swapcase().replace(" ","_")

    # ------ Place code above here /\ /\ /\ ------
    return reversed


class TestAssignment2(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        a = exercise01()
        self.assertEqual(len(a), 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)
    
    def test_exercise02(self):
        print('Testing exercise 2')
        a, l = exercise02()
        self.assertEqual(len(a), 5)
        self.assertEqual(l, 5)
        self.assertTrue('cat' in a)
        self.assertTrue('dog' in a)
        self.assertTrue('manta ray' in a)

    def test_exercise03(self):
        print('Testing exercise 3')
        c, tfe = exercise03()
        self.assertEqual(c[0], 10)
        self.assertEqual(c[11], -5)
        self.assertEqual(len(c), 12)
        self.assertEqual(tfe, 6)

    def test_exercise04(self):
        print('Testing exercise 4')
        more_temperatures = np.random.randint(300, 400, size=25)
        iot_sensor_points = {1: 801, 2: 644, 3: 991, 4: 721,
                             5: 752, 6: 871, 7: 991, 8: 1023, 9: 804, 10: 882}
        samples, temperatures, more_temperatures, iot_sensor_points, a, b, c, d, e, copy_of_samples = exercise04(more_temperatures, iot_sensor_points,
                                                                                                                 8000, 8500, 9000, 9500, 9999)

        self.assertEqual(len(temperatures), 50)
        self.assertEqual(len(samples), 10)
        self.assertEqual(temperatures[0], 9999)
        self.assertEqual(temperatures[11], 801)
        self.assertEqual(samples[9], 8000)
        self.assertEqual(copy_of_samples[0], 8000)
        self.assertEqual(a, 8000)
        self.assertEqual(b, 8500)
        self.assertEqual(c, 9000)
        self.assertEqual(d, 9500)
        self.assertEqual(e, 9999)

    def test_exercise05(self):
        print('Testing exercise 5')
        self.assertEqual(exercise05(5), 120)
        self.assertEqual(exercise05(10), 3628800)

    def test_exercise06(self):
        print('Testing exercise 6')
        length_n, sum_n, average_n = exercise06([1, 2, 3, 4, 5])
        self.assertEqual(average_n, 3)
        self.assertEqual(length_n, 5)
        length_n, sum_n, average_n = exercise06([1, 2, 120])
        self.assertEqual(average_n, 41)
        self.assertEqual(length_n, 3)

    def test_exercise07(self):
        print('Testing exercise 7')
        self.assertTrue(exercise07([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True)
        self.assertTrue(exercise07([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == False)
        self.assertTrue(exercise07([1, 2.00002, 2.00001, 4, 5, 6, 7, 8, 9, 10]) == True)

    def test_exercise08(self):
        print('Testing exercise 8')
        menu = ['Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum']
        r, l = display_menu(menu)
        self.assertEqual(r,-1)
        self.assertEqual(l,4)
        menu = ('Buy Bitcoin','Buy Ethereum','Sell Bitcoin','Sell Ethereum')
        r, l = display_menu(menu)
        self.assertTrue(r > 0)
        self.assertEqual(l,4)
    
    def test_exercise09(self):
        print('Testing exercise 9')
        dogs = exercise09()
        for d in dogs:
            print(d)
        self.assertTrue('https://random.dog/' in d)
            

    def test_exercise10(self):
        print('Testing exercise 10')
        self.assertEqual(exercise10('HellO'),'oLLEh')
        self.assertEqual(exercise10('ThIs Is MaD'),'dAm_Si_SiHt')




if __name__ == '__main__':
    unittest.main()
