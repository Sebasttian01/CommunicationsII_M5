# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_derivador_ff
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: saca la derivada a una senal compleja: parte real e imaginaria por aparte. a cada una le sca una diferencia y la divide entre el tiempo de muestreo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_derivador_ff(gr.hier_block2):
    def __init__(self, F_muestreo=1000):
        gr.hier_block2.__init__(
            self, "b_derivador_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.F_muestreo = F_muestreo

        ##################################################
        # Blocks
        ##################################################

        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(F_muestreo)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.blocks_sub_xx_0, 0))


    def get_F_muestreo(self):
        return self.F_muestreo

    def set_F_muestreo(self, F_muestreo):
        self.F_muestreo = F_muestreo
        self.blocks_multiply_const_vxx_1.set_k(self.F_muestreo)

