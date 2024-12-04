# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_M_PAM_bb
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Es un modulador M-PAM. La entrada y la salida es de tipo Byte, pero en la entrada lo que se esperan son unos y ceros, osea que la entrada es una senal PCM.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import b_M_PAM_bb_e_bipol_to_unip as e_bipol_to_unip  # embedded python block
import math
import threading







class b_M_PAM_bb(gr.hier_block2):
    def __init__(self, M=4):
        gr.hier_block2.__init__(
            self, "b_M_PAM_bb",
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
        self.Nbps = Nbps = 8
        self.Bps = Bps = int(math.log(M,2))

        ##################################################
        # Blocks
        ##################################################

        self.e_bipol_to_unip = e_bipol_to_unip.blk()
        self.blocks_packed_to_unpacked_xx_0_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(Nbps)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0_0, 0), (self, 0))
        self.connect((self.e_bipol_to_unip, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self, 0), (self.e_bipol_to_unip, 0))


    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_Nbps(self):
        return self.Nbps

    def set_Nbps(self, Nbps):
        self.Nbps = Nbps

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps

