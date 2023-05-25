"""
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
"""
"""
Retos Semanales ‘23
Reto #3: EL GENERADOR DE CONTRASEÑAS
Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
Podrás configurar generar contraseñas con los siguientes parámetros:
- Longitud: Entre 8 y 16.
- Con o sin letras mayúsculas.
- Con o sin números.
- Con o sin símbolos.
(Pudiendo combinar todos estos parámetros entre ellos)

Autor: Clark - @ClarkCodes
Fecha de Resolución: 20/04/2023

Última Actualización: 25/05/2023
Versión: 2.0.1
"""

# Imports
import random
import typer
from rich import print
from rich.table import Table
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn
from enum import Enum

# Atributos Globales
# Constantes
OPT_NO_DISPONIBLE = "\n❌ Opción no diponible. La configuración no se ha alterado."
CONF_APPLIED = f"\n✔ ¡Listo! ->"
CONF_TAG = "* Configuración -"
ALLOWED = "PERMITIDO"
NOT_ALLOWED = "NO PERMITIDO"
LENGTH_TITLE = "Longitud"
UPPER_LETTERS_TITLE = "Letras mayúsculas"
NUMBERS_TITLE = "Números"
SYMBOLS_TITLE = "Símbolos"
REPEAT_CHARS_TITLE = "Repetición de Caracteres"
MAX_OPTS_NUM = 8

# Tuplas fuentes de datos
LOWER_LETTERS = ( "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" )
UPPER_LETTERS = ( "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" )
DIGITS = ( "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" )
SYMBOLS = ( ".", ":", ",", ";", "-", "_", "+", "*", "/", "\\", "~", "´", "`", "'", "\"", "¿", "?", "¡", "!", "@", "|", "°", "#", "$", "%", "&", "(", ")", "[", "]", "{", "}", "<", ">", "^", "=" )

# Parámetros de Configuración
withUpperLetters = True
withNumbers = True
withSymbols = True
repeatChars = True
pwdLenght = 8

# Contraseña Generada
generatedPwd = ""

# Parámetros de Calidad
lowerLettersCant = 0
upperLettersCant = 0
numbersCant = 0
symbolsCant = 0

# Enums
class OptionType( Enum ):
    CHECK_CONFIG = 1
    LENGTH = 2
    UPPER_LETTERS = 3
    NUMBERS = 4
    SYMBOLS = 5
    REPEAT = 6
    GENERATE_PASSWORD = 7
    QUALITY_REPORT = MAX_OPTS_NUM

class ElementType( Enum ):
    LOWER_LETTERS = 1
    UPPER_LETTERS = 2
    NUMBERS = 3
    SYMBOLS = 4

# Funciones
def menu_opciones():
    options_table = Table( "[green]Opción", "[green]Descripción", title = "[bold green]Menú", title_justify = "center", box = box.ROUNDED )
    options_table.add_row( "1. ", f"Estado Actual de la Configuración" )
    options_table.add_row( "2. ", f"{LENGTH_TITLE}" )
    options_table.add_row( "3. ", f"{UPPER_LETTERS_TITLE}" )
    options_table.add_row( "4. ", f"{NUMBERS_TITLE}" )
    options_table.add_row( "5. ", f"{SYMBOLS_TITLE}" )
    options_table.add_row( "6. ", f"{REPEAT_CHARS_TITLE}" )
    options_table.add_row( "7. ", f"Generar Contraseña" )
    options_table.add_row( "8. ", f"Reporte de Calidad" )
    options_table.add_row( "q. ", f"Salir" )
    print( options_table )

def check_settings_state():
    global withUpperLetters 
    global withNumbers
    global withSymbols
    global pwdLenght
    global repeatChars

    options_table = Table( f"[green]Configuración", "[green]Estado", title = "[bold][green]* Estado Actual de la Configuración *", title_justify = "center", box = box.ROUNDED )
    options_table.add_row( f"{LENGTH_TITLE}", f"{pwdLenght} caracteres" )
    options_table.add_row( f"{UPPER_LETTERS_TITLE}", f"{ALLOWED}" if withUpperLetters else f"{NOT_ALLOWED}" )
    options_table.add_row( f"{NUMBERS_TITLE}", f"{ALLOWED}" if withNumbers else f"{NOT_ALLOWED}" )
    options_table.add_row( f"{SYMBOLS_TITLE}", f"{ALLOWED}" if withSymbols else f"{NOT_ALLOWED}" )
    options_table.add_row( f"{REPEAT_CHARS_TITLE}", f"{ALLOWED}" if repeatChars else f"{NOT_ALLOWED}" )
    
    print( " " )
    print( options_table )

# Método generalizado de Configuraciones, residen todas menos la de longitud, esa tiene un método propio al ser muy diferente de expresar
def settings( setting_type : OptionType ):
    # Identificación de variables globales para poder usarlas
    global withUpperLetters 
    global withNumbers
    global withSymbols

    # Variables locales de Configuración
    title : str 
    setting_option : str
    state_condition : bool
    gender_letter = "o"

    # Se establecen los valores de las variables locales en base a la configuración respectiva que el usuario seleccionó
    if( setting_type == OptionType.UPPER_LETTERS ):
        title = UPPER_LETTERS_TITLE
        setting_option = UPPER_LETTERS_TITLE.lower()
        state_condition = withUpperLetters
        gender_letter = "a"

    elif( setting_type == OptionType.NUMBERS ):
        title = NUMBERS_TITLE
        setting_option = NUMBERS_TITLE.lower()
        state_condition = withNumbers

    elif( setting_type == OptionType.SYMBOLS ):
        title = SYMBOLS_TITLE
        setting_option = SYMBOLS_TITLE.lower()
        state_condition = withSymbols
    
    # Se muestra la Cabecera y el Menú de la Configuración que se eligió, esto se hace de manera generalizada una sola vez
    print( f"\n[bold][green]{CONF_TAG} {title}[/bold]\nEstado: ", end = "" )
    print( f"{title} incluíd{gender_letter}s" if state_condition else f"Sin {setting_option}" )
    options_table = Table( "[green]Opción", "[green]Descripción", title = "Seleccione una Opción", title_justify = "center", box = box.ROUNDED )
    options_table.add_row( "1. ", f"Incluír {setting_option}" )
    options_table.add_row( "2. ", f"Sin {setting_option}" )
    print( " " )
    print( options_table )

    print( " " )
    user_op = input( "Elija una opción: " )

    # Se verifica lo que ingresó el usuario, si es una opción válida se asigna el valor correspondiente y se muestra el mensaje de confirmación indicando el valor elegido, si el usuario ingesó una opción no válida, no disponible, se muestra un mensaje de error
    if( user_op == "1" ):
        if( setting_type == OptionType.UPPER_LETTERS ):
            withUpperLetters = True

        elif( setting_type == OptionType.NUMBERS ):
            withNumbers = True

        elif( setting_type == OptionType.SYMBOLS ):
            withSymbols = True
            
        print( f"[green]{CONF_APPLIED} {title} incluíd{gender_letter}s." )

    elif( user_op == "2" ):
        if( setting_type == OptionType.UPPER_LETTERS ):
            withUpperLetters = False

        elif( setting_type == OptionType.NUMBERS ):
            withNumbers = False

        elif( setting_type == OptionType.SYMBOLS ):
            withSymbols = False

        print( f"[green]{CONF_APPLIED} La contraseña será sin {setting_option}." )

    else:
        print( OPT_NO_DISPONIBLE )


# Configuración para la Longitud de la Contraseña
def lenSetting():
    global pwdLenght # Identificación de variable global para poder usarla

    print( f"\n[bold][green]{CONF_TAG} {LENGTH_TITLE}[/bold]\nEstado: ", end = "" )
    print( f"Contraseña de {pwdLenght} caracteres de {LENGTH_TITLE}." )
    print( "\nUna contraseña segura debe tener una logitud de entre 8 y 16 caracteres, ingrese un número entero dentro de este rango, si ingresa un número menor, la contraseña será establecida en 8 caracteres y en 16 si ingresa uno mayor.\n" )
    
    try:
        lenght = int( typer.prompt( "Cantidad de Caracteres" ) )

        if( lenght >= 8 and lenght <= 16 ):
            pwdLenght = lenght

        else: 
            pwdLenght = 8 if lenght < 8 else 16

        print( f"[green]{CONF_APPLIED} {LENGTH_TITLE} de contraseña a generar establecida en {pwdLenght} caracteres." )

    except ValueError:
        print( OPT_NO_DISPONIBLE )

# Configuración para la Repetición de Caracteres
def repeat_chars_setting():
    global repeatChars # Identificación de variable global para poder usarla
    state_preffix = "Se " if repeatChars else "No se "

    print( f"\n[bold][green]{CONF_TAG} {REPEAT_CHARS_TITLE}[/bold]\nEstado: ", end = "" )
    print( f"{state_preffix}permite la {REPEAT_CHARS_TITLE}." )

    options_table = Table( "[green]Opción", "[green]Descripción", title = "Seleccione una Opción", title_justify = "center", box = box.ROUNDED )
    options_table.add_row( "1. ", f"Permitir la {REPEAT_CHARS_TITLE}" )
    options_table.add_row( "2. ", f"No permitir la {REPEAT_CHARS_TITLE}" )
    print( " " )
    print( options_table )

    print( " " )
    user_op = input( "Elija una opción: " )

    if( user_op == "1" or user_op == "2" ): # Se verifica si es una opción válida disponible, sino se muestra el mensaje de error correspondiente
        repeatChars = user_op == "1" # Se asigna el valor que corresponde según lo ingresado por el usuario y se muestra el mensaje de confirmación de como quedó la configuración
        
        state_preffix = "Se " if repeatChars else "No se "
        print( f"[green]{CONF_APPLIED} {state_preffix}permitirá la {REPEAT_CHARS_TITLE}." )

    else:
        print( OPT_NO_DISPONIBLE )

# Counter - Devuelve la cantidad de caracteres que existen en la contraseña del conjunto indicado
def counter( current_password: str, type: ElementType ):
    source = []
    cant = 0

    if( type == ElementType.LOWER_LETTERS ):
        source = LOWER_LETTERS
    elif( type == ElementType.UPPER_LETTERS ):
        source = UPPER_LETTERS
    elif( type == ElementType.NUMBERS ):
        source = DIGITS
    elif( type == ElementType.SYMBOLS ):
        source = SYMBOLS
    
    found = any( ch in current_password for ch in source ) # Se detecta si hay al menos un caracter del conjunto indicados

    if ( found ):
        for ch in source: # Se cuenta cuantos caracteres de este tipo hay en la contraseña
            cant += current_password.count( ch ) 

    return cant

# Revisión de Calidad - Se juntan conteos y estadisticas de la contraseña
def quality_check( current_password : str ):
    global lowerLettersCant
    global upperLettersCant
    global numbersCant
    global symbolsCant
    lowerLettersCant = 0
    upperLettersCant = 0
    numbersCant = 0
    symbolsCant = 0

    # Letras Minúsculas
    lowerLettersCant = counter( current_password, ElementType.LOWER_LETTERS )
    
    # Letras Mayúsculas
    if( withUpperLetters ): # Se detecta la configuración de letras mayúsculas, si estan permitidas se cuentan cuantas hay, si no estan permitidas por en es 0
        upperLettersCant = counter( current_password, ElementType.UPPER_LETTERS ) # Si se encontró letras mayúsculas se cuentan cuantas hay, más adelante se hace lo mismo con los números y los símbolos        

    # Números
    if( withNumbers ):
        numbersCant = counter( current_password, ElementType.NUMBERS )

    # Símbolos
    if( withSymbols ):
        symbolsCant = counter( current_password, ElementType.SYMBOLS )
        
# Reporte de Calidad
def quality_report():
    print( f"\n[bold green]* Reporte de Calidad *" )
    if( generatedPwd != "" ):
        print( f"\n- El reporte es en base a la última contraseña generada." )
        options_table = Table( f"[green]Parámetro", "[green]Datos", title = "[bold][green]* Reporte *", title_justify = "center", box = box.ROUNDED )
        options_table.add_row( f"Contraseña generada:", f"{generatedPwd}" )
        options_table.add_row( f"Longitud establecida:", f"{pwdLenght} caracteres" )
        options_table.add_row( f"Repetición de Caracteres:", f"{ALLOWED}" if repeatChars else f"{NOT_ALLOWED}" )
        options_table.add_row( f"Cantidad de Letras Minúsculas:", f"{lowerLettersCant}" )
        options_table.add_row( f"Uso de Letras Mayúsculas: ", f"{ALLOWED}" if withUpperLetters else f"{NOT_ALLOWED}" )
        options_table.add_row( f"Cantidad de Letras Mayúsculas: ", f"{upperLettersCant}" )
        options_table.add_row( f"Uso de Números: ", f"{ALLOWED}" if withNumbers else f"{NOT_ALLOWED}" )
        options_table.add_row( f"Cantidad de Números: ", f"{numbersCant}" )
        options_table.add_row( f"Uso de Símbolos: ", f"{ALLOWED}" if withSymbols else f"{NOT_ALLOWED}" )
        options_table.add_row( f"Cantidad de Símbolos: ", f"{symbolsCant}" )
    
        print( " " )
        print( options_table )
    else:
        print( f"\nNo se ha generado una contraseña todavía, genere una para acceder al respectivo reporte de calidad." )

# Motor de Generación de Contraseña Aleatoria
def safe_password_generator():
    global generatedPwd
    generatedPwd = "" 
    granting_chars = {} # Diccionario que se usa para asegurar un caracter de cada conjunto permitido en la configuración, las letras minúsculas siempre esta permitidas de base y los demas son configurables.
    ch_drawn = "" # Variable para el caracter elegido aleatoriamente
    char_set = [] # Lista que servirá como pool de caracteres disponibles para elegir uno de manera aleatoria en cada iteración del for para así completar la contraseña
    char_set.extend( LOWER_LETTERS ) # A esta lista se le iran añadiendo las tuplas de caracteres según se halla indicado en la configuración, empezando por las letras minúsculas que son la base obligatoria, los demás son configurables
                
    # Se determina un caracter de letra minúscula aleatoriamente para asegurar que siempre exista al menos una letra minúscula
    rand_index = random.randint( 0, pwdLenght - 1 ) # Primero se determina el indice donde irá este caracter en la contraseña basado en la longitud establecida en la configuración
    rand_ch = random.choice( LOWER_LETTERS ) # Se elige una letra minúscula aleatoriamente
    
    granting_chars[rand_index] = rand_ch # Se añaden el índice elegido como clave y el caracter elegido como valor, formando un par clave-valor, al diccionario, dado que es el primer par, no se verifica si ya existe ese indice

    if( withUpperLetters ): # Preparación: Se añaden los caracteres de las demás tuplas a la lista char_set pool de caracteres para la contraseña, según la configuración establecida por el usuario o según la configuración por default si no se ha modificado, de esta manera, esta lista queda con todos los caracteres disponibles, se deberan entonces escoger aleatoriamente de aquí para así poder generarla
        char_set.extend( UPPER_LETTERS )
        
        while True:
            rand_index = random.randint( 0, pwdLenght - 1 ) # Se determina también el indice donde irá el caracter de letra mayúscula en la contraseña

            if( not rand_index in granting_chars ): # Dado que ya hay un par en el diccionario, se verifica que el indice obtenido no exista todavía
                rand_ch = random.choice( UPPER_LETTERS ) # Si en efecto el índice no existe, se determina un caracter de letra mayúscula aleatorio, se añade el par al diccionario y se sale del bucle, pero si ya existe el índice, se genera uno nuevo y se hace nuevamente la verificación, esto se hace con los otros dos conjuntos de números y símbolos también si es que estan permitidos en la configuración
                granting_chars[rand_index] = rand_ch
                break
                
    if( withNumbers ):
        char_set.extend( DIGITS )

        while True:
            rand_index = random.randint( 0, pwdLenght - 1 )

            if( not rand_index in granting_chars ):
                rand_ch = random.choice( DIGITS )
                granting_chars[rand_index] = rand_ch
                break
                
    if( withSymbols ):
        char_set.extend( SYMBOLS )

        while True:
            rand_index = random.randint( 0, pwdLenght - 1 )

            if( not rand_index in granting_chars ):
                rand_ch = random.choice( SYMBOLS )
                granting_chars[rand_index] = rand_ch
                break

    # Motor de Generación de la Contraseña
    for index in range( pwdLenght ): 
        insertion_pending = index in granting_chars # Se verifica si existe una clave en el diccionario que coincida con el índice actual del for en la contraseña, de ser así significa que hay que insertar ese caracter almacenado en el valor de ese par del diccionario en la contraseña, por lo tanto hay una inserción pendiente

        if( repeatChars ): # Si la Repetición de Caracteres está permitida simplemente se añade un caracter a la contraseña sin verificar si se repite o no, así hasta completar la cantidad de caracteres requeridos según la configuración establecida.
            generatedPwd += granting_chars[index] if insertion_pending else random.choice( char_set ) # Si hay una insercion pendiente, se obtiene el caracter del valor del par del diccionario cuya clave coincide con el índice en la iteración actual del for y se lo añade a la contraseña, si no hay una inserción pendiente simplemente se añade un caracter aleatorio a la contraseña de la lista pool de caracteres de manera normal
  
        else: # Modo de No Repetición
            if( insertion_pending and generatedPwd.find( granting_chars[index] ) == -1 ): # Se verifica si hay una inserción pendiente y si el caracter del diccionario que habría que insertar no existe todavía en la contraseña, si no existe, se lo añade a la contraseña, si ya existe o si no hay una inserción pendiente se sigue el funcionamiento normal
                generatedPwd += granting_chars[index]

            else:
                while True: # (Bloque que simula un Do-While) Si no está permitida la repetición, se elige el caracter aleatoriamente y se verifica que no exista como parte de la contraseña, si ya existe, se volverá a generar un caracter hasta que se detecte que no exista dentro de la contraseña, entonces se añade el caracter y se sale del bucle while hacia la siguiente iteración del for, y así sucesivamente hasta completar la cantidad de caracteres requeridos.
                    ch_drawn = random.choice( char_set )
                                
                    if( generatedPwd.find( ch_drawn ) == -1 ):
                        generatedPwd += ch_drawn
                        break

    quality_check( generatedPwd )
                
    print( f"\n[bold][green]-*- Contraseña Generada -*-[/green]: [purple4]{generatedPwd}\n" ) # Finalmente, se muestra la contraseña generada al usuario.

# Función Principal
def main():
    print( "[bold green]\n*** Reto #3: EL GENERADOR DE CONTRASEÑAS - By ClarkCodes ***" )
    
    while True: # Bucle para Repetir el Menú hasta que el usuario decida salir.
        print( "\n[bright_cyan]* Lobby de Opciones *[/bright_cyan]\nSeleccione una de las opciones disponibles para cambiar sus parámetros, generar la contraseña o ingrese 'q' para salir.\n" )
        menu_opciones()

        user_op = input( "\nOpción Elegida: " )
        
        if( user_op == 'q' or user_op == 'Q' ): # Condición de Salida
            print( "[green]\n✅ Esto ha sido todo por hoy.\n❤ Muchas gracias por ejecutar este Script, hasta la próxima...💻 Happy Coding!,👋🏼 bye :D\n😎 Clark." )
            break

        try:
            user_numeric_option = int( user_op ) # Se convierte la opcion ingresada por el usuario de texto a entero

            if( user_numeric_option >= 1 and user_numeric_option <= MAX_OPTS_NUM ): # Se verifica si la opción ingresada es válida, estando dentro el rango de opciones disponibles
                # Se invocan las funciones de configuración correspondiente, en el modo adecuado según elija el usuario o si elije Generar la Contraseña, se hace lo propio.
                if( user_numeric_option == OptionType.CHECK_CONFIG.value ): # Option #1
                    check_settings_state()
                
                elif( user_numeric_option == OptionType.LENGTH.value ): # Option #2
                    lenSetting()

                elif( user_numeric_option == OptionType.UPPER_LETTERS.value ): # Option #3
                    settings( OptionType.UPPER_LETTERS )

                elif( user_numeric_option == OptionType.NUMBERS.value ): # Option #4
                    settings( OptionType.NUMBERS )

                elif( user_numeric_option == OptionType.SYMBOLS.value ): # Option #5
                    settings( OptionType.SYMBOLS )

                elif( user_numeric_option == OptionType.REPEAT.value ): # Option #6
                    repeat_chars_setting()

                elif( user_numeric_option == OptionType.GENERATE_PASSWORD.value ): # Option #7
                    with Progress( SpinnerColumn(), TextColumn( "[progress.description]{task.description}" ) ) as progress:
                        progress.add_task( description="[light_sky_blue1]*** Generando Contraseña Segura... Un momento por favor...", total = None )
                    
                    safe_password_generator()
                
                elif( user_numeric_option == OptionType.QUALITY_REPORT.value ): # Option #8
                    quality_report()
            else:
                print( "\n❌ Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
            
        except ValueError:
            print( "\n❌ Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
        except Exception as ex:
            print( "\n❌ Oops... algo no ha salido bien, revise nuevamente por favor." )
            print( "Message Error: ", ex )

# Llamada a la Función Principal usando typer
if __name__ == "__main__":
    typer.run( main )