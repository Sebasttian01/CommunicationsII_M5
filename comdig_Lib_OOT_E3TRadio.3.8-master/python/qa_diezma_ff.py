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
from diezma_ff import diezma_ff

class qa_diezma_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        senal_entrante = (1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        src = blocks.vector_source_f (senal_entrante)
        diez = diezma_ff(4)
        snk = blocks.vector_sink_f ()
        self.tb.connect (src, diez)
        self.tb.connect (diez, snk)

       # Aqui va lo que querramos incluir para probar y encontrar fallas, como prints.
        self.tb.run ()
        senal_salida = snk.data ()
        salida_esperada = (1,5,9,13,17)
        print ("la respuesta; ", senal_salida)
        print ("la esperada; ", salida_esperada)

        self.assertFloatTuplesAlmostEqual (salida_esperada, senal_salida, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_diezma_ff, "qa_diezma_ff.xml")
