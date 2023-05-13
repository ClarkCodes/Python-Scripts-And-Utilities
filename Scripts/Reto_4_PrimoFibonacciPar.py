# Retos Semanales ‘23
# Reto #4: PRIMO, FIBONACCI Y PAR
# Escribe un programa que, dado un número, compruebe y muestre si es primo,
# fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

# Autor: Clark - @ClarkCodes
# Fecha de Resolución: 24/04/2023

# Imports
import math

# Funciones
def isPrime( n : int ) -> bool:
    for i in range( 2, n ):
        if( ( n % i ) == 0 ):
            return False
    return True

def isEven( n : int ) -> bool:
    return ( n % 2 ) == 0

def isFibonacci( n : int ) -> bool: # Propiedad de los números Fibonacci: Un número es de Fibonacci si y solo si uno o ambos de (5 * n^2 + 4) o (5 * n^2 - 4) es un cuadrado perfecto    
    baseOperation = 5 * ( n ** 2 )
    return math.sqrt( baseOperation + 4 ).is_integer() or math.sqrt( baseOperation - 4 ).is_integer()

def numberVerifier():
    print( "\n*** Reto #4: PRIMO, FIBONACCI Y PAR - By ClarkCodes ***" )
    
    while True: # Bucle para Repetir el Menú hasta que el usuario decida salir.
        print( "\nIngrese un número para verificar si es Primo, parte de la serie de Fibonacci y si es Par. Ingrese 'q' para salir.\nNo se admiten números negativos, si se ingresa uno no se tomará en cuenta el signo." )
        userOp = input( "Número: " )
        
        if( userOp == 'q' or userOp == 'Q' ): # Condición de Salida
            print( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima... Happy Coding!, bye :D\nClark." )
            break

        try:
            number = abs( int( userOp ) ) # Se convierte la opcion ingresada por el usuario de texto a entero

            primeStateSuffix = "" if isPrime( number ) else "no "
            fibonacciStateSuffix = "" if isFibonacci( number ) else "no "
            evenStatePostfix = "Par" if isEven( number ) else "Impar"
            
            print( "\n* Estas son las características: " )
            print( f"\tEl número {number} {primeStateSuffix}es Primo, {fibonacciStateSuffix}es Fibonacci y es {evenStatePostfix}." )

        except ValueError:
            print( "Solo se permite un número entero positivo para verificar sus características o la letra 'q' para salir, verifique nuevamente." )
        except:
            print( "Oops... algo no ha salido bien, revise nuevamente por favor." )

# Llamada a la Función
numberVerifier()