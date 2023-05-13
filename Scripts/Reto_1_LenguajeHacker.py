# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 19/04/2023

# Atributos Globales
leetAlphabetNumbers = { "a" : "4", "b" : "I3", "c" : "[", "d" : ")", "e" : "3", "f" : "|=", "g" : "&", "h" : "#", "i" : "1", "j" : ",_|", "k" : ">|", "l" : "1", "m" : "/\\/\\", "n" : "^/", "o" : "0", "p" : "|*", "q" : "(_,)", "r" : "I2", "s" : "5", "t" : "7", "u" : "(_)", "v" : "\\/", "w" : "\\/\\/", "x" : "><", "y" : "j", "z" : "2", "0" : "o", "1" : "L", "2" : "R", "3" : "E", "4" : "A", "5" : "S", "6" : "b", "7" : "T", "8" : "B", "9" : "g" }

# Función
def leetTranslator():
    print( "\n*** Reto #1: EL \"LENGUAJE HACKER\" - By ClarkCodes ***" )
    print( "Solo se traducirán letras de la a-z sin tildes ni acentos y números del 0-9." )
    print( "\nTraductor" )

    userMessage = input( "Mensaje a traducir: " )
    translatedMessage = ""

    try:
        for ch in userMessage:
            if( ch.lower() in leetAlphabetNumbers ):
                translatedMessage += leetAlphabetNumbers[ch.lower()]
            else:
                translatedMessage += ch

        print( f"\nMensaje Traducido:\n{ translatedMessage }" )

    except:
        print( "Oops... algo no ha salido bien, revise nuevamente por favor." )

    print( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )

# Llamada a la Función
leetTranslator()