'''   JourneyMan_ActivityOne_Tester.py

Roderic Deichler 11/13/2017

Python Journeyman from Cybrary.it

String Server


'''

# import all of the methods from JourneyMan_ActivityOne, os & socket
from JourneyMan_ActivityOne import *
import os
import socket


# method to test that the first task is properly solved
def journeyman_task_one_test():
	# a list of lists to test
	test_list =	[
				['a', 'f', 'b', 'c', 'd', 'e'],
				['I', 'have', 'testing', 'strong', 'python', 'skills'],
				['1', '2', '3', '4', '5']
				]
				
	#this integer list will decide the filename for each list			
	int_list = [1, 2, 4]
	
	# for loop to iterate the length of the test_list
	for i in range(len(test_list)):
		
		#initialize a list to fill with each list within test_list
		check_list = []
		
		#iterate through the individual lists and append values
		for val in test_list[i]:
			check_list.append(val)
			
		#pass the first iteration of test_list and int_list into method
		journeyman_task_one(test_list[i], int_list[i])
		
		#filename should be stored in the first list in test_list
		#at the index of the first member of the int_list
		f = open(test_list[i][int_list[i]])
		
		#remove the value stored there, because it merely holds the
		#filename and its data is unimportant
		check_list.remove(check_list[int_list[i]])
		
		#iterate through the check_list
		for j in range(len(check_list)):
			
			#read the contents at each index
			line = f.read(len(check_list[j]))
			
			#in case of failure
			if line != check_list[j]:
				print "Failed. The lists do not match"
				return -1
		
			#print out the line just to see in terminal
			print line	
		
		#go to next line to show it is the next list
		print "\n"
			
		#close file and free memory allocation
		f.close()
		os.remove(test_list[i][int_list[i]])
	
		
	#it must have worked :)
	print "The 1st task was SUCCESFUL\n\n"
	return 0
			
	
# method to test that the second task is properly solved
def journeyman_task_two_test():
	
	#list of integers to sum
	sum_list = [5, 25, 9, 400]
	
	#iterate through list to test function
	for i in sum_list:
		
		#ensure the function is adding properly
		if journeyman_task_two(i) != sum(range(i+1)):
			print "Failed. The sums were miscalculated"
			return -1
			
		#print sums so user can see results
		print "%d has a number sum of: %d" %(i, journeyman_task_two(i))
		
	#it must have worked :)
	print "The 2nd task was SUCCESSFUL\n\n"
	return 0
	
# method to test that the third task is properly solved
def journeyman_task_three_test():
	
	#list identical to the possible server messages
	server_msg_list = ['string', 'string2', 'string3']
	
	#iterate through the list
	for i in server_msg_list:
		
		#set the received string to what our function returns
		Str_recv = journeyman_task_three()
		
		print Str_recv
		print "\n"
		
		#if any of the messages do not line up there was a mistake	
		if Str_recv != i:
			print "Failed: Improper message received"
			return -1
		
	#it must have worked :)	
	print "The 3rd task was SUCCESSFUL \n\n"
	return 0

# method to test that the fourth task is properly solved
def journeyman_task_four_test():
	
	#Let's just see what gets printed..
	journeyman_task_four()
	
def main():
	journeyman_task_one_test()
	journeyman_task_two_test()
	journeyman_task_three_test()
	journeyman_task_four_test()
main()
