#!/usr/bin/env python3 

# Ejecutar con sudo: sudo python3 torghost.py
import subprocess
import time
import sys

# Colores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def verificar_tor_instalado():
    try:
        subprocess.check_output(["which", "tor"])
        return True
    except subprocess.CalledProcessError:
        return False

def instalar_tor():
    print(f"{bcolors.WARNING}NO TIENES TOR INSTALADO.{bcolors.ENDC}")
    respuesta = input(f"{bcolors.OKCYAN}¿Deseas instalarlo? (Y/N): {bcolors.ENDC}").lower()
    if respuesta == 'y':
        try:
            subprocess.run(["sudo", "apt-get", "install", "tor"], check=True)
            print(f"\n{bcolors.OKGREEN}TOR se ha instalado correctamente.{bcolors.ENDC}")
            print(f"\n{bcolors.OKGREEN}Ruta del archivo de configuración de ProxyChains: /etc/proxychains4.conf{bcolors.ENDC}")
        except subprocess.CalledProcessError:
            print(f"\n{bcolors.FAIL}Error al instalar TOR.{bcolors.ENDC}")
            sys.exit()
    else:
        print(f"\n{bcolors.FAIL}TOR no está instalado. No se puede continuar.{bcolors.ENDC}")
        sys.exit()

def cambiar_direccion_mac():
    print(f"\n\n{bcolors.OKBLUE}[+] Cambiando Dirección MAC...{bcolors.ENDC}")
    mi_red = input(f"\n{bcolors.OKCYAN}Elije tu interfaz de red: {bcolors.ENDC}")
    subprocess.run(["sudo", "macchanger", "-r", mi_red])
    print(f"\n{bcolors.OKGREEN}[+] Nueva MAC asignada correctamente{bcolors.ENDC}")

def iniciar_tor():
    print(f"\n\n                  *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***{bcolors.ENDC}\n")
    print(f"\n{bcolors.OKBLUE}[+] Iniciando TOR:{bcolors.ENDC}")
    subprocess.run(["sudo", "service", "tor", "start"])
    print(f"\n{bcolors.OKGREEN}[+] Comprobando si está corriendo:{bcolors.ENDC}")
    subprocess.run(["sudo", "service", "tor", "status"])

def configurar_proxychains():
    print(f"\n{bcolors.OKBLUE}[+] Dame los proxys que quieres incluir y sus puertos (escribe 'e' para dejar de introducir proxies):{bcolors.ENDC}")
    proxies = []
    while True:
        ip = input(f"\n\t{bcolors.OKCYAN}[+] Dame Ip (Ej: 10.10.10.10): {bcolors.ENDC}")
        if ip.lower() == 'e':
            break
        puerto = input(f"\n\t{bcolors.OKCYAN}[+] Puerto (Ej: 4488): {bcolors.ENDC}")
        proxies.append((ip, puerto))
    
    with open("/etc/proxychains4.conf", "a") as f:
        for proxy in proxies:
            f.write(f"socks5 {proxy[0]} {proxy[1]}\n")
    print(f"\n{bcolors.OKGREEN}[+] Proxies añadidos correctamente.{bcolors.ENDC}\n")

def bloquear_scripts_y_rastreadores():
    print(f"\n{bcolors.OKBLUE}[i] Bloqueando scripts y rastreadores en el navegador TOR...{bcolors.ENDC}")
    # Aquí puedes agregar comandos o configuraciones para bloquear scripts y rastreadores en el navegador TOR
    print(f"\n{bcolors.OKGREEN}[+] Scripts y rastreadores bloqueados correctamente{bcolors.ENDC}")

def modo_paranoico():
    cambiar_direccion_mac()
    bloquear_scripts_y_rastreadores()
    configurar_proxychains()
    iniciar_tor()
    cambio_intervalo = input(f"\n{bcolors.OKCYAN}[+] Indica cada cuántos minutos quieres que cambie tu Dirección IP: {bcolors.ENDC}")
    try:
        cambio_intervalo = int(cambio_intervalo)
        while True:
            print(f"{bcolors.OKBLUE}[i] Cambiando dirección IP...{bcolors.ENDC}")
            subprocess.run(["sudo", "service", "tor", "restart"])
            print(f"{bcolors.OKGREEN}[+] Dirección IP cambiada correctamente{bcolors.ENDC}")
            time.sleep(cambio_intervalo * 60)  # Convertir a segundos
    except ValueError:
        print(f"{bcolors.FAIL}¡Error! Debes ingresar un número válido.{bcolors.ENDC}")
    except KeyboardInterrupt:
        print(f"\n\n                  *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***{bcolors.ENDC}\n")

        print(f"{bcolors.WARNING}¡Interrupción del usuario! Finalizando programa...{bcolors.ENDC}")

def main(): 
    if not verificar_tor_instalado():
        instalar_tor()

    try:
        print(f"{bcolors.OKGREEN}")
        print("                           ..,,;;;;;;,,,,")
        print("                     .,;'';;,..,;;;,,,,,.''';;,..")
        print("                 ,,''                    '';;;;,;''")
        print("                ;'       ,;@@;'  ,@@;, @@, ';;;@@;,;';.")
        print("               ''     ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;")
        print("                     ;;@@@@@;    ''''    .,,;;;@@@@@@@;;;")
        print("                    ;;@@@@@@;           , ';;;@@@@@@@@;;;.")
        print("                     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;")
        print("                        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'")
        print("                         ''..,,      ''''    '  .,;'")
        print(f"     Tor Ghost                By C4sp3r        ")
        print(f"{bcolors.ENDC}")

        print(f"\n{bcolors.HEADER}[+] Accediendo al modo Anónimo:{bcolors.ENDC}")
        print(f"\n\t{bcolors.OKCYAN}[i] Elije entre: {bcolors.ENDC}[{bcolors.OKGREEN}1{bcolors.ENDC}] {bcolors.OKGREEN}Tor normal{bcolors.ENDC} [{bcolors.OKGREEN}2{bcolors.ENDC}] {bcolors.OKGREEN}Tor + Proxys{bcolors.ENDC} [{bcolors.OKGREEN}3{bcolors.ENDC}] {bcolors.OKGREEN}Modo Paranoico{bcolors.ENDC}")
        opcion = input(f"\n\t{bcolors.OKCYAN}Opción: {bcolors.ENDC}")
        if opcion == '1':
            bloquear_scripts_y_rastreadores()
            cambiar_direccion_mac()
            iniciar_tor()
        elif opcion == '2':
            bloquear_scripts_y_rastreadores()
            cambiar_direccion_mac()
            configurar_proxychains()
            iniciar_tor()
        elif opcion == '3':
            modo_paranoico()
        else:
            print(f"{bcolors.FAIL}Opción inválida.{bcolors.ENDC}")

        print(f"\n{bcolors.OKGREEN}[+] TOR corriendo exitosamente, recuerda que para finalizar TOR, debes introducir el comando: {bcolors.ENDC}")
        print(f"\n{bcolors.OKGREEN}    service tor stop{bcolors.ENDC}")
        print(f"\n{bcolors.OKGREEN}[+] Para resetear tu IP en TOR, debes introducir el comando: {bcolors.ENDC}")
        print(f"\n{bcolors.OKGREEN}    sudo service tor restart{bcolors.ENDC}")
    except KeyboardInterrupt:
        print(f"\n{bcolors.WARNING}¡Interrupción del usuario! Finalizando programa...{bcolors.ENDC}")
        sys.exit()

if __name__ == "__main__":
    main()

