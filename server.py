#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys

class SIPHandler(SocketServer.DatagramRequestHandler):
    """
    SIP server class
    """
    def procesar(self, line):
        linea = line.split(" ")
        metodo = linea[0]
        if metodo == "INVITE" :
            line = 'SIP/2.0 100 Trying' + '\r\n' + '\r\n'
            line += 'SIP/2.0 180 Ring' + '\r\n' + '\r\n'
            line+= 'SIP/2.0 200 OK' + '\r\n' + '\r\n'
            self.wfile.write(line)
        if metodo != "INVITE" or "ACK" or "BYE":
            line = "SIP/2.0 405 Method Not Allowed" + '\r\n' + '\r\n'
            self.wfile.write(line)
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
                # Leyendo línea a línea lo que nos envía el cliente
                line = self.rfile.read()
                print line +"------------------------------"
                if not line:
                    break
                else:
                    print "El cliente nos manda " + line
                    self.procesar(line)
                # Si no hay más líneas salimos del bucle infinito
                
            
if __name__ == "__main__":
    try:
        # Creamos servidor de eco y escuchamos
        HOST = sys.argv[1]
        PORT= int(sys.argv[2])
        AUDIO= sys.argv[3]
        serv = SocketServer.UDPServer((HOST, PORT), SIPHandler)
        print "Listening..."
        serv.serve_forever()
    except IndexError:
        print "Usage: python server.py IP port audio_file"
    except ValueError:
        print "Usage: python server.py IP port audio_file"
