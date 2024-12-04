# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_FFT_p
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
import threading







class b_FFT_p(gr.hier_block2):
    def __init__(self, Nu=8):
        gr.hier_block2.__init__(
            self, "b_FFT_p",
                gr.io_signature.makev(8, 8, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature.makev(8, 8, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Nu = Nu

        ##################################################
        # Blocks
        ##################################################

        self.fft_vxx_1_0 = fft.fft_vcc(Nu, True, window.rectangular(Nu), False, 1)
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_gr_complex*1, Nu)
        self.blocks_streams_to_vector_0 = blocks.streams_to_vector(gr.sizeof_gr_complex*1, Nu)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_streams_to_vector_0, 0), (self.fft_vxx_1_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self, 1))
        self.connect((self.blocks_vector_to_streams_0, 2), (self, 2))
        self.connect((self.blocks_vector_to_streams_0, 3), (self, 3))
        self.connect((self.blocks_vector_to_streams_0, 4), (self, 4))
        self.connect((self.blocks_vector_to_streams_0, 5), (self, 5))
        self.connect((self.blocks_vector_to_streams_0, 6), (self, 6))
        self.connect((self.blocks_vector_to_streams_0, 7), (self, 7))
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_vector_to_streams_0, 0))
        self.connect((self, 0), (self.blocks_streams_to_vector_0, 0))
        self.connect((self, 1), (self.blocks_streams_to_vector_0, 1))
        self.connect((self, 2), (self.blocks_streams_to_vector_0, 2))
        self.connect((self, 3), (self.blocks_streams_to_vector_0, 3))
        self.connect((self, 4), (self.blocks_streams_to_vector_0, 4))
        self.connect((self, 5), (self.blocks_streams_to_vector_0, 5))
        self.connect((self, 6), (self.blocks_streams_to_vector_0, 6))
        self.connect((self, 7), (self.blocks_streams_to_vector_0, 7))


    def get_Nu(self):
        return self.Nu

    def set_Nu(self, Nu):
        self.Nu = Nu
        self.fft_vxx_1_0.set_window(window.rectangular(self.Nu))

