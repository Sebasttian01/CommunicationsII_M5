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
from diezmoppenh3_ff import diezmoppenh3_ff

class qa_diezmoppenh3_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        senal_entrante=(1., 2., 3., 4., 5.,6,7,8,9,10)
        paso=4
        Delay1=0
        src=blocks.vector_source_f (senal_entrante)
        prom=diezmoppenh3_ff(paso,Delay1)
        snk = blocks.vector_sink_f ()
        self.tb.connect (src, prom)
        self.tb.connect (prom, snk)

        # check data
        self.tb.run ()
        senal_salida = snk.data ()
        print ("entrada: ", senal_entrante)
        salida_esperada = (1., 0., 0., 0., 5.,0,0,0,9,0)
        print ("salida esperada: ", salida_esperada)
        print ("salida obtenida: ", senal_salida)

        self.assertFloatTuplesAlmostEqual (salida_esperada, senal_salida, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_diezmoppenh3_ff, "qa_diezmoppenh3_ff.xml")
