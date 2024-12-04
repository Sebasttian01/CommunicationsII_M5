# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_USRP_Sourc_simul_f
# Author: Homoero Ortega Boada
# Copyright: Grupo RadioGis Universidad Industrial de Santander
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







class b_USRP_Sourc_simul_f(gr.hier_block2):
    def __init__(self, Bandwidth=0, Center_Freq=50000000, Gain_Value_dB=0, samp_rate=200000, samp_rate_rf=(50000000+200000)):
        gr.hier_block2.__init__(
            self, "b_USRP_Sourc_simul_f",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Bandwidth = Bandwidth
        self.Center_Freq = Center_Freq
        self.Gain_Value_dB = Gain_Value_dB
        self.samp_rate = samp_rate
        self.samp_rate_rf = samp_rate_rf

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=samp_rate_rf,
                taps=[],
                fractional_bw=0)
        self.b_downconverter_fc_0 = b_downconverter_fc(
            BW=samp_rate/2,
            Fc=Center_Freq,
            samp_rate=samp_rate_rf,
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

    def get_Center_Freq(self):
        return self.Center_Freq

    def set_Center_Freq(self, Center_Freq):
        self.Center_Freq = Center_Freq
        self.b_downconverter_fc_0.set_Fc(self.Center_Freq)

    def get_Gain_Value_dB(self):
        return self.Gain_Value_dB

    def set_Gain_Value_dB(self, Gain_Value_dB):
        self.Gain_Value_dB = Gain_Value_dB

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_downconverter_fc_0.set_BW(self.samp_rate/2)

    def get_samp_rate_rf(self):
        return self.samp_rate_rf

    def set_samp_rate_rf(self, samp_rate_rf):
        self.samp_rate_rf = samp_rate_rf
        self.b_downconverter_fc_0.set_samp_rate(self.samp_rate_rf)

