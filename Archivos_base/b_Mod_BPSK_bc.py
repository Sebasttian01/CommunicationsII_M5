# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Mod_BPSK_bc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Description: Por cada bit que recibe, produce un simbolo en BPSK bandabase
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_Mod_BPSK_bc(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_Mod_BPSK_bc",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Blocks
        ##################################################

        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_char_to_float_0, 0))


