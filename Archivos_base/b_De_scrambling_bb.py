# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_De_scrambling_bb
# Author: Homero Ortega Boada
# Description: Realiza el scrambling
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import b_De_scrambling_bb_e_Multiply as e_Multiply  # embedded python block
import b_De_scrambling_bb_e_bipol_to_unip as e_bipol_to_unip  # embedded python block
import b_De_scrambling_bb_e_unip_to_bipol as e_unip_to_bipol  # embedded python block
import threading







class b_De_scrambling_bb(gr.hier_block2):
    def __init__(self, retardo=0, semilla=42):
        gr.hier_block2.__init__(
            self, "b_De_scrambling_bb",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.retardo = retardo
        self.semilla = semilla

        ##################################################
        # Blocks
        ##################################################

        self.e_unip_to_bipol = e_unip_to_bipol.blk()
        self.e_bipol_to_unip = e_bipol_to_unip.blk()
        self.e_Multiply = e_Multiply.blk()
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_char*1, retardo)
        self.analog_random_uniform_source_x_0_0 = analog.random_uniform_source_b(0, 2, semilla)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_uniform_source_x_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.e_unip_to_bipol, 0))
        self.connect((self.e_Multiply, 0), (self.e_bipol_to_unip, 0))
        self.connect((self.e_bipol_to_unip, 0), (self, 0))
        self.connect((self.e_unip_to_bipol, 0), (self.e_Multiply, 1))
        self.connect((self, 0), (self.e_Multiply, 0))


    def get_retardo(self):
        return self.retardo

    def set_retardo(self, retardo):
        self.retardo = retardo
        self.blocks_delay_0_0.set_dly(int(self.retardo))

    def get_semilla(self):
        return self.semilla

    def set_semilla(self, semilla):
        self.semilla = semilla

