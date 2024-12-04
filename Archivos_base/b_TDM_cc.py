# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_TDM_cc
# Author: Homero Ortega
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: multiplexa hasta N=8 usuarios/n con Nspcell muestras por usuario
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_TDM_cc(gr.hier_block2):
    def __init__(self, Nspcell=8):
        gr.hier_block2.__init__(
            self, "b_TDM_cc",
                gr.io_signature.makev(8, 8, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
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

        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, (N*Nspcell))
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*Nspcell, N)
        self.blocks_stream_to_vector_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, Nspcell)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_streams_to_vector_0, 1))
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.blocks_streams_to_vector_0, 3))
        self.connect((self.blocks_stream_to_vector_0_0_0_0, 0), (self.blocks_streams_to_vector_0, 7))
        self.connect((self.blocks_stream_to_vector_0_0_1, 0), (self.blocks_streams_to_vector_0, 5))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_streams_to_vector_0, 2))
        self.connect((self.blocks_stream_to_vector_0_1_0, 0), (self.blocks_streams_to_vector_0, 6))
        self.connect((self.blocks_stream_to_vector_0_2, 0), (self.blocks_streams_to_vector_0, 4))
        self.connect((self.blocks_streams_to_vector_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self, 1), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self, 2), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self, 3), (self.blocks_stream_to_vector_0_0_0_0, 0))
        self.connect((self, 4), (self.blocks_stream_to_vector_0_0_1, 0))
        self.connect((self, 5), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self, 6), (self.blocks_stream_to_vector_0_1_0, 0))
        self.connect((self, 7), (self.blocks_stream_to_vector_0_2, 0))


    def get_Nspcell(self):
        return self.Nspcell

    def set_Nspcell(self, Nspcell):
        self.Nspcell = Nspcell

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

