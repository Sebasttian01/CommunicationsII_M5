# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_scrambling_ff
# Author: Homero Ortega Boada
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Realiza el scrambling
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_scrambling_ff(gr.hier_block2):
    def __init__(self, retardo=0, semilla=42):
        gr.hier_block2.__init__(
            self, "b_scrambling_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.retardo = retardo
        self.semilla = semilla

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_char*1, retardo)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_b(0, 2, semilla)
        self.E3TRadio_unipolar_to_bipolar_ff_0_0 = E3TRadio.unipolar_to_bipolar_ff(1.)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))


    def get_retardo(self):
        return self.retardo

    def set_retardo(self, retardo):
        self.retardo = retardo
        self.blocks_delay_0.set_dly(int(self.retardo))

    def get_semilla(self):
        return self.semilla

    def set_semilla(self, semilla):
        self.semilla = semilla

