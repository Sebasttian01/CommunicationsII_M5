# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_MS_vector
# Author: Homero Ortega Boada
# Description: genera la senal modulada en bandabase de una estacion movil. A diferencia del b_MS, la senal que se genera no es aleatoria, sino que esta dada por un vector que representa la senal binaria del usuario. Es util cuando se realizan pruebas para conocer si lo que se recibe es lo mismo que se envia, gracias a que los datos se repiten periodicamente
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import math
import threading







class b_MS_vector(gr.hier_block2):
    def __init__(self, Constelacion=[1+.0j,-1+.0j, .0+1j,0 -1j ], N=1, senal=(134,7)):
        gr.hier_block2.__init__(
            self, "b_MS_vector",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Constelacion = Constelacion
        self.N = N
        self.senal = senal

        ##################################################
        # Variables
        ##################################################
        self.Bps = Bps = int(math.log(len(Constelacion),2))

        ##################################################
        # Blocks
        ##################################################

        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(Constelacion, 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_b(senal, True, 1, [])
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_MSB_FIRST)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(N)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.E3TRadio_zero_order_hold2_cc_0, 0))


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_Bps(int(math.log(len(self.Constelacion),2)))
        self.digital_chunks_to_symbols_xx_0.set_symbol_table(self.Constelacion)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.N)

    def get_senal(self):
        return self.senal

    def set_senal(self, senal):
        self.senal = senal
        self.blocks_vector_source_x_0.set_data(self.senal, [])

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps

