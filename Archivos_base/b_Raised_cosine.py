# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Raised_cosine_cc
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: It is the Raised Cosine Filter. Usually gnuradio comes with the square root variant, but this is the right one. Parameters: rolloff - is the rolloff factor or Exccess Bandwidth;  sps - the number of samples per simbol the filter will produce. Note that at the input must be only one sample per simbol; ntaps - the number of components of the Impulse response to take into account; samp_rate - the sample rate at the output
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import threading







class b_Raised_cosine(gr.hier_block2):
    def __init__(self, ntaps=16, rolloff=1, samp_rate=1000, sps=8):
        gr.hier_block2.__init__(
            self, "b_Raised_cosine_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.ntaps = ntaps
        self.rolloff = rolloff
        self.samp_rate = samp_rate
        self.sps = sps

        ##################################################
        # Blocks
        ##################################################

        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                2,
                samp_rate,
                (samp_rate/sps),
                rolloff,
                ntaps))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(
            sps,
            firdes.root_raised_cosine(
                2,
                samp_rate,
                (samp_rate/sps),
                rolloff,
                ntaps))


        ##################################################
        # Connections
        ##################################################
        self.connect((self, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self, 0))


    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.rolloff, self.ntaps))

