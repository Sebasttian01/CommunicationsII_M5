# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_USRP_2_USRP
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Este bloque es el simulador de un canal inalambrico que incluye 2 USRPs, uno en la parte transmisora y otro en la receptora. Se puede usar cuando no se tengan USRP fisicos a la mano. Parametros usados: samp_rate (Hz) es la frecuencia de muestreo de la señal que entra y la que sale de este bloque; Center freq (Hz) frecuencia central del canal inalambrico; Bandwidth  (Hz) ancho de banda pasobandas del canal inalambrico; ; Toffset (numero de muestras de offset) permtite programar un tiempo de retardo de la senal en propagacion; Foffset (Hz) permite programar una desviacion entre la frecuencia central usada en la transmision y la usada en la recepcion; Phoffset (Rad) permite programar una desviacion entre el angulo de la portadora usada en transmision y la usada en recepcion; Vruido (volt) nivel del ruido blanco; Katt (lineal) nivel de atenuacion que la senal transmitida sufre en el proceso de propagacion.
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







class b_USRP_2_USRP(gr.hier_block2):
    def __init__(self, B=130000, Fc=200000000, Foffset=0., Katt=10., Phoffset=((numpy.pi)*2*random.random()), Toffset=5, Vruido=0., samp_rate=(100e6/512)):
        gr.hier_block2.__init__(
            self, "b_USRP_2_USRP",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.B = B
        self.Fc = Fc
        self.Foffset = Foffset
        self.Katt = Katt
        self.Phoffset = Phoffset
        self.Toffset = Toffset
        self.Vruido = Vruido
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (B/2.),
                (B/8.),
                window.WIN_HAMMING,
                6.76))
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1./Katt+0j)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, Toffset)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Foffset, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Vruido, 42)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cmath.exp(1j * Phoffset))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.B/2.), (self.B/8.), window.WIN_HAMMING, 6.76))

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset
        self.analog_sig_source_x_0.set_frequency(self.Foffset)

    def get_Katt(self):
        return self.Katt

    def set_Katt(self, Katt):
        self.Katt = Katt
        self.blocks_multiply_const_vxx_0.set_k(1./self.Katt+0j)

    def get_Phoffset(self):
        return self.Phoffset

    def set_Phoffset(self, Phoffset):
        self.Phoffset = Phoffset
        self.analog_const_source_x_1_0.set_offset(cmath.exp(1j * self.Phoffset))

    def get_Toffset(self):
        return self.Toffset

    def set_Toffset(self, Toffset):
        self.Toffset = Toffset
        self.blocks_delay_0.set_dly(int(self.Toffset))

    def get_Vruido(self):
        return self.Vruido

    def set_Vruido(self, Vruido):
        self.Vruido = Vruido
        self.analog_noise_source_x_0.set_amplitude(self.Vruido)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.B/2.), (self.B/8.), window.WIN_HAMMING, 6.76))

