#!/usr/bin/python3

import nmap
import sys
import os
import socket
import json
import urllib.request
import netifaces

def opcion_1():
    ip_privada = None
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        if iface != "lo" and netifaces.AF_INET in netifaces.ifaddresses(iface):
            ip_privada = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    if ip_privada:
        print(f"La dirección IP privada de tu máquina es: {ip_privada}")
    else:
        print("No se pudo obtener la dirección IP privada.")
    input("\nPresiona Enter para salir...")

def opcion_2():
    ip= input("[+]Introduzca la ip objetivo: ")
    nm= nmap.PortScanner()
    puertos_abiertos="-p"
    count=0
    results= nm.scan(ip, arguments="-sT -n -Pn -T4 ")
    #print(results)
    print("----------------------------------------------------")
    print("\n\033[33mIP : %s\033[0m" % ip)
    print("State : %s" % nm[ip].state())
    for proto in nm[ip].all_protocols():
     print("----------")
     print("Protocol : %s" % proto)
     lport = nm[ip][proto].keys()
     sorted(lport)
     for port in lport:
         print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
         if count==0:
            puertos_abiertos= puertos_abiertos+" "+str(port)
            count=1
         else:
            puertos_abiertos= puertos_abiertos+","+str(port)

    print("\nPuertos abiertos: "+puertos_abiertos+","+str(port))
    input("\nPresiona Enter para salir...")

def opcion_3():
    print("IP objetivo: 192.168.1.1")
    ip= "192.168.1.1"
    nm= nmap.PortScanner()
    puertos_abiertos="-p"
    count=0
    results= nm.scan(ip, arguments="-sT -n -Pn -T4 ")
    #print(results)
    print("----------------------------------------------------")
    print("\n\033[33mIP : %s\033[0m" % ip)
    print("State : %s" % nm[ip].state())
    for proto in nm[ip].all_protocols():
     print("----------")
     print("Protocol : %s" % proto)
     lport = nm[ip][proto].keys()
     sorted(lport)
     for port in lport:
         print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
         if count==0:
            puertos_abiertos= puertos_abiertos+" "+str(port)
            count=1
         else:
            puertos_abiertos= puertos_abiertos+","+str(port)

    print("\nPuertos abiertos: "+puertos_abiertos+","+str(port))
    input("\nPresiona Enter para salir...")

def opcion_4():
    default_subnet = "192.168.1.0/24"
    subnet = input("[+] Introduzca la subred (por defecto, 192.168.1.0/24): ") or default_subnet

    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments='-T4 -n -sP -PE -PA80,443,8080,53,3306,2082,2083,8443')

    print("\nResultados del escaneo:")

    for host in nm.all_hosts():
        if nm[host]['status']['state'] == 'up':
            print(f"\nIP: {host} - Estado: {nm[host]['status']['state']}")
            if nm[host].all_protocols():
                print("Servicios activos:")
                for protocol in nm[host].all_protocols():
                    ports = nm[host][protocol].keys()
                    for port in ports:
                        print(f"   - Puerto {port}: {nm[host][protocol][port]['name']} ({nm[host][protocol][port]['state']})")
            else:
                print("Sin servicios de host de web en subred.")
        else:
            print(f"\nIP: {host} - Estado: {nm[host]['status']['state']}")
    input("\nPresiona Enter para salir...")

def opcion_5():
    default_subnet = "192.168.1.0/24"
    subnet = input("[+] Introduzca la subred (por defecto, 192.168.1.0/24): ") or default_subnet

    print("\n\n             menu de argumentos")
    print("---------------------------------------------------")
    print("(1) info de la versiones de los servicios (-sV)")
    print("(2) SO que halla en esa IP (-O)")
    print("(3) rapidez (-T5)")
    print("(4) seleccionar canal para escaner (-e)")
    print("(5) seleccionar puertos especificos (-p)")
    print("(6) realizar con un script (-sC)")
    print("(0) No elegir ningún argumento")
    print("---------------------------------------------------")
    opciones = input("Elija una o más opciones del menú separadas por comas (por ejemplo, 1,3,5): ")

    nm = nmap.PortScanner()

    argumentos_escaneo = ""
    if opciones != "0":
        if "1" in opciones:
            argumentos_escaneo += " -sV"
        if "2" in opciones:
            argumentos_escaneo += " -O"
        if "3" in opciones:
            argumentos_escaneo += " -T5"
        if "4" in opciones:
            canal = input("Introduzca el canal para escanear (-e): ")
            argumentos_escaneo += f" -e {canal}"
        if "5" in opciones:
            puertos = input("Introduzca los puertos específicos (-p): ")
            argumentos_escaneo += f" -p {puertos}"
        if "6" in opciones:
            argumentos_escaneo += " -sC"

    comando = f"nmap {argumentos_escaneo} {subnet}"
    print("\nComando resultante:")
    print(comando)
    input("\nPresiona Enter para salir...")

def salir():
    print("Saliendo del programa.")
    sys.exit()

menu = {
    "1": opcion_1,
    "2": opcion_2,
    "3": opcion_3,
    "4": opcion_4,
    "5": opcion_5,
    "6": salir
}

while True:
    os.system("clear")
    print("Esta herramienta esta hecha sine el objetivo de fines criminales ni malicioso. \nEl programa no se hace responsable de uso malicioso del mismo.")
    print("\nEsta es una herramineta de escaner de redes con la libreria de python3: python-nmap")
    print("\nMenu de acciones")
    print("----------------------------------------------------")
    print("(1)IP privada propia")
    print("(2)Escaner exaustivo de una IP")
    print("(3)Escaner de la administracion de la red local")
    print("(4)Chequear estatus de network")
    print("(5)Escaner general de la red")
    print("(6)Salir")
    print("----------------------------------------------------")

    seleccion = input("Selecciona una opción (1-6): ")

    if seleccion in menu:
        menu[seleccion]()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
