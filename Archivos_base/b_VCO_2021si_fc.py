# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_VCO_2021si_fc
# Author: estudiantes e3t
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import b_VCO_2021si_fc_epy_block_0 as epy_block_0  # embedded python block
import math
import threading







class b_VCO_2021si_fc(gr.hier_block2):
    def __init__(self, Sps=8, samp_rate=32000):
        gr.hier_block2.__init__(
            self, "b_VCO_2021si_fc",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Sps = Sps
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.epy_block_0 = epy_block_0.blk()
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff((math.pi*2/samp_rate))
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.E3TRadio_acumulador_truncado_ff_0 = E3TRadio.acumulador_truncado_ff(Sps,0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_acumulador_truncado_ff_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.epy_block_0, 1))
        self.connect((self.epy_block_0, 0), (self, 0))
        self.connect((self, 0), (self.E3TRadio_acumulador_truncado_ff_0, 0))


    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_multiply_const_vxx_0_0.set_k((math.pi*2/self.samp_rate))

