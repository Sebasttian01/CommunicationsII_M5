# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_mod_constelacion_cb
# Author: Homero Ortega Boada
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_mod_constelacion_cb(gr.hier_block2):
    def __init__(self, Constelacion=[(1.41 + 1.41*1j),  (-1.41 + 1.41*1j), (-1.41 - 1.41*1j), (1.41 - 1.41*1j)]):
        gr.hier_block2.__init__(
            self, "b_mod_constelacion_cb",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Constelacion = Constelacion

        ##################################################
        # Blocks
        ##################################################

        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc(Constelacion, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self, 0))
        self.connect((self, 0), (self.digital_chunks_to_symbols_xx, 0))


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.digital_chunks_to_symbols_xx.set_symbol_table(self.Constelacion)

