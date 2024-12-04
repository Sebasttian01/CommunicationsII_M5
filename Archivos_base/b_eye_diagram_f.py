# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_eye_diagram_f
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: permite visualizar el diagrama de ojo. Parametros usados: Sps - muestras por simbolo; Vpico - amplitud pico de la señal
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_eye_diagram_f(gr.hier_block2):
    def __init__(self, Delay=0, Sps=8, samp_rate=32000):
        gr.hier_block2.__init__(
            self, "b_eye_diagram_f",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(0, 0, 0),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Delay = Delay
        self.Sps = Sps
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.N = N = Sps*256

        ##################################################
        # Blocks
        ##################################################

        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay)
        self.E3TRadio_vec_diagrama_ojo_f_0 = E3TRadio.vec_diagrama_ojo_f(Sps, samp_rate, N)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.E3TRadio_vec_diagrama_ojo_f_0, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay
        self.blocks_delay_0.set_dly(int(self.Delay))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_N(self.Sps*256)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

