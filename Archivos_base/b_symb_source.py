# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_symb_source
# Author: Homero Ortega Boada
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import math
import threading







class b_symb_source(gr.hier_block2):
    def __init__(self, Constelacion=[1+.0j,-1+.0j, .0+1j,0 -1j ]):
        gr.hier_block2.__init__(
            self, "b_symb_source",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Constelacion = Constelacion

        ##################################################
        # Variables
        ##################################################
        self.Bps = Bps = int(math.log(len(Constelacion),2))

        ##################################################
        # Blocks
        ##################################################

        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(Constelacion, 1)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_MSB_FIRST)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 256, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self, 0))


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_Bps(int(math.log(len(self.Constelacion),2)))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table(self.Constelacion)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps

