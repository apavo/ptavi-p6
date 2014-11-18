#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente SIP simple.
def procesar_contestacion(data):
    contestacion=data.split(" ")
    if contestacion[-1] == "OK\r\n\r\n":
        line = "ACK " + 'sip:' + LOGIN + '@' + IP + 'SIP/2.0' + '\r\n'  + '\r\n'
        my_socket.send(line)
try:
    # Dirección IP del servidor.
    SERVER = 'localhost'
    METODO = sys.argv[1].upper()
    cliente = sys.argv[2].split("@")
    LOGIN = cliente[0]
    cliente = cliente[1].split(":")
    IP = cliente[0]
    PORT = int(cliente[-1])
     # Contenido que vamos a enviar
    line = METODO + ' ' + 'sip:' + LOGIN + '@' + IP + 'SIP/2.0' + '\r\n'  + '\r\n'
    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))
    
    print "Enviando: " + line
    my_socket.send(line + '\r\n')
    data = my_socket.recv(1024)
    print data
    contestacion=data.split(' ')
    procesar_contestacion(data)
    print "Terminando socket..."

    # Cerramos todo
    my_socket.close()
    print "Fin."

#except ValueError: 
 #  print "Usage: python client.py method receiver@IP:SIPport "

#except IndexError:
 #   print "Usage: python client.py method receiver@IP:SIPport "

#except NameError:
 #     print "Usage: python client.py method receiver@IP:SIPport "

except socket.error:
    print "Error: No server listening at" + " " + IP + " " + str(PORT)    
