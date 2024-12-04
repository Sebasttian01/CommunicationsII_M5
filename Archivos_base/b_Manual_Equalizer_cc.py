# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Manual_Equalizer_cc
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from scipy import fftpack
import threading







class b_Manual_Equalizer_cc(gr.hier_block2):
    def __init__(self, taps=[1,1,1,1,1,1,1,1]):
        gr.hier_block2.__init__(
            self, "b_Manual_Equalizer_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.taps = taps

        ##################################################
        # Variables
        ##################################################
        self.eq_gain = eq_gain = 0.01
        self.Eq_taps = Eq_taps = fftpack.ifftshift(fftpack.ifft([taps[0], taps[1], taps[2], taps[3], taps[4], taps[5], taps[6], taps[7]]))

        ##################################################
        # Blocks
        ##################################################

        self.channels_channel_model_0_0 = channels.channel_model(
            noise_voltage=0,
            frequency_offset=0,
            epsilon=1.,
            taps=Eq_taps,
            noise_seed=13,
            block_tags=False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.channels_channel_model_0_0, 0), (self, 0))
        self.connect((self, 0), (self.channels_channel_model_0_0, 0))


    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.set_Eq_taps(fftpack.ifftshift(fftpack.ifft([self.taps[0], self.taps[1], self.taps[2], self.taps[3], self.taps[4], self.taps[5], self.taps[6], self.taps[7]])))

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain

    def get_Eq_taps(self):
        return self.Eq_taps

    def set_Eq_taps(self, Eq_taps):
        self.Eq_taps = Eq_taps
        self.channels_channel_model_0_0.set_taps(self.Eq_taps)

