'''
 Copyright 2023 ClarkCodes

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''
# NetScanner.py
# Descripción: Utilidad de red escrita en Python para escanear y detectar dispositivos 
#   en un segmento de red indicado con nmap, obtener direcciones ip, direcciones mac y 
#   sus puertos abiertos.

# Author: Clark - @ClarkCodes
# Versión: 2.0

# Imports
import nmap
import typer
from rich import print
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn

# Constantes
SEPARATOR = "********************************************"

# Global Variables
dev_Scanner = nmap.PortScanner()

# Functions
def printFoundHosts( all_hosts_list : list[str] ):
    if len( all_hosts_list ) > 0:
        print( "[yellow]*--- Dispositivos encontrados:\n" )

        for i, host in enumerate( all_hosts_list ):
            print( SEPARATOR )
            found_device_table = Table( f"[green]Parámetro", "[green]Datos", title = f"[bold][green]*** Dispositivo #{ i + 1 } ***", title_justify = "center", box = box.ROUNDED )
            found_device_table.add_row( f"Nombre:", f"{dev_Scanner[host].hostname()}" )
            found_device_table.add_row( f"Dirección Ip:", f"{host}" )

            if 'mac' in dev_Scanner[host]['addresses']:
                found_device_table.add_row( f"Dirección MAC:", f"{dev_Scanner[host]['addresses']['mac']}" )

            found_device_table.add_row( f"Estado:", f"{dev_Scanner[host].state()}" )
            
            print( "" )
            print( found_device_table )

            protocols_list = dev_Scanner[host].all_protocols()

            if len( protocols_list ) > 0:
                protocols_table = Table( f"[green]Parámetro", "[green]Datos", title = "[bold][green]* Protocolos *", title_justify = "center", box = box.ROUNDED )
                
                for proto in dev_Scanner[host].all_protocols():
                    protocols_table.add_row( f"Protocolo:", f"{proto}" )

                    lport = dev_Scanner[host][proto].keys()
                    #lport.sort()
                    for port in lport:
                        protocols_table.add_row( f"Puerto:", f"{port}" )
                        protocols_table.add_row( f"Estado:", f"{dev_Scanner[host][proto][port]['state']}" )

                print( "" )
                print( protocols_table )

        print( f"[yellow]{SEPARATOR}" )
    else:
        print( "[bright_black]\nNo se encontraron dispositivos en el segmento de red indicado." )

def is_ip_range_valid( ip_range : str ):
    dots_counter = ip_range.count( '.' )

    if( dots_counter != 3 ):
        return False
    
    segments_list = ip_range.split( '.' )

    for index, segment in enumerate( segments_list ):
        if( ( index < 3 or ( index == 3 and segment.find( '/' ) == -1 ) ) ):
            number = int( segment )

            if( number < 0 or number > 255 ):
                return False

    return True

# Función Principal
def main():
    print( "[bold green]\n*** Clark's Network Devices Scanner ***" )
    
    while True: # Bucle para Repetir el Menú hasta que el usuario decida salir.
        print( "\n[bright_cyan]* Lobby de Opciones *[/bright_cyan]\nIngrese un rango ip para escanear la red o ingrese 'q' para salir." )

        user_input = input( "\nIngrese el Rango Ip: " )
        
        if( user_input == 'q' or user_input == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            if( not is_ip_range_valid( user_input ) ):
                raise ValueError

            print( "" )
            with Progress( SpinnerColumn(), TextColumn( "[yellow][progress.description]{task.description}" ), transient = True ) as progress:
                progress.add_task( description="[light_sky_blue1]Buscando dispositivos presentes en la red dentro del rango Ip indicado... Un momento por favor...", total = None )
                
                dev_Scanner.scan( user_input )
                printFoundHosts( dev_Scanner.all_hosts() )
            
        except ValueError:
            print( "\n❌ La estructura del rango ip no es válida, verifique nuevamente." )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( "Message Error: ", ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )