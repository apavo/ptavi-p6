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

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    try:
        # Creamos servidor de eco y escuchamos
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
        AUDIO= sys.argv[3]
        serv = SocketServer.UDPServer(("", 6001), SIPHandler)
        print "Lanzando servidor SIP..."
        serv.serve_forever()
    except IndexError:
        print "Usage: python server.py IP port audio_file"
    except ValueError:
        print "Usage: python server.py IP port audio_file"
