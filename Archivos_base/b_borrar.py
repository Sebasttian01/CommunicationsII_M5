# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_borrar
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import math
import threading







class b_borrar(gr.hier_block2):
    def __init__(self, Sps=4, h=[1,1,1,1]):
        gr.hier_block2.__init__(
            self, "b_borrar",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Sps = Sps
        self.h = h

        ##################################################
        # Blocks
        ##################################################

        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2.)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-0.5))
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self, 0))


    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0.set_taps(self.h)

