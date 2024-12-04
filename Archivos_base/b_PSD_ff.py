# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_PSD_ff
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
import E3TRadio
import numpy
import threading







class b_PSD_ff(gr.hier_block2):
    def __init__(self, Ensayos=1000000, N=1024, samp_rate_audio=22000):
        gr.hier_block2.__init__(
            self, "b_PSD_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*N),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ensayos = Ensayos
        self.N = N
        self.samp_rate_audio = samp_rate_audio

        ##################################################
        # Variables
        ##################################################
        self.Ka = Ka = numpy.full(N,1./(Ensayos*N))

        ##################################################
        # Blocks
        ##################################################

        self.fft_vxx_0 = fft.fft_vfc(N, True, window.rectangular(N), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(Ka)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(N)
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, 1000000000)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos
        self.set_Ka(numpy.full(self.N,1./(self.Ensayos*self.N)))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_Ka(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.fft_vxx_0.set_window(window.rectangular(self.N))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio

    def get_Ka(self):
        return self.Ka

    def set_Ka(self, Ka):
        self.Ka = Ka
        self.blocks_multiply_const_vxx_0_0.set_k(self.Ka)

