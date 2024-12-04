# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_sound_USRP_Sink
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Es algo parecido a un USRP Source pero en vez de usar una antena, usa la bocina de sonido del computador, en un rango de frecuencias entre 0 Hz y  22500 Hz para explotar al maximo las capacidades de audio que usualmente tienen los computadores. Las salidas que este bloque tiene son opcionales, para pruebas, pues la verdadera salida es el sonido que sale por la bocina. Parametros usados: samp_rate (Hz) - es la frecuencia de muestreo de la senal que recibe nuestro bloque; Fc (Hz) - es la frecuencia de la portadora; Gain Value - es la ganancia en dB del amplificador interno; B (Hz) ancho de banda del canal pasobandas.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_upconverter_cf import b_upconverter_cf  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
import math
import threading







class b_sound_USRP_Sink(gr.hier_block2):
    def __init__(self, B=2000, Fc=4000, Gain_dB=0., samp_rate=2000):
        gr.hier_block2.__init__(
            self, "b_sound_USRP_Sink",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_float*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.B = B
        self.Fc = Fc
        self.Gain_dB = Gain_dB
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_passband = samp_rate_passband = 44100
        self.Gain_volts = Gain_volts = math.pow(10,Gain_dB/20.)
        self.BW = BW = B/2

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_passband,
                decimation=samp_rate,
                taps=[],
                fractional_bw=0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate_passband,
                BW,
                (BW/16.),
                window.WIN_HAMMING,
                6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Gain_volts)
        self.b_upconverter_cf_0 = b_upconverter_cf(
            Fc=Fc,
            samp_rate=samp_rate_passband,
        )
        self.audio_sink_0 = audio.sink(samp_rate_passband, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_upconverter_cf_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))
        self.connect((self.low_pass_filter_0, 0), (self.b_upconverter_cf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self, 1))
        self.connect((self, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))


    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.set_BW(self.B/2)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_upconverter_cf_0.set_Fc(self.Fc)

    def get_Gain_dB(self):
        return self.Gain_dB

    def set_Gain_dB(self, Gain_dB):
        self.Gain_dB = Gain_dB
        self.set_Gain_volts(math.pow(10,self.Gain_dB/20.))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_samp_rate_passband(self):
        return self.samp_rate_passband

    def set_samp_rate_passband(self, samp_rate_passband):
        self.samp_rate_passband = samp_rate_passband
        self.b_upconverter_cf_0.set_samp_rate(self.samp_rate_passband)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_passband, self.BW, (self.BW/16.), window.WIN_HAMMING, 6.76))

    def get_Gain_volts(self):
        return self.Gain_volts

    def set_Gain_volts(self, Gain_volts):
        self.Gain_volts = Gain_volts
        self.blocks_multiply_const_vxx_0.set_k(self.Gain_volts)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate_passband, self.BW, (self.BW/16.), window.WIN_HAMMING, 6.76))

