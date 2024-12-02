#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

import numpy
from gnuradio import gr

class amplificador_ff(gr.sync_block):
    """
    actua como un amplificador. Para ello la funcion work() toma cada valor de entrada y lo multiplica
por el coeficiente que tiene previamente preconfigurado el bloque. Ese coeficiente puede ser cambiado aun
despues de haber sido preconfigurado el bloque, gracias al callback representado en la funcion
set_ka
    """
    def __init__(self, Kamp=1):
        gr.sync_block.__init__(self, name="amplificador_ff", in_sig=[numpy.float32], out_sig=[numpy.float32])
        self.Kamp=Kamp

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>
        out[:] = in0*self.Kamp
        return len(output_items[0])

    # Este es el caller que permite cambiar en caliente el coeficiente de amplificacion
    # el xml debe ser informado que esta es la funcion a llamar para ese tipo de cambios
    def set_ka(self, Kamp):
        self.Kamp=Kamp

