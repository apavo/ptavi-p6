#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.
try:
    # Dirección IP del servidor.
    SERVER = 'localhost'
    METODO = sys.argv[1]
    cliente = sys.argv[2].split("@")
    LOGIN = cliente[0]
    cliente = cliente[1].split(":")
    IP = cliente[0]
    PORT = int(cliente[-1])


    # Contenido que vamos a enviar
    LINE = '¡Hola mundo!'

    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print "Enviando: " + LINE
    my_socket.send(LINE + '\r\n')
    data = my_socket.recv(1024)

    print 'Recibido -- ', data
    print "Terminando socket..."

    # Cerramos todo
    my_socket.close()
    print "Fin."

except ValueError: 
   print "Usage: python client.py method receiver@IP:SIPport "

except IndexError:
    print "Usage: python client.py method receiver@IP:SIPport "

except socket.error:
    print "Error: No server listening at" + " " + IP + " " + str(PORT)
    
