# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_accum_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Hace lo mismo que el acum, pero con senales complejas. Es un acumulador que se resetea cada N muestras. Arranca en la muestra M.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_accum_cc(gr.hier_block2):
    def __init__(self, M=0, N=0):
        gr.hier_block2.__init__(
            self, "b_accum_cc",
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

        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.E3TRadio_acumulador_truncado_ff_0_0 = E3TRadio.acumulador_truncado_ff(N,M)
        self.E3TRadio_acumulador_truncado_ff_0 = E3TRadio.acumulador_truncado_ff(N,M)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_acumulador_truncado_ff_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.E3TRadio_acumulador_truncado_ff_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.E3TRadio_acumulador_truncado_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.E3TRadio_acumulador_truncado_ff_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))


    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.E3TRadio_acumulador_truncado_ff_0.set_ka(self.M)
        self.E3TRadio_acumulador_truncado_ff_0_0.set_ka(self.M)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

