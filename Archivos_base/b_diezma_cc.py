# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_diezma_cc
# Author: Homero Ortega. Universidad Industrial de Santander. Colombia
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Realiza un diezmado del mundo real. Sps es la distancia entre las muestras a diezmar, D es el punto de inicio.   El codigo esta en diezma_ff.py.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_diezma_cc(gr.hier_block2):
    def __init__(self, D=0, Sps=8):
        gr.hier_block2.__init__(
            self, "b_diezma_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.D = D
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.E3TRadio_diezma_ff_0_0 = E3TRadio.diezma_ff(Sps, D)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, D)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.E3TRadio_diezma_ff_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.E3TRadio_diezma_ff_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))


    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.E3TRadio_diezma_ff_0.set_ka(self.D)
        self.E3TRadio_diezma_ff_0_0.set_ka(self.D)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

