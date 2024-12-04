# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Gray_Encoder_BB
# Author: Homero Ortega
# Description: apply Gray coding to input byte signal
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_Gray_Encoder_BB(gr.hier_block2):
    def __init__(self, M=8):
        gr.hier_block2.__init__(
            self, "b_Gray_Encoder_BB",
                gr.io_signature(1, 1, gr.sizeof_char*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.M = M

        ##################################################
        # Variables
        ##################################################
        self.cod_gray = cod_gray = digital.utils.gray_code.gray_code(M)
        self.cod_gray_inv = cod_gray_inv = digital.mod_codes.invert_code(cod_gray)

        ##################################################
        # Blocks
        ##################################################

        self.digital_map_bb_0 = digital.map_bb(cod_gray)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_map_bb_0, 0), (self, 0))
        self.connect((self, 0), (self.digital_map_bb_0, 0))


    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_cod_gray(digital.utils.gray_code.gray_code(self.M))

    def get_cod_gray(self):
        return self.cod_gray

    def set_cod_gray(self, cod_gray):
        self.cod_gray = cod_gray
        self.set_cod_gray_inv(digital.mod_codes.invert_code(self.cod_gray))

    def get_cod_gray_inv(self):
        return self.cod_gray_inv

    def set_cod_gray_inv(self, cod_gray_inv):
        self.cod_gray_inv = cod_gray_inv

