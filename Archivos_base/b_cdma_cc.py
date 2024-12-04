# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_cdma
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_ds_spreadspect_cc import b_ds_spreadspect_cc  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import cmath
import math
import numpy
import threading







class b_cdma_cc(gr.hier_block2):
    def __init__(self, SF=8, c0=(0+0j,0+0j,0+0j), c1=(0+0j,0+0j,0+0j), c2=(0+0j,0+0j,0+0j), c3=(0+0j,0+0j,0+0j), c4=(0+0j,0+0j,0+0j), c5=(0+0j,0+0j,0+0j), c6=(0+0j,0+0j,0+0j), c7=(0+0j,0+0j,0+0j)):
        gr.hier_block2.__init__(
            self, "b_cdma",
                gr.io_signature.makev(8, 8, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.SF = SF
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5
        self.c6 = c6
        self.c7 = c7

        ##################################################
        # Variables
        ##################################################
        self.N = N = 8

        ##################################################
        # Blocks
        ##################################################

        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_ds_spreadspect_cc_0_0_5 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c7,
        )
        self.b_ds_spreadspect_cc_0_0_4 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c6,
        )
        self.b_ds_spreadspect_cc_0_0_3 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c5,
        )
        self.b_ds_spreadspect_cc_0_0_2 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c4,
        )
        self.b_ds_spreadspect_cc_0_0_1 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c3,
        )
        self.b_ds_spreadspect_cc_0_0_0 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c2,
        )
        self.b_ds_spreadspect_cc_0_0 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c1,
        )
        self.b_ds_spreadspect_cc_0 = b_ds_spreadspect_cc(
            SF=8,
            codigo=c0,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_ds_spreadspect_cc_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.b_ds_spreadspect_cc_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.b_ds_spreadspect_cc_0_0, 2), (self, 0))
        self.connect((self.b_ds_spreadspect_cc_0_0, 1), (self, 2))
        self.connect((self.b_ds_spreadspect_cc_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.b_ds_spreadspect_cc_0_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.b_ds_spreadspect_cc_0_0_2, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.b_ds_spreadspect_cc_0_0_3, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.b_ds_spreadspect_cc_0_0_4, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.b_ds_spreadspect_cc_0_0_5, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_add_xx_0, 0), (self, 1))
        self.connect((self, 0), (self.b_ds_spreadspect_cc_0, 0))
        self.connect((self, 1), (self.b_ds_spreadspect_cc_0_0, 0))
        self.connect((self, 2), (self.b_ds_spreadspect_cc_0_0_0, 0))
        self.connect((self, 3), (self.b_ds_spreadspect_cc_0_0_1, 0))
        self.connect((self, 4), (self.b_ds_spreadspect_cc_0_0_2, 0))
        self.connect((self, 5), (self.b_ds_spreadspect_cc_0_0_3, 0))
        self.connect((self, 6), (self.b_ds_spreadspect_cc_0_0_4, 0))
        self.connect((self, 7), (self.b_ds_spreadspect_cc_0_0_5, 0))


    def get_SF(self):
        return self.SF

    def set_SF(self, SF):
        self.SF = SF

    def get_c0(self):
        return self.c0

    def set_c0(self, c0):
        self.c0 = c0
        self.b_ds_spreadspect_cc_0.set_codigo(self.c0)

    def get_c1(self):
        return self.c1

    def set_c1(self, c1):
        self.c1 = c1
        self.b_ds_spreadspect_cc_0_0.set_codigo(self.c1)

    def get_c2(self):
        return self.c2

    def set_c2(self, c2):
        self.c2 = c2
        self.b_ds_spreadspect_cc_0_0_0.set_codigo(self.c2)

    def get_c3(self):
        return self.c3

    def set_c3(self, c3):
        self.c3 = c3
        self.b_ds_spreadspect_cc_0_0_1.set_codigo(self.c3)

    def get_c4(self):
        return self.c4

    def set_c4(self, c4):
        self.c4 = c4
        self.b_ds_spreadspect_cc_0_0_2.set_codigo(self.c4)

    def get_c5(self):
        return self.c5

    def set_c5(self, c5):
        self.c5 = c5
        self.b_ds_spreadspect_cc_0_0_3.set_codigo(self.c5)

    def get_c6(self):
        return self.c6

    def set_c6(self, c6):
        self.c6 = c6
        self.b_ds_spreadspect_cc_0_0_4.set_codigo(self.c6)

    def get_c7(self):
        return self.c7

    def set_c7(self, c7):
        self.c7 = c7
        self.b_ds_spreadspect_cc_0_0_5.set_codigo(self.c7)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

