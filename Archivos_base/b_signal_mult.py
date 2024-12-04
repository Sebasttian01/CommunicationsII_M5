# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_signal_mult
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: multiplica la entrada por una senoidal compleja, con los siguientes parametros: samp_rate: frecuencia de muesteo en Hz; f: frecuencia de la senoidad en Hz
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_signal_mult(gr.hier_block2):
    def __init__(self, f=8, samp_rate=32e3):
        gr.hier_block2.__init__(
            self, "b_signal_mult",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.f = f
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, f, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 1))


    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.analog_sig_source_x_0.set_frequency(self.f)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

