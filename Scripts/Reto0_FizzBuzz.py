# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 19/04/2023

# Función
def fizzBuzz():
    print( "\n*** Reto #0: EL FAMOSO \"FIZZ BUZZ\" - By ClarkCodes ***" )
    print( "\nSerie FizzBuzz:\n" )
    for i in range( 1, 101 ):
        if( i % 3 == 0 and i % 5 == 0 ):
            print( "fizzbuzz" )
        elif( i % 3 == 0 ):
            print( "fizz" )
        elif( i % 5 == 0 ):
            print( "buzz" )
        else:
            print( i )

    print( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark.\n" )

# Llamada a la Función
fizzBuzz()