# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_unipolar2bipolar_ff
# Author: Homero Ortega
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_unipolar2bipolar_ff(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_unipolar2bipolar_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2.)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, (-1./2.))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_add_xx_0, 1))


