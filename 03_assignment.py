'''
Assignment #3
1. Add / modify code ONLY between the marked areas (i.e. "Place code below"). Do not modify or add code elsewhere.
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 03_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch in Github
8. Use the test cases to infer requirements wherever feasible
'''
import csv, json, math, pandas as pd, requests, unittest, uuid

# ------ Declare your classes here ONLY \/ \/ \/ ------

# Box class declaration below here
class Box:
    
    #====================================================#
    #====================================================#
    
    #Initialize the private length and width parameters of the box
    
    def __init__(self,length,width):
        
        #checks if input are both ints
        if(type(length) != int or type(width) != int):
            
            raise AttributeError("Length or Width is not int")
            
        #checks if input is less than 1
        elif(length < 1 or width < 1):
            
            raise AttributeError("Length or Width is less than 1")
            
        #initializes box if inputs are valid
        else:
        
            self.__length = length
            self.__width = width
    
    #====================================================#
    #====================================================#
    
    #fetches length
    
    def get_length(self):
        return(self.__length)
    
    
    #====================================================#
    #====================================================#
    
    #fetches width
    
    def get_width(self):
        return(self.__width)
    
    
    #====================================================#
    #====================================================#
    
    #Print the box with asterisks
    
    def render(self):
        
        #for each unit length of the box, print asterisks according to the row
        for row in range(self.__length):
            
            #first and last rows print asterisks times width
            if(row == 0 or row == self.__length - 1):
            
                print("*"*self.__width)
            
            #all other rows print one asterisk, width - 2 empty spaces, and another asterisk
            else:
                
                print("*" + (" "*(self.__width - 2)) +"*")
    
    #====================================================#
    #====================================================#
    
    #Swaps length and width
    
    def invert(self):
        
        #put length and width into temporary variables
        temp_length = self.__length
        temp_width = self.__width
        
        #assigns temp variables to be the new length and width
        self.__length = temp_width
        self.__width = temp_length
        
    #====================================================#
    #====================================================#
    
    #Get area of rectangle
    
    def get_area(self):
        
        #length times width is area
        return(self.__length * self.__width)
    
    #====================================================#
    #====================================================#
    
    #Get perimeter of rectangle
    
    def get_perimeter(self):
        
        #two times (length + width) is perimeter
        return(2*(self.__length + self.__width))
    
    #====================================================#
    #====================================================#
    
    #Doubles width of rectangle
    
    def double(self):
        
        #two times width
        doubled_width = self.__width * 2
        
        #assigns doubled width to the width of the rectangle
        self.__width = doubled_width
        
        return(self)
    
    #====================================================#
    #====================================================#
    
    #Equality statement
    
    def __eq__(self,other):
        
        #checks if other object is a box
        if(isinstance(other,Box) == True):
            
            #checks if the length and width of the other box are the same
            same_width = self.__width == other.__width
            same_length = self.__length == other.__length
            
            
            #if both the length and width are the same for both boxes, return true, else false
            if(same_width + same_length == 2):
                
                return(True)
                
            else:
                
                return(False)
                
                
        #if other object is not a box, return false
        else:
            
            return(False)
        
    #====================================================#
    #====================================================#
    
    def print_dim(self):
        
        print("Length of box is: " + str(self.__length))
        print("Width of box is: " + str(self.__width))
    
    
    #====================================================#
    #====================================================#
    
    #gets dimension of the box
    
    def get_dim(self):
        
        #puts length and width of box into a tuple and returns it
        output = (self.__length,self.__width)
        
        return(output)
    
    
    #====================================================#
    #====================================================#
    
    #combines length and width of two boxes
    
    def combine(self,other):
        
        #checks if other object is a box
        if(isinstance(other,Box) == True):
            
            #adds lengths and widths together
            big_width = self.__width + other.__width
            big_length = self.__length + other.__length
            
            #assigns new combined lengths and widths to current box
            self.__width = big_width
            self.__length = big_length
            
            return(self)
        
        #if other object is not a box, raises error
        else:
            
            raise TypeError("Cannot combine non-boxes")


    #====================================================#
    #====================================================#
    
    #calculates hypotenuse
    
    def get_hypot(self):
        
        #squares the length and width
        a_square = self.__length ** 2
        b_square = self.__width ** 2
        
        #takes square root of the sum of length and width to get hypotenuse
        hypot = math.sqrt(a_square + b_square)
    
        return(hypot)

    #====================================================#
    #====================================================#
    #====================================================#
    #================== BOX ENDS HERE ===================#
    #====================================================#
    #====================================================#
    #====================================================#




class MangoDB:
  
    #====================================================#
    #====================================================#
    
    #initializes MangoDB
    
    def __init__(self):
        
        #creates default collection
        self.__collections = {'default0':{
                'version': 'v1.0',
                'db': 'mangodb',
                'uuid': str(uuid.uuid4())}}
        
        
        #creates list of collection names
        self.__collection_names = ['default0']
     
    #====================================================#
    #====================================================#
        
    #displays all collections
    
    def display_all_collections(self):
        
        #uses json.dumps function to format the dictionary for easy reading
        #indent = 2 allows for two levels of indentation
        #sort_keys sorts the keys
        print(json.dumps(self.__collections, indent = 2, sort_keys = True))
     
        
    #====================================================#
    #====================================================#

    #adds collection to existing collections
        
    def add_collection(self,collection_name):
        
        
        #checks if collection name is a string
        if(type(collection_name) != str):
            
            raise AttributeError("Collection name is not string")
            
        #checks if collection already exists
        elif(collection_name in self.__collection_names):
            
            raise KeyError("Collection name already exists")
        
        #creates empty dictionary for collection
        else:
            
            self.__collections[collection_name] = {}
            self.__collection_names.append(collection_name)
    

    #====================================================#
    #====================================================#

    #update collection
    
    def update_collection(self,collection_name,items):
        
        
        #checks if collection name is a string
        if(type(collection_name) != str):
            
            raise AttributeError("Collection name is not string")
            
            
        #checks if collection name exists
        elif(collection_name not in self.__collection_names):
            
            raise AttributeError("Collection name does not exist")
        
        
        #checks if new items are in dictionary format
        elif(type(items) != dict):
            
            raise AttributeError("Items are not a dictionary")
            
            
        #appends dictionary items to collection
        else:         
            
            self.__collections[collection_name] = {**self.__collections[collection_name],**items}
            
    #====================================================#
    #====================================================#
            
    #remove collection        
    
    def remove_collection(self,collection_name):
        
        #checks if collection name is a string
        if(type(collection_name) != str):
            
            raise AttributeError("Collection name is not string")
            
            
        #checks if collection name exists
        elif(collection_name not in self.__collection_names):
            
            raise AttributeError("Collection name does not exist")
            
            
        #prevents default collection from being removed
        elif(collection_name == "default0"):
        
            raise AttributeError("Cannot delete default collection")
            
            
        #removes collection
        else:
            
            del self.__collections[collection_name]
            
            self.__collection_names.remove(collection_name)
            
    #====================================================#
    #====================================================#

    #list collections (twice? why twice?)

    def list_collections(self):
        
        print(self.__collection_names * 2)
                
    #====================================================#
    #====================================================#


    def get_collection_size(self,collection_name):
        
        #checks if collection name is a string
        if(type(collection_name) != str):
            
            raise AttributeError("Collection name is not string")
            
            
        #checks if collection name exists
        elif(collection_name not in self.__collection_names):
            
            raise AttributeError("Collection name does not exist")
            
            
        #return the number of items in a collection
        else:
            
            return(len(self.__collections[collection_name].keys()))
            
            
    #====================================================#
    #====================================================#    
           
    #converts dictionary to json string format
    
    def to_json(self,collection_name):
        
        #checks if collection name is a string
        if(type(collection_name) != str):
            
            raise AttributeError("Collection name is not string")
            
            
        #checks if collection name exists
        elif(collection_name not in self.__collection_names):
            
            raise AttributeError("Collection name does not exist")
            
        #uses json.dumps function to format dictionary in json friendly format
        else:
        
            return(json.dumps(self.__collections[collection_name]))
            
    #====================================================#
    #====================================================#    
    
    #wipes database
    
    def wipe(self):
        
        #reassigns the collections variable to only include the default collection
        self.__collections = {"default0":self.__collections["default0"]}
        
        #resets the collection name list to only include the default collection
        self.__collection_names = ["default0"]
    
    #====================================================#
    #====================================================#
    
    #creates list of all available collections
    
    def get_collection_names(self):
        
        #list comprehension concatenates "collection-" to each key and returns the list
        collection_names = ["collection-" + item for item in list(self.__collections.keys())]
        
        return(collection_names)

    #====================================================#
    #====================================================#
    
    #fetches uuid
    
    def fetch_uuid(self):
        
        #there was no easy way to fetch the uuid using the existing methods, so I made a method that explicitly returns the uuid
        return(self.__collections["default0"]["uuid"])
    
    


# ------ Create your classes here /\ /\ /\ ------


def exercise03():
    '''
    1. Avocado toast is expensive but enormously yummy. What's going on with avocado prices? Read about avocado prices (https://www.kaggle.com/neuromusic/avocado-prices/home)
    2. Load the included avocado.csv file and display every other line to the screen, i.e. line 1,3,5..
    3. Open the file name under csv_file
    4. The reader should be named reader
    5. Use only the imported csv library to read and print out the avacodo file
    '''
    
    #opens file avocado.csv
    with open('avocado.csv') as csv_file:
        
        #initializes counter to count odd numbered lines
        counter = 0
        
        #reads file
        reader = csv.reader(csv_file)
        
        #prints file
        for r in reader:
            
            #increments counter
            counter += 1
            
            #if counter is not divisible by 2, print line
            if(counter % 2 != 0):
                
                #prints line
                print(r)
            
            #else, go to next loop
            else:
                
                continue

    return csv_file, reader


def exercise02():
    '''
    Create a class called MangoDB. The MangoDB class wraps a dictionary of dictionaries. At the the root level, each key/value will be called a collection, similar to the terminology used by MongoDB, an inferior version of MangoDB ;) A collection is a series of 2nd level key/value paries. The root value key is the name of the collection and the value is another dictionary containing arbitrary data for that collection.
    For example:
        {
            'default0': {
            'version': v1.5,
            'db':'mangodb',
            'uuid':'0fd7575d-d331-41b7-9598-33d6c9a1eae3'
            },
        {
            'temperatures': {
                1: 50,
                2: 100,
                3: 120
            }
        }
    
    The above is a representation of a dictionary of dictionaries. Default0 and temperatures are collections or root keys. The default0 collection has a series of key/value pairs that make up the collection. The MangoDB class should create the default collection, similar to what's shown here:
                collection: default0
                    version: v1.0
                    db: mangodb
                    uuid: 739bd6e8-c458-402d-9f2b-7012594cd741 
    
    On a MangoDB instance being created include a randomly generated uuid using the uuid4() method and have the following methods:
        - display_all_collections() which iterates through every collection and prints to screen each collection names and the collection's content underneath and may look something like:
            collection: default0
                collection: default0
                    version: v1.0
                    db: mangodb
                    uuid: 739bd6e8-c458-402d-9f2b-7012594cd741 
            collection: temperatures
                1 50
                2 100 
        - add_collection(collection_name) allows the caller to add a new collection by providing a name. The collection will be empty but will have a name.
        - update_collection(collection_name,updates) allows the caller to insert new items into a collection i.e. 
                db = MangoDB()
                db.add_collection('temperatures')
                db.update_collection('temperatures',{1:50,2:100})
        - remove_collection() allows caller to delete the collection and its associated data
        - list_collections() displays a list of all the collections twice
        - get_collection_size(collection_name) finds the number of key/value pairs in a given collection
        - to_json(collection_name) that converts the collection to a JSON string
        - wipe entirely cleans out the db and resets it with just a default0 collection
        - get_collection_names() that returns a list of collection names, with each name prefixed with the string 'collection-' 
        Make sure to never expose the underlying data structures
        For exercise02(), perform the following:
        - Create an instance of MangoDB
        - Add a collection called testscores
        - Take the test_scores list and insert it into the testscores collection, providing a sequential key i.e 1,2,3...
        - Display the size of the testscores collection
        - Display a list of collections
        - Display the db's UUID
        - Wipe the database clean
        - Display the db's UUID again
    '''

    test_scores = [99,89,88,75,66,92,75,94,88,87,88,68,51]

    # ------ Place code below here \/ \/ \/ ------

    #create an instance of MangoDB
    db = MangoDB()
    
    #Add a collection called testscores
    db.add_collection("testscores")
    
    #creates keys and zips them into test score dictionary
    test_score_range = [i for i in range(1,len(test_scores) + 1)]
    test_score_dict = dict(zip(test_score_range,test_scores))
    
    #Insert test scores list into testscores collection
    db.update_collection("testscores",test_score_dict)
    
    #Display the size of the testscores collection
    db.get_collection_size("testscores")
    
    #Display a list of collections
    db.get_collection_names()
    
    #Display the db's UUID
    db.fetch_uuid()

    #Wipe the database clean
    db.wipe()
    
    #Display the db's UUID again
    db.fetch_uuid()

    # ------ Place code above here /\ /\ /\ ------

def exercise01():

    '''
        Create an immutable class Box that has private attributes length and width that takes values for length and width upon construction (instantiation via the constructor). Make sure to use Python 3 semantics. Make sure the length and width attributes are private and accessible only via getters.
        
        In addition, create...
        - A method called render() that prints out to the screen an unfilled box made with asterisks of length and width perimeter
        - A method called invert() that switches length and width with each other
        - Methods get_area() and get_perimeter() that return appropriate geometric calculations
        - A method called double() that doubles the width of the box. Hint: Pay attention to return value here
        - Implement __eq__ so that two boxes can be compared using == 
        - A method print_dim that prints to screen the length and width details of the box
        - A method get_dim that returns a tuple containgthe length and width of the box
        - A method combine that takes another box as an argument and increases its length and width by the dimensions of the other box
        - A method get_hypot() that finds the length of the diagonal that cuts throught the middle
        In the function exercise01():
        - Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively 
        - Print dimension info for each using print_dim()
        - Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
        - Combine box3 into box1 (i.e. box1.combine())
        - Double the size of box2
        - Combine box2 into box1
        - Using a for loop, iterate through and print the tuple received from calling box2's get_dim()
        - Find the size of the diagonal of box2
'''

    # ------ Place code below here \/ \/ \/ ------

    #Make  box 1, 2, and 3
    box1 = Box(5,10)
    box2 = Box(3,4)
    box3 = Box(5,10)
    
    #checks if boxes are equal
    print(box1==box2)
    print(box1==box3)
    
    
    #combine box1 to box3
    box1.combine(box3)
    
    
    #double box2 and combine with box1
    box2.double()
    box1.combine(box2)
    
    
    #prints dimension of box2
    for d in box2.get_dim():
        print(d)
    
    #prints hypotenuse of box2
    print(box2.get_hypot())


    # ------ Place code above here /\ /\ /\ ------
    return box1, box2, box3

    



class TestAssignment3(unittest.TestCase):
    
    def test_exercise01(self):
        print('Testing exercise 1')
        b1, b2, b3 = exercise01()
        self.assertEqual(b1.get_length(),13)
        self.assertEqual(b1.get_width(),28)
        self.assertTrue(b1==Box(13,28))
        self.assertEqual(b2.get_length(),3)
        self.assertEqual(b2.get_width(),8)
        self.assertEqual(b3.get_length(),5)
        self.assertEqual(b2.get_hypot(),8.54400374531753)
        self.assertEqual(b1.double().get_length(),13)
        self.assertEqual(b1.double().get_width(),112)
        self.assertTrue(3 in b2.get_dim())
        self.assertTrue(8 in b2.get_dim())
        self.assertTrue(b2.combine(Box(1,1))==Box(4,9))
    
    def test_exercise02(self):
        print('Testing exercise 2')
        db = MangoDB()
        self.assertEqual(db.get_collection_size('default0'),3)
        print(db.get_collection_names())
        self.assertEqual(len(db.get_collection_names()),1)
        self.assertTrue('collection-default0' in db.get_collection_names() )
        db.add_collection('temperatures')
        self.assertTrue('collection-temperatures' in db.get_collection_names() )
        self.assertEqual(len(db.get_collection_names()),2)
        db.update_collection('temperatures',{1:50})
        db.update_collection('temperatures',{2:100})
        self.assertEqual(db.get_collection_size('temperatures'),2)
        self.assertTrue(type(db.to_json('temperatures')) is str)
        self.assertEqual(db.to_json('temperatures'),'{"1": 50, "2": 100}')
        db.wipe()
        self.assertEqual(db.get_collection_size('default0'),3)
        self.assertEqual(len(db.get_collection_names()),1)
      
    def test_exercise03(self):
        print('Exercise 3 does not have unit tests')

     

if __name__ == '__main__':
    unittest.main()