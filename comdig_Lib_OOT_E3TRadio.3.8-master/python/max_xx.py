#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Aquí pretendemos demostrar el uso de un bloque con entradas y salidad vectoriales propiamente dichas 

import numpy
from gnuradio import gr

class max_xx(gr.sync_block):
    """
    compara N senales de entrada y punto a punto extrae el mayor valor, siendo la entrada vectorial
así como la salida. El usuario elige el tamano del vector, en numero de entradas, el tipo de las 
senales
    """

# lo siguiente, es para definir los requerimientos para el bloque. Es el constructor
# vemos aqui que el bloque tendra 3 entradas: el tipo de senales a manejar, el tamano de los vectores
# a manejar y el numero de senales que va a procesar.

    def __init__(self, tipo, vec_long, n_entradas):

# Los anteriores son requerimientos especificos de nosotros. En realidad lo demás lo heredamos
# de del bloque "gr.sync_blok" de la biblioteca.
# "self, name, in_sig, out_sig" es el formato establecido para ese bloque
# En realidad in_sig y out_sig son listas, hice los siguientes experiementos en el interprete:
# >>> N=5
# >>> M=3
# >>> in_sig=[(numpy.float32,N)]*M
# >>> in_sig
# [(<type 'numpy.float32'>, 5), (<type 'numpy.float32'>, 5), (<type 'numpy.float32'>, 5)]
# >>> type(in_sig)
# <type 'list'>

        gr.sync_block.__init__(self, name="max_xx", in_sig=[(tipo, vec_long)]*n_entradas, out_sig=[(tipo, vec_long)])

# Vemos que ni el siguiente metodo, ni el constructor anterior, es diferente a los realizados para streams
# Para entender el metodo siguiente hice estas pruebas en el interprete de python:
# >>> in0=[(2,3,4,5,6), (2,5,7,8,3), (1,9,1,8,6)] 
# Nota: el grc usa este formato porque el in_sig del metodo anterior, le indica que debe usar M (3) entradas 
# y que cada una de ellas tiene tamaño N (5)
# >>> type(in0)
# <type 'list'>
# >>> out[:] = numpy.max(in0,0)
# >>> out
# [2, 9, 7, 8, 6]
# >>> type(out)
# <type 'list'>
# se concluye que in0 y out son simplemente listas. De modo que numpy.max opera quiza con vectores, pero devuelve otra lista
# tambien entiendo que aunque el bloque tiene dibujadas N entradas, en terminos de programacion, en realidad
# tiene una entrada, la entrada 0, solo que dentro de esa entrada el grc le clava los N vectores.

    def work(self, input_items, output_items):
        
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = numpy.max(input_items,0)
        return len(output_items[0])

# las siguientes clases heredan de max.xx, por lo tanto contienen a work, complementada para
# el caso de entradas flotantes o complejas
# estas son las verdaderas clases a usar.

class max_cc(max_xx):
    def __init__(self, vec_long, n_entradas):
        super(max_cc, self).__init__(numpy.complex64,vec_long, n_entradas)

class max_ff(max_xx):
    def __init__(self, vec_long, n_entradas):
        super(max_ff, self).__init__(numpy.float32,vec_long, n_entradas)

