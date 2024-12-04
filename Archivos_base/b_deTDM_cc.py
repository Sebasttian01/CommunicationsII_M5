# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_deTDM_cc
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Demultiplexa una senal que ha sido multiplexada con el bloque b_TDM
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_deTDM_cc(gr.hier_block2):
    def __init__(self, Nspcell=16):
        gr.hier_block2.__init__(
            self, "b_deTDM_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(8, 8, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Nspcell = Nspcell

        ##################################################
        # Variables
        ##################################################
        self.N = N = 8

        ##################################################
        # Blocks
        ##################################################

        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*Nspcell, N)
        self.blocks_vector_to_stream_1_0_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_1_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_0_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_vector_to_stream_1_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, (Nspcell*N))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0_0_0_0_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self.blocks_vector_to_stream_1_0, 0), (self, 3))
        self.connect((self.blocks_vector_to_stream_1_0_0, 0), (self, 6))
        self.connect((self.blocks_vector_to_stream_1_0_0_0, 0), (self, 7))
        self.connect((self.blocks_vector_to_stream_1_0_0_0_0, 0), (self, 0))
        self.connect((self.blocks_vector_to_stream_1_0_0_1, 0), (self, 5))
        self.connect((self.blocks_vector_to_stream_1_0_1, 0), (self, 4))
        self.connect((self.blocks_vector_to_stream_1_0_1_0, 0), (self, 1))
        self.connect((self.blocks_vector_to_stream_1_0_2, 0), (self, 2))
        self.connect((self.blocks_vector_to_streams_0, 7), (self.blocks_vector_to_stream_1_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 6), (self.blocks_vector_to_stream_1_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 4), (self.blocks_vector_to_stream_1_0_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_vector_to_stream_1_0_0_0_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 2), (self.blocks_vector_to_stream_1_0_0_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 5), (self.blocks_vector_to_stream_1_0_1, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_vector_to_stream_1_0_1_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 3), (self.blocks_vector_to_stream_1_0_2, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0_0_0_0_0, 0))


    def get_Nspcell(self):
        return self.Nspcell

    def set_Nspcell(self, Nspcell):
        self.Nspcell = Nspcell

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

