#!/usr/bin/python3.8
import socket

print(""" __   __  ___  ___      ___                 __   __   __  ___  __   __            
|__) /  \  |  |__  |\ |  |  |  /\  |       |__) /  \ |__)  |  /__` /  `  /\  |\ | 
|    \__/  |  |___ | \|  |  | /~~\ |___    |    \__/ |  \  |  .__/ \__, /~~\ | \| 
                                      
									                                              """)


def scan():
	ip = input("Digite o ip do alvo\n")

	for ports in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
			if s.connect_ex((ip,ports)) == 0:

				print ("PORTA", ports, "ABERTA")


				
				s.close()
	print("scanneamento concluido")

scan()
