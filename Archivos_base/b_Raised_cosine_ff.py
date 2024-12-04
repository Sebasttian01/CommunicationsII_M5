# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Raised_cosine_ff
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander.
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: It is the float type version of the Raised Cosine Filter. Usually gnuradio comes with the square root variant, but this is the right one . You can introduce the rolloff factor (rolloff), the number of samples you want the filter produce at the output per each input symbol (sps) and of course, the number of components to take into account in the impulse response of the filter (ntaps)
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import threading







class b_Raised_cosine_ff(gr.hier_block2):
    def __init__(self, ntaps=16, rolloff=1, samp_rate=1000, sps=8):
        gr.hier_block2.__init__(
            self, "b_Raised_cosine_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
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

        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                2,
                samp_rate,
                (samp_rate/sps),
                rolloff,
                ntaps))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_fff(
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

