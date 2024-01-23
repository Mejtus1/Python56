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

############################
# Python Conditionals
# - conditional statements are used to perform different actions depending on whether condition evaluates as true or false

# Conditional Statements
# if, elif, else

# Comparison Operators
# ==, !=, <, >, <=, >=

# Boolean Operators
# and, or, not

# Membership Operators
# in, not in 

# Identity Operators 
# is, is not

# - to easily evaluate statement, you can use different built-in operators like comparison ( == )
# - this operator compares value on left side to value on right side and determines if they are equal (True) or not equal (False)
# - list of operators that can be used during different evaluations:

# Comparison operators:
# ==  : This operator compares whether values on the left and right side are equal.
# !=  : This operator compares whether values on the left and right side are not equal.
# <   : This operator compares whether the value on the left is less than the value on the right.
# >   : This operator compares whether the value on the left is greater than the value on the right.
# <=  : This operator compares whether the value on the left is less than or equal to the value on the right
# >=  : This operator compares whether the value on the left is greater than or equal to the value on the right.

# Boolean operators:
# and: This operator requires that both statements are true.
# or:  This operator allows either of the statements to be true.
# not: This operator returns the value that is the opposite of the original statement (true for false; false for true).

# Membership operators:
# : This operator checks whether the value on the left exists in the value on the right.
# not in: This operator checks whether the value on the left does not exist in the value on the right.

# Identity operators:
# is: This operator compares whether the value that is assigned to the variable on the left is the same as the   value that is assigned to the variable to the right
# is not: This operator compares whether the value that is assigned to the variable on the left is not the same as the value that is assigned to the variable to the right.  

# Now you can apply operators to conditional statements
# There are three conditional statements in Python: 
# if, elif, else
# The if condition starts the statement evaluation process
# - if statement is true, then action is executed and code block is exited
# - if statement is false, then optional elif conditional check can be used to evaluate another statement for being true or false
# - If all conditional statements evaluate to false, then else clause can be used to execute line of code 

# - conditional checks can be nested:
if hostname == "csr1kv-1":
  if os_version == "16.09.03":
    print("Device {hostname} is running version {os_version}".format(hostname=hostname, os_version=os_version))
  else:
    print("Device {hostname} is running unknown version of os".format(hostname=hostname))

#################################################################
# Python Loops and Functions
# Manually obtaining value from nested dictionary or list is not very practical. 
    # - in addition, it is not very practical to have repetitive code that checks if value has changed
    # - to address those types of scenarios, you will need to use proper tools within Python
    # - to address first problem, you will use for loop and to address second one, you will use while loop
    # - explanation of each loop type and supporting examples are as follows:

###########
# For Loops
# - unlike other programming languages, Python "for" loop does not evaluate statement before running underlying code; 
# - instead, it iterates over a provided object
# - Python "for" loop is like “for each” loop in other languages

The given object being “looped over” or “iterated over” can be a primitive string, range, or nonprimitive 
(list, dictionary, tuple, or a set) data type. 
he syntax of a for loop is as follows: for variable_name in object_of_iteration: 

# variable_name: This temporary variable holds data that are relevant to that iteration cycle. A good general principle is to give the temporary variable a name that describes the data it will hold. For example, if you are iterating over VLANs, then name the variable “vlan,” for example, for vlan in vlans: A more generic name that is often used is “item,” for example, for item in vlans:.
# in: This variable is membership operator
# object_of_iteration: This variable name is being looped (iterated) through

# Example:
vlans = [100, 200, 300]
for vlan in vlans:
print(vlan)
# 100
# 200
# 300  

#############
# While Loops
# - “While” is another looping method that Python supports, but instead of iterating over object, while loop executes underlying code until supplied condition is true
# - this mechanism is very useful, but it requires attention
# - underlying code is running while condition is true, it is possible to enter infinite-looping state during which code runs forever and can negatively affect host on which code is running
interface_id =1
  while interface_id <=4:
    print('Ethernet1/{}'.format(interface_id))
    interface_id += 1
# Ethernet1/1
# Ethernet1/2
# Ethernet1/3
# Ethernet1/4

##################
# Python Functions 
# - all programming languages, including Python, can create blocks of organized and reusable code that are called functions 
# - functions provide efficiency, consistency, and modularity
# - functions can be built-in, written in code, or can be imported from other Python scripts

# create reusable code
# - wrap standard Python code within function definition  
def issue_command(hostname, command):
  print("Connecting to device: {}".format(hostname))
  print("Issuing the following command: {}".format(command))

issue_command('nycr1', 'show version')
 # Connecting to device: nycr1
 # Issuing the following command: show version


# Functions might require arguments to be provided when called and optionally return data for further processing 
# - functions and how to use them:

# User-defined function:
def hostname_conf(name):
    return 'hostname {}'.format(name)
print(hostname_conf('csr1kv-1'))
# hostname csr1kv-1

# Built-in functions:
len(vlans)
# 1
str(100)
# '100'
int(3.14)
# 3

#################################################################
# Network libraries and packages 

# Network Libraries
# - software library is collection of prewritten code to assist developers during their software creation process 
# - breakdown of available prewritten code:
# Python libraries
# In-house Libraries
# Free or Open source Libraries

# - module is single file that contains Python objects that can be reused in scripts

# - package is collection of modules, in one or more directories, to streamline and modularize development of package

# - “library” is often used to refer to collection of modules or packages. 
# - often standard modules that come with install of Python are referred to as “Python standard library”
# - libraries can come from different sources. 
# - in Python, people who are responsible for Python itself develop and maintain libraries
# - Again, this library is standard library

# - python is not limited to standard library
# - developers can download libraries from open source and public communities that are often found on GitHub or Python Package Index (PyPI)

# - last type of library is one that is developed in a company for a specific purpose
# - these libraries are customized, in-house libraries
# - large clients may have in-house libraries and code to provision different pods for requesting users
# - this code is customized, not public, and is usually specific to use case

# Modules and Packages 
# - difference between Python module and Python package was mentioned earlier
# - module is single file with .py extension that contains some usable code
# - package is collection of modules that is stored in folder where name of folder is name of package

# - you might be wondering how you can differentiate package from module in Python code itself
# - you can make this distinction when module is imported and single file is referenced
# - import Netmiko or from Netmiko, import ConnectHandler 
# - if you want to import module from package, then you must use “dotted module names” 
# you could use:

# import cobra.mit.access
#  or
# from cobra.mit.access import MoDirectory 

# - where each name that is followed by a dot represents folder and last entry in chain represents file (module)

################
# Use PYTHONPATH
# - by default, you can be in any directory to use Python standard library 
# - you may write a script, script must be stored in one of two locations: 
# - local directory where script is saved or within PYTHONPATH environment variable
# - PYTHONPATH is list of directories that system will search for Python modules and packages when doingimports in script
# - it is quite common to update PYTHONPATH in login script such as .profile

# - you can check PYTHONPATH on Linux shell using env command to see any custom paths that have been added
# - to see all available directories that Python will search, you can easily check from Python shell using sys.path command:

# >>> import sys
# >>> print(sys.path)
# ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/student/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']

###################
# Import Statements
# - import statements help you perform many tasks
# - following provides description of different import methods and what they do:
import netmiko: # method imports everything in Netmiko module. 

# Suppose that Netmiko has a variable called VERSION that is defined in its file. 
# - to use that variable, you will need to use following format to refer to it: 
netmiko.VERSION. 
# - same requirement applies to classes and functions
# ConnectHandler is part of Netmiko module and you can use it by following same syntax: 
netmiko.ConnectHandler().

# from netmiko import ConnectHandler: 
# - this method tells python to extract object (in this instance, object is ConnectHandler) from  module and make it directly callable
# - directly callable means that you do not need to refer to module name and object
# - instead, you can use class name directly, same approach applies to functions and variables

# from netmiko import ConnectHandler as ch: 
# - some objects have really long names, and to make them shorter, you can create aliases of original object

###########################
# Free Open Source Software 
# Python software is available in many places. 
# - there is growing community of network developers who host their code on GitHub including Cisco DevNet, 
# - it has several free and open source projects on DevNet Code Exchange, curated collection of example code and projects
# - you can find several Cisco libraries on CiscoDevNet GitHub page: https://github.com/CiscoDevNet

# - two Python packages that are open source and quite popular in network industry are Netmiko and Network Automation and Programmability Abstraction Layer with Multivendor (NAPALM):
# Netmiko: 
# - this package is multivendor SSH library for Python to simplify Paramiko SSH connections to network devices: 
# https://github.com/ktbyers/netmiko

# NAPALM: 
# - this package implements set of functions that interact with different network device operating systems using unified API: 
# https://github.com/napalm-automation/napalm

#######################
# Inside Python Modules

# - python module is simply Python file that has one or more Python objects, such as variables, functions, and classes
# - keep in mind that modules can use other modules
# - this process is possible using import statements just like you would do if you were writing script (not a module)

# examples of Python modules:
# - device_data.py
USERNAME = "cisco"
PASSWORD = "cisco"
DEVICE_TYPE = "cisco_xe"
INVENTORY = ["csr1kv1", "csr1kv2", "csr1kv3"]

# This module only has variables. 
# - Other Python scripts and other Python modules can use these variables. 
# - example of script that uses device_data.py module:
# automation_code.py 
import device_data
print(device_data.USERNAME)
print(device_data.INVENTORY)

# - there are many ways to import data within script from module
import device_data as dd
print(dd.USERNAME)

from device_data import USERNAME
print(USERNAME)

from device_data import USERNAME as user
print(user)

from device_data import PASSWORD
print(PASSWORD) 

# - python classes and functions can also be saved in module file and can be referenced in any other Python code

# cisco_networks.py
def print_routers():
def verify_bgp(device):
def configure_bgp():

# Constructing Module
# - it is quite straightforward to create Python module once you know Python fundamentals
# - example will use the Python interpreter. 
# - devnet.py file is custom module for this class that resides 
# - in /home/student/modules folder

# student@student-vm:~$ cat modules/devnet.py
 inventory = {
    "csr1kv1": { 
        "username": "cisco", 
        "password": "cisco", 
        "device_type": "cisco_ios", 
    }, 
    "csr1kv2": { 
        "username": "cisco", 
        "password": "cisco", 
        "device_type": "cisco_ios", 
    }, 
 }

 def print_routers():
    for router in inventory: 
        print(router) 

 def verify_bgp():
    print("BGP session is active") 

 def configure_bgp():
    for router in inventory: 
        print("Configuring BGP for {} ".format(router))

# - Python interpreter is opened by typing python command
# - present working directory is /home/student

# student@student-vm:~$ python
# Python 3.6.8 (default, Jan 14 2019, 11:02:34)
# [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
# Type "help", "copyright", "credits" or "license" for more information. 

# - if you attempt to import module immediately, it will fail
import devnet
Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
# ModuleNotFoundError: No module named 'devnet'

# - four options to resolve problem: 

# - change your present working directory to modules folder, then start interpreter (this option is easiest)
# - create special file in modules folder named __init__.py (completely empty), which will make your folder package
# - add modules folder to your PYTHONPATH environmental variable
# - copy devnet.py module to folder that exists in PYTHONPATH
# here are options in operation:

# Option 1: Change the working directory.
quit()
# student@student-vm:~$ cd modules
# student@student-vm:~/modules$ python
# Python 3.6.8 (default, Jan 14 2019, 11:02:34)
# [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
# Type "help", "copyright", "credits" or "license" for more information.
import devnet
print(devnet.inventory)
# {'csr1kv1': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}, 'csr1kv2': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}}

# option 2:
# - create  __init__.py file in modules folder:
quit()
# student@student-vm:~$ touch modules/__init__.py
# student@student-vm:~$ python
# Python 3.6.8 (default, Jan 14 2019, 11:02:34)
# [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
# Type "help", "copyright", "credits" or "license" for more information.
import modules.devnet
print(modules.devnet.inventory)
# {'csr1kv1': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}, 'csr1kv2': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}}

# Option 3: 
# - add modules folder to PYTHONPATH environmental variable
import sys
sys.path.insert(1, '/home/student/modules/') #sys.path is a list and we can invoke any methods a list supports
import devnet
print(devnet.inventory)
# {'csr1kv1': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}, 'csr1kv2': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}}
# - update .bashrc in home directory to add to the PYTHONPATH if you need the PYTHONPATH to have a new directory search for all apps. 

# Option 4. 
# - copy your module to folder that exists in PYTHONPATH environmental variable (Superuser permission is required.  
import sys
sys.path
# ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/student/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']
quit()
# student@student-vm:~$ sudo cp modules/devnet.py /usr/lib/python3/dist-packages/
# student@student-vm:~$ python
# Python 3.6.8 (default, Jan 14 2019, 11:02:34)
# [GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
# Type "help", "copyright", "credits" or "license" for more information.
import devnet
print(devnet.inventory)
# {'csr1kv1': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}, 'csr1kv2': {'username': 'cisco', 'password': 'cisco', 'device_type': 'cisco_ios'}}

########################################################
# Netmiko
# - popular method for communicating with network devices = "SSH client like PuTTY, SecureCRT, or Linux terminal with SSH client" 
# - with shift to network automation, there needs to be way to “use SSH from Python” 

# - netmiko is Python-based SSH client
# - rather than connecting to each device separately from GUI client and issuing desired commands one by one, whole process can be automated with Python and commands can be applied to all devices at once if necessary. 
# - Netmiko is actually wrapper for Paramiko (de facto SSH library in Python) with some added network intelligence for sending commands, log in to devices, and so on, which is why Netmiko is becoming de facto SSH client for networking devices
# - netmiko supports more than 20 different vendors, most notably Cisco, with Cisco IOS, Cisco IOS XE, and Cisco Nexus Operating System (NX-OS), and others
# - in following design activity, you will examine Netmiko use case with Cisco Cloud Services Routers:

# Challenge: You have 10 Cisco CSR routers that need following:
# - configured hostnames
# - SSH as only permitted terminal connection method
# - configured loopback interface with proper IP address  

# Assumption:
# - inventory dictionary containing all necessary information exists
# - template for each configuration type exists

# Solution:
# - generate configuration file using templates and information from inventory dictionary
# - connect to each device using Netmiko
# - push configuration file
# - verify that configuration was successfully applied
# - disconnect from device

# Common Netmiko Methods
# - netmiko has many functions (methods) that developers can use while interacting with device
# - because it is very long list, most useful ones are discussed here with detailed descriptionand applicable use cases 
# - to learn about all supported methods, refer to official Netmiko documentation

# ConnectHandler(): 
# - Python class initiates connection with device
# - you will need to provide IP address, username, password, and device type information to successfully initiate connection  
# Example: 
device = ConnectHandler(host="csr1kv1", username="cisco", password="cisco", device_type="cisco_xe")

# is_alive(): 
# - this method determines if connection with device is alive and returns True or False 
# Example: 
device.is_alive()
# True

# establish_connection(): 
# - In cases when device is disconnected manually or automatically due to connection timeout (default 60 seconds), this method can be used to reinitiate connection
# Example: 
device.is_alive()
# False
device.establish_connection()
device.is_alive()
# True

disconnect(): 
# - This method is used to manually disconnect session
# Example:
device.is_alive()
# True
device.disconnect()
device.is_alive()
# False

# send_command(<VALID_COMMAND>): 
# - Use this method to send operational show command to device 
# - it must be single string that contains valid command
# Example:
device.send_command("show version")
# 'Cisco IOS XE Software, Version 16.09.03\nCisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.3, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2019 by Cisco Systems, Inc.\nCompiled Wed 20-Mar-19 07:56 by mcpre\n\n\nCisco IOS-XE software, Copyright (c) 2005-2019 by cisco Systems, Inc.\nAll rights reserved.  Certain components of Cisco IOS-XE software are\nlicensed under the GNU General Public License ("GPL")
# <... output omitted ...>

# send_config_from_file(<PATH_TO_THE_FILE>): 
# - this method can be used to apply configuration file to device 
# - in argument, you must supply full path to configuration file
# Example:
# % cat interface_conf.cfg
# interface GigabitEthernet1
# description SALES 
device.send_config_file("/home/student/config_files/interface_conf.cfg")
 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\ncsr1kv1(config)#interface GigabitEthernet1\ncsr1kv1(config-if)#  description SALES\ncsr1kv1(config-if)#end\ncsr1kv1#'

# send_config_set([<COMMAND_1>, <COMMAND_2>]): 
# - this method can be used to send list of configuration commands to device
# - list must contain commands as string and must be in proper order
# Example:
print(interface_config)
# ['interface GigabitEthernet1', 'description HR']
device. send_config_set(interface_config)
# 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\ncsr1kv1(config)#interface GigabitEthernet1\ncsr1kv1(config-if)#description HR\ncsr1kv1(config-if)#end\ncsr1kv1#'

# open_session_log(<FILE_NAME>): 
# - use this method to log your session to file for debugging purposes
# Example:
device.open_session_log("/home/student/logs/CSR.log")
# % cat CSR.log
# csr1kv1#show version
# Cisco IOS XE Software, Version 16.09.03
# Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.3, RELEASE SOFTWARE (fc2)
# Technical Support: http://www.cisco.com/techsupport
# Copyright (c) 1986-2019 by Cisco Systems, Inc.
# Compiled Wed 20-Mar-19 07:56 by mcpre
# Cisco IOS-XE software, Copyright (c) 2005-2019 by cisco Systems, Inc.
# All rights reserved.  Certain components of Cisco IOS-XE software are
# licensed under the GNU General Public License ("GPL") Version 2.0.  The
# software code licensed under GPL Version 2.0 is free software that comes
# with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
# GPL code under the terms of GPL Version 2.0.  For more details, see the
# documentation or "License Notice" file accompanying the IOS-XE software,
# or the applicable URL provided on the flyer accompanying the IOS-XE
# software.
# <... output omitted ...>

# session_timeout: 
# - this variable defines number of seconds after which session should time out. 
# - it can be defined with ConnectHandler as extra argument, or can be changed after connection is initiated 
# - default value is 60 seconds
# Example:
device = ConnectHandler(host="csr1kv1", username="cisco", password="cisco", device_type="cisco_xe", session_timeout=120)
device.session_timeout
# 120
device.session_timeout = 180
device.session_timeout
# 180

      
