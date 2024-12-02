#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Es que, como ocurre tambien en Simulink, la salida vectorial de un bloque no se puede visualizar en un
# scope normal, se requiere uno vectorial.
#    Tambien entiendo que la diferencia entre stream y vector es un poco difusa, pues la programación de este bloque
# demuestra que todo lo que llamamos streams son tambien vectores, lo que sucede es que se desconoce su longitud.
# Me imagino que un vector es lo que llamariamos en Simulink un frame, en grc una senal con datos empaquetados
# mientras el stream es cuando el frame solo tiene un dato empaquetado.

import numpy
from gnuradio import gr

class sum_vectors_ff(gr.sync_block):
    """
    Este es un sumador muy sencillo de senales entrantes. Lo ha creado HOB basicamente, para aprender a hacerlo. 
La idea era poder sumar dos vectores entrantes. Pero entiendo que lo que estamos logrando es en realidad
usar vectores de longitud N=128, internamente, para el cálculo, mientras a la hora de usar el bloque en GRC, 
la entrada y salida del bloque siguen siendo streams. Por esa razon el bloque no tiene sus puertos obscurecidos.
    """
    def __init__(self):
        gr.sync_block.__init__(self,name="sum_vectors_ff", in_sig=[(numpy.float32, 128), (numpy.float32, 128)], out_sig=[(numpy.float32,128)])

# El siguiente metodo es usado por el programa que crea el GRC. El es el que sabe tomar las entradas del bloque
# construido y con los valores apropiados, usar el siguiente metodo.

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0+in1
        return len(output_items[0])

# DUDA:
# - No veo que papel juega in_sig, out_sig.
# Hipotesis1: supongo que, a la hora de hacer conexiones, es cuando son usados estos datos
# es de pronto alli, donde datos tomados de in_sig son pasados a al bloque work.
# Hipotesis2: in_sig y out_sig, son parte del formato exigido por el constructor de la clase
#             que estamos heredando. Ese formato nos exige pasar de esa manera, informacion sobre
#             la entrada y la salida del bloque.
# Hipotesis3: aplica la hipotesis2 en primer lugar y la hipotesis1 en segundo lugar.


