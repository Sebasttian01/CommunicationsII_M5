# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_USRP_Sink_simul_f
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Es un simulador del bloque USRP_Sink con el hardware tipo USRP 2920. Entrega una senal pasobandas, con una frecuencia de muestreo que se calcula asi: samp_rate_o=(Center_Freq+samp_rate/2)*8
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







class b_USRP_Sink_simul_f(gr.hier_block2):
    def __init__(self, Bandwidth=0, Center_Freq=50000000, Gain_Value_dB=0, Samp_Rate=200000, tag_name="    "):
        gr.hier_block2.__init__(
            self, "b_USRP_Sink_simul_f",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Bandwidth = Bandwidth
        self.Center_Freq = Center_Freq
        self.Gain_Value_dB = Gain_Value_dB
        self.Samp_Rate = Samp_Rate
        self.tag_name = tag_name

        ##################################################
        # Variables
        ##################################################
        self.Samp_Rate_o = Samp_Rate_o = int((Center_Freq+Samp_Rate/2)*8)

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=Samp_Rate_o,
                decimation=Samp_Rate,
                taps=[],
                fractional_bw=0)
        self.b_upconverter_cf_0 = b_upconverter_cf(
            Fc=Center_Freq,
            samp_rate=Samp_Rate_o,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_upconverter_cf_0, 0), (self, 0))
        self.connect((self, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.b_upconverter_cf_0, 0))


    def get_Bandwidth(self):
        return self.Bandwidth

    def set_Bandwidth(self, Bandwidth):
        self.Bandwidth = Bandwidth

    def get_Center_Freq(self):
        return self.Center_Freq

    def set_Center_Freq(self, Center_Freq):
        self.Center_Freq = Center_Freq
        self.set_Samp_Rate_o(int((self.Center_Freq+self.Samp_Rate/2)*8))
        self.b_upconverter_cf_0.set_Fc(self.Center_Freq)

    def get_Gain_Value_dB(self):
        return self.Gain_Value_dB

    def set_Gain_Value_dB(self, Gain_Value_dB):
        self.Gain_Value_dB = Gain_Value_dB

    def get_Samp_Rate(self):
        return self.Samp_Rate

    def set_Samp_Rate(self, Samp_Rate):
        self.Samp_Rate = Samp_Rate
        self.set_Samp_Rate_o(int((self.Center_Freq+self.Samp_Rate/2)*8))

    def get_tag_name(self):
        return self.tag_name

    def set_tag_name(self, tag_name):
        self.tag_name = tag_name

    def get_Samp_Rate_o(self):
        return self.Samp_Rate_o

    def set_Samp_Rate_o(self, Samp_Rate_o):
        self.Samp_Rate_o = Samp_Rate_o
        self.b_upconverter_cf_0.set_samp_rate(self.Samp_Rate_o)

