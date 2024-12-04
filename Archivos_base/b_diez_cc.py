# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_diez_cc
# Author: Homero Ortega
# Copyright: RadioGis UIS
# Description: Realiza un diezmado del mundo real. N es la distancia entre las muestras a diezmar (En el caso de requerir diezmar una senal digitales equivale a Sps (Samples per symbol)), M es el punto de inicio.

# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_diez_cc(gr.hier_block2):
    def __init__(self, M=0, N=8):
        gr.hier_block2.__init__(
            self, "b_diez_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.M = M
        self.N = N

        ##################################################
        # Blocks
        ##################################################

        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, M)
        self.E3TRadio_diezmador_cc_0 = E3TRadio.diezmador_cc(N)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezmador_cc_0, 0), (self, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.E3TRadio_diezmador_cc_0, 0))
        self.connect((self, 0), (self.blocks_delay_0_0, 0))


    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.blocks_delay_0_0.set_dly(int(self.M))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

