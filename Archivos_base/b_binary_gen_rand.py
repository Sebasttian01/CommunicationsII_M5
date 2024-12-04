# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_binary_rand_source_f
# Author: Homero Ortega Boada. Universidad Industrial de Santader
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: This is a binary random generator with output of type float
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_binary_gen_rand(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_binary_rand_source_f",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Blocks
        ##################################################

        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self, 0))


