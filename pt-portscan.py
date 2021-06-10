#!/usr/bin/python3.8
import socket
def scan():
    ip = input("Type the target IP") 
	for ports in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # noqa: E731,E123
		
			if s.connect_ex((ip,ports)) == 0:

				print ("PORTA", ports, "ABERTA")


				
				s.close()
	print("scanneamento concluido")

scan()
