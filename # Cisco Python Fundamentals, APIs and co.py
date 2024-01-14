# Cisco Python Fundamentals, APIs and configurations for devices 
# - network automation involves manipulation of data. 
# - we can organize or structure this data in different ways using data types 
# - two categories of data types in Python: primitive and non-primitive
# Primitive: Integer, Float, String, Boolean (store single value)
# Nonprimitive: List, Tuple, Dictionary, Set (store primitives)
# - nonprimitive data types quality is nesting 
# Nested List [[],[],[]]
# Nested Dictionary [{},{}]
# - nesting applies to all 4 non primitive data types 
# Network automation often poses challenge of large datasets
# - loop is useful in this scenario, iterates over elements
# while loop = repeats code while conditional statement is True
# for loop = iterates over individual items (does not evaulate a statement before running underlying code)

###################
# Python Data Types
# - like any programming language, Python supports different data types 
# - each supported type can be divided into two categories: 
# primitive and nonprimitive
# - primitive data types are represented in their basic form
# - nonprimitive data types are intended to organize and manage primitive data types

######################
# Primitive Data Types

# Integer: 
# - any whole number is integer
ssh_timeout = 30
error_code= -1

# Float: 
# - this data type is floating point number, and any number with decimal point is considered as float
ios_version = 15.8

# String: 
# - any alphanumeric characters that are enclosed within pair of single or double quotation marks is string
leaf_switch  = "Nexus 9300"
spine_switch = "Nexus 9336PQ"

# Boolean: 
# This data type can accept only two values: 
# True or False
code_upgraded = True
errors_observed = False

#########################
# Nonprimitive Data Types
# List: 
# - any data that is enclosed within square brackets ( [] ) and separated by comma is considered list
devices = ["ASA", "NEXUS", "CATALYST", "ASR"]

# Tuple: 
# - any data that is enclosed within parenthesis ( ( ) ) and separated by comma is considered tuple
# - tuples are immutable, data that is stored in tuple cannot be modified at run time 
# - following is tuple of IP addresses
ip_addr = ("10.254.0.1", "10.254.0.2", "10.254.0.3")
ip_addr[1]
# '10.254.0.2'
ip_addr[1] = "10.254.1.2"
# Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
# TypeError: 'tuple' object does not support item assignment

# Dictionary: 
# - any key-value pairs that are enclosed in curly brackets ( {  } ) and separated by comma is dictionary 
# - following dictionary has keys that are equal to interface names and values with desired state of interface 
if_state = {"Gi0/1":"shutdown", "Gi0/2":"no shutdown"}

# Set: 
# - collection of unique objects that is enclosed curly  brackets ( {  } ) and separated by comma is considered set
if_names = {"Gi0/1", "Gi0/2", "Gi0/3", "Gi0/1"}
if_names
# {'Gi0/1', 'Gi0/2', 'Gi0/3'}

################################################################
# Primitive data types can be converted to other primitive types 
# - using built-in functions with assumption that converted value is valid
bool(1)
# True
int(False)
# 0
float("3.14")
# 3.14

# - some nonprimitive data types can also be converted to other (similar) data types
# -list can be converted to set or tuple, but cannot be converted to dictionary 
devices= ["ASA", "NEXUS", "CATALYST", "NEXUS", "asa"]
set(devices)
{'NEXUS', 'ASA', 'asa', 'CATALYST'}
# - as shown in output, devices list contains duplicate entry of "NEXUS", but when converted to set data type, it was removed
# - note that set removes items based on case sensitivity
# - from previous output, you can see that 'ASA' and 'asa' are still present in set because they are different values.

# - it is possible to convert list to tuple, but variable that holds converted tuple can no longer be modified 
cisco_devices = tuple(devices)
# ('ASA', 'NEXUS', 'CATALYST')
cisco_devices
# ('ASA', 'NEXUS', 'CATALYST', 'NEXUS', 'asa')
cisco_devices[-1] = "FTD"
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module> 
# TypeError: 'tuple' object does not support item assignment

# - as mentioned earlier, it is not possible to convert one data type to another if converted value is invalid
# - if you attempt to convert list to dictionary, error will be raised
dict(devices)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module> 
# ValueError: dictionary update sequence element #0 has length 3; 2 is required

# - each data type that was mentioned previously supports different built-in methods and attributes
# - to list methods that can be used on particular data type, create variable with thattype and then issue dir() built-in method
vendor = "Cisco"
dir(vendor)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', 
 '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
 '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# - if you want to convert string to all capital letters, then you need to use upper() method
vendor.upper()
# CISCO

# - to learn how to use each method, you can use help() function
help(vendor.upper)
# Help on built-in function upper:
# 
# upper() method of builtins.str instance
#    Return a copy of the string converted to uppercase.


##################################################################
# Nested data structures are only applicable to nonprimitive types 
# - each nonprimitive type can contain same or other nonprimitive data types as nested entries

# - nested list can contain dictionary as nested item:
if_state = ["Gi0/1", [{"state": "shutdown"}]]

# - to access the value inside nested list without looping through list, you first need to identify its position in list 
# - because lists are ordered, and positions, starting from 0, are incremented from left to right by 1, position for nested dictionary will be 1

# Now, to refer to position, you need to put integer within square brackets: 
if_state[1]
# [{"state": "shutdown"}]

# - however, that will give [{"state": "shutdown"}] item, because it is also list, and has only one value that can be referenced with its positional number:
if_state[1][0]
# {"state": "shutdown"}

# - at this point, what remains is dictionary. 
# - you can print value of key by appending name of key to variable that precedes position in list: 
if_state[1][0]["state"]
# shutdown

# - now, consider nested dictionary
# - as you know, dictionaries are not sorted, so position of key cannot be referenced. 
# - it can be referenced directly by specifying its name and enclosing it in square brackets. 
facts ={"csr1kv1": {"os":"ios-xe", "version":"16.09.03"}, "if_state": [{"name": "Gi0/1", "state":"shutdown"}]}

# - you can obtain nested values that are stored under each root key. 
# - in this example, start with csr1kv1
# - to return value stored in key, you enclose key’s name in square brackets and append it to variable
facts["csr1kv1"]
# {"os":"ios-xe", "version":"16.09.03"}

# - returned value is another dictionary
# - to return value of nested key, you need to add its name after name of root key
facts["csr1kv1"]["os"]
# ios-xe
facts["csr1kv1"]["version"]
# 16.09.03

# - now consider second root key
# - as you can see, value is list, so you need to act accordingly 
# - you need to obtain value, pick position within list, and then use key name to return value
facts["if_state"]
# [{"name”: "Gi0/1", "state":"shutdown"}]
facts["if_state"][0]
# {"name": "Gi0/1", "state":"shutdown"} 
facts["if_state"][0]["name"]
# Gi0/1
