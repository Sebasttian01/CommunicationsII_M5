# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_1tubes_2tubes
# Author: Homero Ortega Boada
# Description: Usado para extraer dos chorros de datos de diferentes velocidades (dos tubos) en un solo gran tubo. N1 es el numero de espacios que ocupa en el gran tubo, el primer tubo. N2 es para el segunto tubo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_1tubes_2tubes(gr.hier_block2):
    def __init__(self, N=8, N1=5, N2=3):
        gr.hier_block2.__init__(
            self, "b_1tubes_2tubes",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.N = N
        self.N1 = N1
        self.N2 = N2

        ##################################################
        # Blocks
        ##################################################

        self.blocks_streams_to_stream_0_0 = blocks.streams_to_stream(gr.sizeof_gr_complex*1, N2)
        self.blocks_streams_to_stream_0 = blocks.streams_to_stream(gr.sizeof_gr_complex*1, N1)
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_gr_complex*1, (N1+N2))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_streams_0, 2), (self.blocks_streams_to_stream_0, 2))
        self.connect((self.blocks_stream_to_streams_0, 3), (self.blocks_streams_to_stream_0, 3))
        self.connect((self.blocks_stream_to_streams_0, 1), (self.blocks_streams_to_stream_0, 1))
        self.connect((self.blocks_stream_to_streams_0, 0), (self.blocks_streams_to_stream_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 4), (self.blocks_streams_to_stream_0, 4))
        self.connect((self.blocks_stream_to_streams_0, 7), (self.blocks_streams_to_stream_0_0, 2))
        self.connect((self.blocks_stream_to_streams_0, 5), (self.blocks_streams_to_stream_0_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 6), (self.blocks_streams_to_stream_0_0, 1))
        self.connect((self.blocks_streams_to_stream_0, 0), (self, 1))
        self.connect((self.blocks_streams_to_stream_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_stream_to_streams_0, 0))


    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_N1(self):
        return self.N1

    def set_N1(self, N1):
        self.N1 = N1

    def get_N2(self):
        return self.N2

    def set_N2(self, N2):
        self.N2 = N2

