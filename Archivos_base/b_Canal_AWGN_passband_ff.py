# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Canal_AWGN_passband_ff
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Este bloque es un simulador de un canal AWGN en version pasobandas con ruido aditivo de banda angosta pasobandas. De modo que tiene las siguientes características: suma ruido blanco a la señal,  restringe el ancho de banda e Introduce un retardo a la señal. Parametros: Ch_NodB - altura de la PSD del ruido blanco bandabase; samp_rate - frecuencia de muestreo de la señal; B - ancho de banda bandabase, Fc frecuencia central, Ch_Toffset - retardo dado en muestraas que el canal introduce
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import cmath
import math
import numpy
import random
import threading







class b_Canal_AWGN_passband_ff(gr.hier_block2):
    def __init__(self, B=1000, Ch_NodB=1000, Ch_Toffset=0, Fc=1000, samp_rate=1000):
        gr.hier_block2.__init__(
            self, "b_Canal_AWGN_passband_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.B = B
        self.Ch_NodB = Ch_NodB
        self.Ch_Toffset = Ch_Toffset
        self.Fc = Fc
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.No = No = math.pow(10.,(Ch_NodB)/10.)
        self.P = P = No*10000
        self.Vrms = Vrms = math.sqrt(P)

        ##################################################
        # Blocks
        ##################################################

        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Ch_Toffset)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (Fc-B/2),
                (Fc+B/2),
                ((B/2)/16),
                window.WIN_HAMMING,
                6.76))
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Vrms, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.B/2), (self.Fc+self.B/2), ((self.B/2)/16), window.WIN_HAMMING, 6.76))

    def get_Ch_NodB(self):
        return self.Ch_NodB

    def set_Ch_NodB(self, Ch_NodB):
        self.Ch_NodB = Ch_NodB
        self.set_No(math.pow(10.,(self.Ch_NodB)/10.))

    def get_Ch_Toffset(self):
        return self.Ch_Toffset

    def set_Ch_Toffset(self, Ch_Toffset):
        self.Ch_Toffset = Ch_Toffset
        self.blocks_delay_0.set_dly(int(self.Ch_Toffset))

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.B/2), (self.Fc+self.B/2), ((self.B/2)/16), window.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.B/2), (self.Fc+self.B/2), ((self.B/2)/16), window.WIN_HAMMING, 6.76))

    def get_No(self):
        return self.No

    def set_No(self, No):
        self.No = No
        self.set_P(self.No*10000)

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self.set_Vrms(math.sqrt(self.P))

    def get_Vrms(self):
        return self.Vrms

    def set_Vrms(self, Vrms):
        self.Vrms = Vrms
        self.analog_noise_source_x_0.set_amplitude(self.Vrms)

