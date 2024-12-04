# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_noise_dB_f
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Genera ruido blanco gaussiano, pidiendo como entrada el valor de la PSD, osea, No en dB. Parametros usados: samp_rate (Hz) es la frecuencia de muestreo de la senal que genera este bloque, NoDB (dB) es la altura de la PSD que como se sabe, para el ruido blanco es una constante
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import math
import threading







class b_noise_dB_f(gr.hier_block2):
    def __init__(self, NodB=0, samp_rate=10000):
        gr.hier_block2.__init__(
            self, "b_noise_dB_f",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.NodB = NodB
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.No = No = math.pow(10.,(NodB)/10.)
        self.P = P = No*samp_rate
        self.Vrms = Vrms = math.sqrt(P)

        ##################################################
        # Blocks
        ##################################################

        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Vrms, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self, 0))


    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB
        self.set_No(math.pow(10.,(self.NodB)/10.))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_P(self.No*self.samp_rate)

    def get_No(self):
        return self.No

    def set_No(self, No):
        self.No = No
        self.set_P(self.No*self.samp_rate)

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

