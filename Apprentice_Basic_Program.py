'''Roderic Deichler 11/07/2017

Python Apprentice from Cybrary.it

Task: Write a program with a menu that can:

Accept and store a string

Perform basic calculations

Print the previously stored string

Comparing 2 numbers to determine which is larger

Remove a chosen letter from a string
'''

#accepts and stores a string
def accept_and_store():
	
	global saved_string
	saved_string = str(raw_input("INPUT STRING: "))
	return

#basic calculator
def calculator():
	
	num1 = int(raw_input("INPUT NUM: "))
	sign = str(raw_input("OPERATION: "))
	num2 = int(raw_input("INPUT NUM2: "))
	
	if (sign == '+'):
		print num1 + num2
		
	elif (sign == '-'):
		print num1 - num2
		
	elif (sign == '*'):
		print num1 * num2
	
	elif (sign == '/'):
		print num1 / num2
		
	elif (sign == '^'):
		print num1 ** num2
		
	else:
		print "Error.. Exiting Calculator\n"
	return
	
#print stored string
def print_string():
	
	print saved_string
	return
	
#comparing numbers to see larger
def larger_num():

	num1 = int(raw_input("INPUT 1ST NUM: "))
	num2 = int(raw_input("INPUT 2ND NUM: "))
	if (num1 > num2):
		print "{} is greater than {}" .format(num1, num2)

	else:
		print "{} is greater than {}" .format(num2, num1)	
	return
	
	
#removing a chosen letter from string
def letter_remove():
	
	letter = str(raw_input("INPUT LETTER TO REMOVE: "))
	new_string = saved_string.replace(letter, "")
	print new_string
	return
	
#main function
def main():
	
	#menu items
	opt_list = [ accept_and_store,
				 calculator,
				 print_string,
				 larger_num,
				 letter_remove ]
	
	#while loop that shows program menu until input makes program crash
	#would be better and safer with defaults or exception handling, but
	#this program is just to follow along cybrary course
	while(1):
		print "SELECT AN OPTION OR ENTER ANYTHING ELSE TO EXIT:"
		print "1.\t Accept and Store"
		print "2.\t Calculator"
		print "3.\t Print String"
		print "4.\t Compare Numbers"
		print "5.\t Remove Letter"
		
		opt_choice = int(raw_input("ENTER NUMBER: "))
		opt_choice -= 1
		opt_list[opt_choice]()

		print "\n"
	return
	
#call the main function
main()



