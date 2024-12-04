# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: USRP_Tx_simulator_cf
# Author: Homero Ortega Boada
# Copyright: RadioGis UIS
# Description: recibe una senal Envolvente Compleja con frec de muestreo samp_rate, realiza una operacion similar a DAC elevando DAC_resamp_factor veces la frec de muestreo y luego convierte la senal a pasobandas con una portadores de Fc Hertz. Si ve que la portadora no está bien definida, eleve DAC_resamp_factor (para senales digitales, se aconseja DAC_resamp_factor=Sps)
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_upconverter_cf import b_upconverter_cf  # grc-generated hier_block
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
import threading







class USRP_Tx_simulator_cf(gr.hier_block2):
    def __init__(self, Fc=64000, K=8, samp_rate=32000):
        gr.hier_block2.__init__(
            self, "USRP_Tx_simulator_cf",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Fc = Fc
        self.K = K
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=K,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.b_upconverter_cf_0 = b_upconverter_cf(
            Fc=Fc,
            samp_rate=samp_rate*K,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_upconverter_cf_0, 0), (self, 0))
        self.connect((self, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.b_upconverter_cf_0, 0))


    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_upconverter_cf_0.set_Fc(self.Fc)

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.b_upconverter_cf_0.set_samp_rate(self.samp_rate*self.K)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_upconverter_cf_0.set_samp_rate(self.samp_rate*self.K)

