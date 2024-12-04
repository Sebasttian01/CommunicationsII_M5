# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_sampler2_cc
# Author: Homero Ortega
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Realiza un muestreo o decimacion de la senal
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_sampler2_cc(gr.hier_block2):
    def __init__(self, Decimation=1):
        gr.hier_block2.__init__(
            self, "b_sampler2_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Decimation = Decimation

        ##################################################
        # Blocks
        ##################################################

        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.E3TRadio_diezma_ff_0_0 = E3TRadio.diezma_ff(Decimation, 0)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Decimation, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.E3TRadio_diezma_ff_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.E3TRadio_diezma_ff_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))


    def get_Decimation(self):
        return self.Decimation

    def set_Decimation(self, Decimation):
        self.Decimation = Decimation

