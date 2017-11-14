'''   JourneyMan_ActivityOne.py

Roderic Deichler 11/13/2017

Python Journeyman from Cybrary.it

String Server

Each task is explained in a comment before the function that solves it.

'''


'''
Task: Take two arguments, a list and an integer. The list is a series of
strings. One of those strings will be the filename and the others will
be the file contents. The integer is the location in the list of the
filename.

IE:

list:

a	0	contents
b	1	contents
c	2	contents
d	3	contents
e	4	filename
f	5	contents

filename is at 4th index
'''
#import socket for 3rd task
import socket 

def journeyman_task_one(str_list, index):
	
	#filename is set to the a passed index of a list
	filename = str(str_list[index])
	
	#open the file with read and write properties
	f = open(filename, 'w+')
	
	#iterate through the list
	for i in str_list:
		
		#as long as the indices don't match we don't have
		#a filename index and we should write to it
		if i != str_list[index]:
			f.write(i)
			
	#close file
	f.close()
	return

'''
Task: Write a function which takes a single integer as an argument
and returns the sum of every integer up to and including that number
using a generator
'''

#internal function to actually sum it up 
def sum_generator(int_to_sum):
	
	#counter to hold values all the way up to the int_to_sum
	current = 0
	
	#while loop that uses yield to "return" the numbers from
	#0 all the way to int_to_sum as current is increased along
	#the way
	while(current <= int_to_sum):
		yield current
		current += 1

#note the builtin generator 'range' could have been used
#but this was better for learning purposes
def journeyman_task_two(int_to_sum):

	#sets range_sum to the sum of each value yielded by our
	#sum_generator function (all nums 0 to int_to_sum)
	range_sum = sum(sum_generator(int_to_sum))
	
	return range_sum


'''
Write a python script which connects to the included server on port 
5001 and returns the message it receives.
'''

def journeyman_task_three():
	
	#defined our socket object with ipv4 and TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#connect to the server
	s.connect(('127.0.0.1',50001))
	
	#recieve up to a maximum of 1024 bytes
	msg_recieved = s.recv(1024)
	
	#close the socket
	s.close()
	
	return msg_recieved

	
'''
Create a class called person with height, weight, hair color, and 
eye color fields, then implement it to describe a friend.
'''
def journeyman_task_four():
	
	#create the class to describe my roommate
	class Person:

		#initializer for the class Roommate (works similar to a 
		#parameterized constructor in c++)
		def __init__(self, height = 0, weight = 0, hairColor = '', eyeColor= ''):
			self.height = height
			self.weight = weight
			self.hairColor = hairColor
			self.eyeColor = eyeColor
			
	#create a roommate object 
	Roommate = Person(1.7, 60, "Brown", "Brown")
	
	#print my roommate's features
	print Roommate.height
	print Roommate.weight
	print Roommate.hairColor
	print Roommate.eyeColor
