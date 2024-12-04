# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_fsk_fc
# Author: Andres Carrillo
# Copyright: b_FDM_Monousuario
# Description: produce senal FSK bandabase
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import threading







class b_fsk_fc(gr.hier_block2):
    def __init__(self, BW=0, Sps=8, f0=0, samp_rate=4800):
        gr.hier_block2.__init__(
            self, "b_fsk_fc",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.BW = BW
        self.Sps = Sps
        self.f0 = f0
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                BW,
                (BW/8.),
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_fff(Sps, Sps*[1.,] )
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f0, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/8.), window.WIN_HAMMING, 6.76))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.interp_fir_filter_xxx_0_0_0.set_taps(self.Sps*[1.,] )

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.analog_sig_source_x_0.set_frequency(self.f0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/8.), window.WIN_HAMMING, 6.76))

