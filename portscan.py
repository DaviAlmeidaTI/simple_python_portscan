#!/usr/bin/python


import socket

ip = raw_input("Digite o ip do alvo\n")

for ports in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		if s.connect_ex((ip,ports)) == 0:

			print "PORTA", ports, "ABERTA"

			s.close()
