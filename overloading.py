#===================================================================
#    Purpose:   Practice in using simple overloading
#===================================================================

# Class to demonstrate overloading the + operator for integers
class MyIntClass:

    def __init__(self, num = 0):

        self.num = num

    def __add__(self,other):

        return self.num + other.num


myIntClass1 = MyIntClass(5)
myIntClass2 = MyIntClass(4)

print(myIntClass1 + myIntClass2)

# Class to demonstrate overloading the + operator for lists
class MyListClass:

    def __init__(self, longNumber = ""):

        self.longNumber = longNumber

    def __add__(self,other):

        for value in other:
            self.longNumber += str(value)

        return self.longNumber

myListClass = MyListClass("23")
numberlist = [5, 3, 6, 4]

print(myListClass + numberlist)

# Class to demonstrate overloading the + operator for string
class MyStrClass:

    def __init__(self, strVal = ""):

        self.strVal = strVal

    def __add__(self,other):

        return self.strVal + other.strVal

myStrClass1 = MyStrClass("Hello")
myStrClass2 = MyStrClass(" World")

print(myStrClass1 + myStrClass2)

# Class to demonstrate overloading the + operator for string with a formatted return
class MyFormattedClass:

    def __init__(self, strVal = ""):

        self.strVal = strVal

    def __add__(self,other):

        return "%s plus %s" % (self.strVal, other.strVal)

myFormattedClass1 = MyFormattedClass("Hello")
myFormattedClass2 = MyFormattedClass("World")

print(myFormattedClass1 + myFormattedClass2)
