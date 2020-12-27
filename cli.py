from argparse import ArgumentParser
from read import read_egresos

def cli():
    '''
    Lee argumentos de la consola al usar el comando instalado.
    '''
    parser = ArgumentParser(
        description='''Genera gráficas de cajas y bigotes del registro de egresos elegido por el usuario.
            Se requieren unicamente elegir el año, en caso de no agregar más parametros los valores por defecto son falsos.
            '''
        )
    parser.add_argument('year', type=int, help='Elegir el año correspondiente entre 2010 y 2018.')
    parser.add_argument('-be', type=str, default=None,
                        help='Su valor indica si se desea generar un boxplot por edad del registro.')
    parser.add_argument('-bp', type=str, default=None,
                        help='Su valor indica si se desea generar un boxplot por peso del registro.')
    parser.add_argument('-bt', type=str, default=None,
                        help='Su valor indica si se desea generar un boxplot por talla del registro.')

    return parser.parse_args()

arguments = cli()
year = arguments.year
if(arguments.be != None):
    edad = True
else:
    edad = False

if(arguments.bp != None):
    peso = True
else:
    peso = False

if(arguments.bt != None):
    talla = True
else:
    talla = False

read_egresos(year, edad, peso, talla)

print(arguments)

    
