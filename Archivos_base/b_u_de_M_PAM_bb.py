# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_u_de_M_PAM_bb
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Es el demodulador que hace juego con el b_u_M_PAM_bb. La salida es una senal binaria (PCM) pero de tipo Byte (osea, unos y ceros en formato Byte). Parametros usados: M- es el orden de la modulacion M-PAM.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import math
import threading







class b_u_de_M_PAM_bb(gr.hier_block2):
    def __init__(self, M=4):
        gr.hier_block2.__init__(
            self, "b_u_de_M_PAM_bb",
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

        self.blocks_unpacked_to_packed_xx_0_1 = blocks.unpacked_to_packed_bb(Bps, gr.GR_MSB_FIRST)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(Nbps)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_1, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self, 0), (self.blocks_unpacked_to_packed_xx_0_1, 0))


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

