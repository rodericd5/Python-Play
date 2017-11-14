''' Roderic Deichler 
	11/13/2017
	Cybrary.it Journeyman Activities
	
'''
import socket


#basic server for testing purposes on part 3
def main():
	
	#generic host same as 0.0.0.0
	HOST = ''
	
	#port set to 50001 as per assignment
	PORT = 50001
	
	#list of messages to recieve
	server_msg_list = ['string', 'string2', 'string3']
	
	#create socket object with either ipv4 or 
	#internet domain notation with tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	#bind socket to all available interfaces and port 50001
	s.bind((HOST, PORT))
		
	#iterate through the server messages
	for i in server_msg_list:
		
		#listen for the message
		s.listen(1)
	
		#accept connection
		conn, addr = s.accept()
		
		#send message at index i
		s.send(i)
		
		#close the connection
		conn.close()
	
main()


