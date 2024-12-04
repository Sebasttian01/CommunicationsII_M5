# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_eye_diagram2_f
# Author: Homero Ortega
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: permite visualizar el diagrama de ojo. Parametros usados: N es el numero de muestras en el intervalo de tiempo a graficar, se recomienda que N=2*Sps, donde Sps es el numero de muestras por simbolo; samp_rate es la frecuencia de muestreo; Delay es el retraso que se le puede aplicar a la senal para centrar mejor el ojo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import b_eye_diagram2_f_epy_block_0 as epy_block_0  # embedded python block
import threading







class b_eye_diagram2_f(gr.hier_block2):
    def __init__(self, Delay=0, Nvol=100, Sps=8, samp_rate=32000):
        gr.hier_block2.__init__(
            self, "b_eye_diagram2_f",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(0, 0, 0),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Delay = Delay
        self.Nvol = Nvol
        self.Sps = Sps
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.Spsi = Spsi = 32
        self.N = N = 64

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=Spsi,
                decimation=Sps,
                taps=[],
                fractional_bw=0)
        self.epy_block_0 = epy_block_0.vec_diagrama_ojo2_f(N=64, samp_rate=samp_rate, Ncurvas=Nvol)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Delay)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.epy_block_0, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_stream_to_vector_0_0, 0))


    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay
        self.blocks_delay_0.set_dly(int(self.Delay))

    def get_Nvol(self):
        return self.Nvol

    def set_Nvol(self, Nvol):
        self.Nvol = Nvol
        self.epy_block_0.Ncurvas = self.Nvol

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_Spsi(self):
        return self.Spsi

    def set_Spsi(self, Spsi):
        self.Spsi = Spsi

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

