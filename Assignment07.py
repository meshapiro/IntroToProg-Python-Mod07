# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: An example of using pickle to load and read a binary file,
#              As well as writing detailed error messages
#              For different types of exceptions
# ChangeLog: (Who, When, What)
# MShapiro, 8/22/2022, Created script
# MShapiro, 8/25/2022, Added pickling section to script
# MShapiro, 8/26/2022, Added comments and formatting
# ------------------------------------------------------------------------ #


# Data --------------------------------------------#
strFileName_text = 'NewFile.txt'
fltV1 = None  # first argument
fltV2 = None  # second argument
fltQuot = None


# -- processing code -- #

import pickle #imports a package for pickling

# Function for creating pickled data and writing to a file
def storePickleData():
    # initializing data to be stored in db
    Meredith = {'id': 1, 'name': 'Meredith Shapiro','age': 36, 'sex': 'F'}
    Jeremy = {'id': 2 , 'name': 'Jeremy Shapiro', 'age': 42, 'sex': 'M'}
    Edie = {'id': 3, 'name': 'Edie Shapiro', 'age': 8, 'sex': 'F'}
    Calvin = {'id': 4, 'name': 'Calvin Shapiro', 'age': 5, 'sex': 'M'}

    # database
    household = {}
    household['M'] = Meredith
    household['J'] = Jeremy
    household['E'] = Edie
    household['C'] = Calvin

    # Its important to use binary mode
    dbfile = open('examplePickle', 'wb')

    # source, destination
    pickle.dump(household, dbfile)
    dbfile.close()

# Function for
def loadPickleData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()


def twoVals(fltV1, fltV2):
    fltQuot = fltV1/fltV2
    return fltV1, fltV2, fltQuot #pack tuple

def displayVals(fltV1, fltV2, fltQuot):
    output = str("The Quotient of " + str(fltV1) + " and " + str(fltV2) + " is " + str(fltQuot) + "\n")
    return output

def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "a")
    pickle.dump(list_of_data, objFile)
    objFile.close()

def read_data_from_file(file_name):
    objFile = open(file_name, "r")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data


# ------- Try/Except for catching errors --------------------------#

try:
    fltV1 = float(input("Enter value 1: "))
    fltV2 = float(input("Enter value 2: "))

    twoVals(fltV1, fltV2)
    fltV1, fltV2, fltQuot = twoVals(fltV1, fltV2)  # unpack tuple

    output = displayVals(fltV1, fltV2, fltQuot)
    print(output)

    objFile = open(strFileName_text, "a")
    objFile.write(output)
    objFile.close()

    print()
    print("Printing Pickle Data: ")
    storePickleData()
    loadPickleData()

# ----- Error handling code --------------------------------#

except ZeroDivisionError as e:
    print("Please do no use Zero for the second number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except UnicodeDecodeError as e:
    print("You need to use binary read mode to decode a binary file!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except FileNotFoundError as e:
    print("Text file must exist before running this script!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except ValueError as e:
    print("Input data must be numeric!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except pickle.UnpicklingError as e:
    print("Something has gone wrong with your unpickling!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except TypeError as e:
    print("The action you are trying to perform doesn't work on object with this data type!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
