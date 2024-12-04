# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: USRP_Rx_simulator_cf
# Author: Homero Ortega Boada
# Copyright: RadioGis UIS
# Description: Recibe una senal pasobandas con frec de portadora Fc y con frec de muestreo samp_rate_in, la convierte Envolvente Compleja y hace una operacion similar a ADC, simplmente decimando la senal ADC_samp_factor veces
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_downconverter_fc import b_downconverter_fc  # grc-generated hier_block
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
import threading







class USRP_Rx_simulator_cf(gr.hier_block2):
    def __init__(self, Bandwidth=16000, Fc=64000, K=8, samp_rate_in=32000):
        gr.hier_block2.__init__(
            self, "USRP_Rx_simulator_cf",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Bandwidth = Bandwidth
        self.Fc = Fc
        self.K = K
        self.samp_rate_in = samp_rate_in

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = samp_rate_in/K

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=K,
                taps=[],
                fractional_bw=0)
        self.b_downconverter_fc_0 = b_downconverter_fc(
            BW=Bandwidth,
            Fc=Fc,
            samp_rate=samp_rate_in,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_downconverter_fc_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self, 0), (self.b_downconverter_fc_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self, 0))


    def get_Bandwidth(self):
        return self.Bandwidth

    def set_Bandwidth(self, Bandwidth):
        self.Bandwidth = Bandwidth
        self.b_downconverter_fc_0.set_BW(self.Bandwidth)

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.b_downconverter_fc_0.set_Fc(self.Fc)

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.set_samp_rate(self.samp_rate_in/self.K)

    def get_samp_rate_in(self):
        return self.samp_rate_in

    def set_samp_rate_in(self, samp_rate_in):
        self.samp_rate_in = samp_rate_in
        self.set_samp_rate(self.samp_rate_in/self.K)
        self.b_downconverter_fc_0.set_samp_rate(self.samp_rate_in)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

