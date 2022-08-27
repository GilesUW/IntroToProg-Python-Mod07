# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate Error Handling and Object Serialization aka the pickle module.
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#AGiles,8.24.2022,Created file, Modified code to complete assignment 07, completed required functions
# ---------------------------------------------------------------------------- #


# Import pickle and pathlib classes
import pickle
import pathlib

print('\tThe following code will demonstrate the use of Python pickling.\n'
      '\tIt will take an initialized dictionary containing the values "{1: "A", 2: "B", 3: "C"}"\n'
      '\tand serialize then store data in file.\n\tIt will then upack the data from file and print values to console. ')
input()
# Processing pickle code
print("Processing...\nPickling dictionary and storing data to file...")
example_dict_prepickle = {1: "A", 2: "B", 3: "C"}
pickle_out = open("pickleFile", "wb")
pickle.dump(example_dict_prepickle, pickle_out)
pickle_out.close()

# Getting file location and requesting user to confirm binary file
file_path = str(pathlib.Path(__file__).parent.resolve()) + "\pickleFile"
print("Confirm file is serialized by opening the following file in a text editor:\n", file_path)
input()

pickle_in = open("pickleFile", "rb")
example_dict = pickle.load(pickle_in)
print("Here is the results after unpickling file:", example_dict, "\n")


# Request input from user for error handling
print("\tNext we will display how error handling is used for a non specified error."
      "\n\tThe code will attempt to open a file.\n")
filename = input('Please input filename (Do not input "pickleFile"): ')

try:
    f = open(filename, "r")
    f.close()
    print('I told you not input "pickleFile"\n')
except:
    print("ERROR! << This is a custom message for an unspecified error")

# Code for specific error handling
print("\n\tNext we will display how error handling is used for a specified error."
      "\n\tThe code will attempt to open a file.\n")
filename = input('Please input filename (Do not input "pickleFile"): ')

try:
    f = open(filename, "r")
    f.close()
    print('I told you not input "pickleFile"\n')
except FileNotFoundError as error:
    print("The following Error Type occured...")
    print(error.__str__(), "\n")
input("End of Program")


