#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from ej_amplificador_ff import ej_amplificador_ff

class qa_ej_amplificador_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # Aqui debe ir nuestro flujograma
        senal_entrante = (0, 1, -2, 5.5, -0.5)
        src = blocks.vector_source_f (senal_entrante)
        mult = ej_amplificador_ff (2)
        snk = blocks.vector_sink_f ()
        self.tb.connect (src, mult)
        self.tb.connect (mult, snk)

       # Aqui se corre el flujograma por primera vez.
        self.tb.run ()

        # Aqui va nuestro flujograma de nuevo, pero con otra senal entrante
        senal_entrante = snk.data ()
        src = blocks.vector_source_f (senal_entrante)
        mult = ej_amplificador_ff (2)
        snk = blocks.vector_sink_f ()
        self.tb.connect (src, mult)
        self.tb.connect (mult, snk)

       # Aqui va lo que querramos incluir para probar y encontrar fallas, como prints.
        self.tb.run ()
        senal_salida = snk.data ()
        print ('la senal de salida es: ', senal_salida)
        salida_esperada = (0, 4, -8, 22, -2)
        self.assertFloatTuplesAlmostEqual (salida_esperada, senal_salida, 6)

if __name__ == '__main__':
    gr_unittest.run(qa_ej_amplificador_ff, "qa_ej_amplificador_ff.xml")
