#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
 

import numpy
from gnuradio import gr

class sumador(gr.sync_block):
    """
    Este es un sumador muy sencillo de señales entrantes. Lo he creado básicamente, para aprender a hacerlo
    CORREGIR: podria llamarse sumador_ff
    """
    def __init__(self):
        gr.sync_block.__init__(self,name="sumador", in_sig=[numpy.float32, numpy.float32], out_sig=[numpy.float32])

# lo anterior es el constructor, que permite darle las características al bloque
# los parámetros son los que estén predefinidos según la documentación del bloque
# así, la documentación señala solo una entrada y una salida.

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0+in1
        return len(output_items[0])

