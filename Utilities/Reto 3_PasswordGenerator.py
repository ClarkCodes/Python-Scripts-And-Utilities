# Copyright 2023 ClarkCodes
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# Retos Semanales ‘23
# Reto #3: EL GENERADOR DE CONTRASEÑAS
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 20/04/2023

# Imports
import random
from enum import Enum

# Atributos Globales
# Constantes
OPT_NO_DISPONIBLE = "Opción no diponible. La configuración no se ha alterado."
LENGTH_TITLE = "Longitud"
UPPER_LETTERS_TITLE = "Letras mayúsculas"
NUMBERS_TITLE = "Números"
SYMBOLS_TITLE = "Símbolos"
REPEAT_CHARS_TITLE = "Repetición de Caracteres"
MAX_OPTS_NUM = 6

# Tuplas fuentes de datos
lowerLetters = ( "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" )
upperLetters = ( "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" )
digits = ( "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" )
symbols = ( ".", ":", ",", ";", "-", "_", "+", "*", "/", "\\", "~", "´", "`", "'", "\"", "¿", "?", "¡", "!", "@", "|", "°", "#", "$", "%", "&", "(", ")", "[", "]", "{", "}", "<", ">", "^", "=" )

# Booleanos y enteros
withUpperLetters = True
withNumbers = True
withSymbols = True
repeatChars = True
pwdLenght = 8

# Enum
class SettingType( Enum ):
    LENGTH = 1
    UPPER_LETTERS = 2
    NUMBERS = 3
    SYMBOLS = 4
    REPEAT = 5

# Funciones
def menuOpciones():
    print( f"\n* Opciones:\n\t1. {LENGTH_TITLE}\n\t2. {UPPER_LETTERS_TITLE}\n\t3. {NUMBERS_TITLE}\n\t4. {SYMBOLS_TITLE}\n\t5. {REPEAT_CHARS_TITLE}\n\t6. Generar Contraseña\n\tq - Salir\n" )

# Método generalizado de Configuraciones, residen todas menos la de longitud, esa tiene un método propio al ser muy diferente de expresar
def settings( settingType : SettingType ):
    # Identificación de variables globales para poder usarlas
    global withUpperLetters 
    global withNumbers
    global withSymbols

    # Variables locales de Configuración
    title : str 
    settingOption : str
    stateCondition : bool
    genderLetter = "o"

    # Se establecen los valores de las variables locales en base a la configuración respectiva que el usuario seleccionó
    if( settingType == SettingType.UPPER_LETTERS ):
        title = UPPER_LETTERS_TITLE
        settingOption = UPPER_LETTERS_TITLE.lower()
        stateCondition = withUpperLetters
        genderLetter = "a"

    elif( settingType == SettingType.NUMBERS ):
        title = NUMBERS_TITLE
        settingOption = NUMBERS_TITLE.lower()
        stateCondition = withNumbers

    elif( settingType == SettingType.SYMBOLS ):
        title = SYMBOLS_TITLE
        settingOption = SYMBOLS_TITLE.lower()
        stateCondition = withSymbols
    
    # Se muestra la Cabecera y el Menú de la Configuración que se eligió, esto se hace de manera generalizada una sola vez
    print( f"\n* Configuración - {title}\nEstado: ", end = "" )
    print( f"{title} incluíd{genderLetter}s" if stateCondition else f"Sin {settingOption}" )
    print( f"\n\t1. Incluír {settingOption}\n\t2. Sin {settingOption}\n" )
    
    userOp = input( "Elija una opción: " )

    # Se verifica lo que ingresó el usuario, si es una opción válida se asigna el valor correspondiente y se muestra el mensaje de confirmación indicando el valor elegido, si el usuario ingesó una opción no válida, no disponible, se muestra un mensaje de error
    if( userOp == "1" ):
        if( settingType == SettingType.UPPER_LETTERS ):
            withUpperLetters = True

        elif( settingType == SettingType.NUMBERS ):
            withNumbers = True

        elif( settingType == SettingType.SYMBOLS ):
            withSymbols = True
            
        print( f"Listo, {title} incluíd{genderLetter}s.\n" )

    elif( userOp == "2" ):
        if( settingType == SettingType.UPPER_LETTERS ):
            withUpperLetters = False

        elif( settingType == SettingType.NUMBERS ):
            withNumbers = False

        elif( settingType == SettingType.SYMBOLS ):
            withSymbols = False

        print( f"Listo, la contraseña será sin {settingOption}.\n" )

    else:
        print( OPT_NO_DISPONIBLE )


# Configuración para la Longitud de la Contraseña
def lenSetting():
    global pwdLenght # Identificación de variable global para poder usarla

    print( f"\n* Configuración - {LENGTH_TITLE}\nEstado: ", end = "" )
    print( f"Contraseña de {pwdLenght} caracteres de {LENGTH_TITLE}." )
    print( f"\n\t1. 8 caracteres\n\t2. 16 caracteres\n" )
    userOp = input( "Elija una opción: " )

    if( userOp == "1" or userOp == "2" ): # Se verifica si es una opción válida disponible, sino se muestra el mensaje de error correspondiente
        if( userOp == "1" ): # Se asigna el valor que corresponde según lo ingresado por el usuario y se muestra el mensaje de confirmación de como quedó la configuración
            pwdLenght = 8

        elif( userOp == "2" ):
            pwdLenght = 16
            
        print( f"Listo, {LENGTH_TITLE} de contraseña a generar establecida en {pwdLenght} caracteres.\n" )

    else:
        print( OPT_NO_DISPONIBLE )

# Configuración para la Repetición de Caracteres
def repeatCharsSetting():
    global repeatChars # Identificación de variable global para poder usarla
    statePreffix = "Se " if repeatChars else "No se "

    print( f"\n* Configuración - {REPEAT_CHARS_TITLE}\nEstado: ", end = "" )
    print( f"{statePreffix}permite la {REPEAT_CHARS_TITLE}." )
    print( f"\n\t1. Permitir la {REPEAT_CHARS_TITLE}\n\t2. No permitir la {REPEAT_CHARS_TITLE}\n" )
    userOp = input( "Elija una opción: " )

    if( userOp == "1" or userOp == "2" ): # Se verifica si es una opción válida disponible, sino se muestra el mensaje de error correspondiente
        repeatChars = userOp == "1" # Se asigna el valor que corresponde según lo ingresado por el usuario y se muestra el mensaje de confirmación de como quedó la configuración
        
        statePreffix = "Se " if repeatChars else "No se "
        print( f"Listo, {statePreffix}permitirá la {REPEAT_CHARS_TITLE}.\n" )

    else:
        print( OPT_NO_DISPONIBLE )

# Función Principal
def pwdGenerator():
    print( "\n*** Reto #3: EL GENERADOR DE CONTRASEÑAS - By ClarkCodes ***" )
    
    while True: # Bucle para Repetir el Menú hasta que el usuario decida salir.
        print( "\n* Lobby de Opciones *\nSeleccione una de las opciones disponible para cambiar sus parámetros o ingrese 'q' para salir." )
        menuOpciones()

        userOp = input( "Opción Elegida: " )
        
        if( userOp == 'q' or userOp == 'Q' ): # Condición de Salida
            print( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )
            break

        try:
            userNumericOption = int( userOp ) # Se convierte la opcion ingresada por el usuario de texto a entero

            if( userNumericOption >= 1 and userNumericOption <= MAX_OPTS_NUM ): # Se verifica si la opción ingresada es válida, estando dentro el rango de opciones disponibles
                # Se invocan las funciones de configuración correspondiente, en el modo adecuado según elija el usuario o si elije Generar la Contraseña, se hace lo propio.
                if( userNumericOption == SettingType.LENGTH.value ): # Option #1
                    lenSetting()

                elif( userNumericOption == SettingType.UPPER_LETTERS.value ): # Option #2
                    settings( SettingType.UPPER_LETTERS )

                elif( userNumericOption == SettingType.NUMBERS.value ): # Option #3
                    settings( SettingType.NUMBERS )

                elif( userNumericOption == SettingType.SYMBOLS.value ): # Option #4
                    settings( SettingType.SYMBOLS )

                elif( userNumericOption == SettingType.REPEAT.value ): # Option #5
                    repeatCharsSetting()

                elif( userNumericOption == MAX_OPTS_NUM ): # Motor de Generación de Contraseña Aleatoria
                    print("*** Generando Contraseña Segura... ***\nUn momento por favor...\n")
                    charSet = [] # Se declara una lista y se le añade la tupla de letras en minúsculas, que son las básicas
                    charSet.extend( lowerLetters )
                
                    if( withUpperLetters ): # Se añaden los caracteres de las demás tuplas a la lista charSet para la contraseña, según la configuración establecida por el usuario o según la configuración por default si no se ha modificado, de esta manera, esta lista queda con todos los caracteres disponibles para la contraseña, se deberan entonces escoger aleatoriamente de aquí y así generarla
                        charSet.extend( upperLetters )
                
                    if( withNumbers ):
                        charSet.extend( digits )
                
                    if( withSymbols ):
                        charSet.extend( symbols )
                
                    generatedPwd = "" # Se declara una nueva variable string para la contraseña que se va a generar, entonces se itera en un bucle for el número de veces establecidas en la configuración actual de longitud de la contraseña
                    chDrawn = "" # Variable para el caracter elegido aleatoriamente

                    for index in range( pwdLenght ):
                        if( repeatChars ): # Si la Repetición de Caracteres está permitida simplemente se genera el caracter aleatoriamente y se lo añade a la contraseña generada hasta completar la cantidad de caracteres requeridos según la configuración establecida o no alterada por el usuario.
                            chDrawn = charSet[ random.randint( 0, len( charSet ) - 1 ) ] # Se va añadiendo un caracter aleatoriamente de todos los que se encuentren en la lista charSet, según la configuración establecida, hasta completar la longitud de caracteres establecidos para la contraseña.
                            generatedPwd += chDrawn
                            
                        else:
                            while True: # (Bloque que simula un Do-While) Por lo contrario, si no está permitida, se genera el caracter y se verifica que no exista como parte de la contraseña, si ya existe, se volverá a generar un caracter hasta que se detecte que no exista dentro de la contraseña, entonces añade el caracter a esta y sale del bucle while hacia la siguiente iteración del for, y así sucesivamente hasta completar la cantidad de caracteres requeridos, ya sean 8 o 16 según la configuración establecida o no alterada por el usuario.
                                chDrawn = charSet[ random.randint( 0, len( charSet ) - 1 ) ] 
                                
                                if( generatedPwd.find( chDrawn ) == -1 ):
                                    generatedPwd += chDrawn
                                    break
                
                    print( f"Contraseña Generada: {generatedPwd}" ) # Finalmente, se muestra la contraseña generada al usuario.

            else:
                print( "Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
            
        except ValueError:
            print( "Opción ingresada no disponible, ingrese solo una de las opciones disponibles en el menú, verifique nuevamente." )
        except:
            print( "Oops... algo no ha salido bien, revise nuevamente por favor." )


# Llamada a la Función
pwdGenerator()
