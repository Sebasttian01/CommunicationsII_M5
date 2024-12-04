# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_de_cdma_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_de_ds_spreadspect_cc import b_de_ds_spreadspect_cc  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import threading







class b_de_cdma_cc(gr.hier_block2):
    def __init__(self, ChipsSysDelay=0, SF=8, c0=(0+0j,0+0j,0+0j), c1=(0+0j,0+0j,0+0j), c2=(0+0j,0+0j,0+0j), c3=(0+0j,0+0j,0+0j), c4=(0+0j,0+0j,0+0j), c5=(0+0j,0+0j,0+0j), c6=(0+0j,0+0j,0+0j), c7=(0+0j,0+0j,0+0j)):
        gr.hier_block2.__init__(
            self, "b_de_cdma_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(12, 12, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.ChipsSysDelay = ChipsSysDelay
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
        self.g = g = 8

        ##################################################
        # Blocks
        ##################################################

        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.b_de_ds_spreadspect_cc_0_7 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c2,
        )
        self.b_de_ds_spreadspect_cc_0_6 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c3,
        )
        self.b_de_ds_spreadspect_cc_0_5 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c4,
        )
        self.b_de_ds_spreadspect_cc_0_4 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c5,
        )
        self.b_de_ds_spreadspect_cc_0_3 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c6,
        )
        self.b_de_ds_spreadspect_cc_0_2 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c7,
        )
        self.b_de_ds_spreadspect_cc_0_0 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c1,
        )
        self.b_de_ds_spreadspect_cc_0 = b_de_ds_spreadspect_cc(
            ChipsSysDelay=ChipsSysDelay,
            SF=SF,
            codigo=c0,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_de_ds_spreadspect_cc_0, 1), (self.blocks_null_sink_0, 3))
        self.connect((self.b_de_ds_spreadspect_cc_0, 3), (self.blocks_null_sink_0, 1))
        self.connect((self.b_de_ds_spreadspect_cc_0, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.b_de_ds_spreadspect_cc_0, 0), (self.blocks_null_sink_0, 2))
        self.connect((self.b_de_ds_spreadspect_cc_0, 4), (self, 0))
        self.connect((self.b_de_ds_spreadspect_cc_0_0, 4), (self, 1))
        self.connect((self.b_de_ds_spreadspect_cc_0_0, 2), (self, 8))
        self.connect((self.b_de_ds_spreadspect_cc_0_0, 0), (self, 9))
        self.connect((self.b_de_ds_spreadspect_cc_0_0, 3), (self, 10))
        self.connect((self.b_de_ds_spreadspect_cc_0_0, 1), (self, 11))
        self.connect((self.b_de_ds_spreadspect_cc_0_2, 1), (self.blocks_null_sink_1, 15))
        self.connect((self.b_de_ds_spreadspect_cc_0_2, 0), (self.blocks_null_sink_1, 14))
        self.connect((self.b_de_ds_spreadspect_cc_0_2, 2), (self.blocks_null_sink_1, 12))
        self.connect((self.b_de_ds_spreadspect_cc_0_2, 3), (self.blocks_null_sink_1, 13))
        self.connect((self.b_de_ds_spreadspect_cc_0_2, 4), (self, 7))
        self.connect((self.b_de_ds_spreadspect_cc_0_3, 3), (self.blocks_null_sink_1, 9))
        self.connect((self.b_de_ds_spreadspect_cc_0_3, 0), (self.blocks_null_sink_1, 10))
        self.connect((self.b_de_ds_spreadspect_cc_0_3, 1), (self.blocks_null_sink_1, 11))
        self.connect((self.b_de_ds_spreadspect_cc_0_3, 2), (self.blocks_null_sink_1, 8))
        self.connect((self.b_de_ds_spreadspect_cc_0_3, 4), (self, 6))
        self.connect((self.b_de_ds_spreadspect_cc_0_4, 1), (self.blocks_null_sink_1, 7))
        self.connect((self.b_de_ds_spreadspect_cc_0_4, 2), (self.blocks_null_sink_1, 4))
        self.connect((self.b_de_ds_spreadspect_cc_0_4, 3), (self.blocks_null_sink_1, 5))
        self.connect((self.b_de_ds_spreadspect_cc_0_4, 0), (self.blocks_null_sink_1, 6))
        self.connect((self.b_de_ds_spreadspect_cc_0_4, 4), (self, 5))
        self.connect((self.b_de_ds_spreadspect_cc_0_5, 1), (self.blocks_null_sink_1, 3))
        self.connect((self.b_de_ds_spreadspect_cc_0_5, 2), (self.blocks_null_sink_1, 0))
        self.connect((self.b_de_ds_spreadspect_cc_0_5, 0), (self.blocks_null_sink_1, 2))
        self.connect((self.b_de_ds_spreadspect_cc_0_5, 3), (self.blocks_null_sink_1, 1))
        self.connect((self.b_de_ds_spreadspect_cc_0_5, 4), (self, 4))
        self.connect((self.b_de_ds_spreadspect_cc_0_6, 1), (self.blocks_null_sink_0, 11))
        self.connect((self.b_de_ds_spreadspect_cc_0_6, 2), (self.blocks_null_sink_0, 8))
        self.connect((self.b_de_ds_spreadspect_cc_0_6, 3), (self.blocks_null_sink_0, 9))
        self.connect((self.b_de_ds_spreadspect_cc_0_6, 0), (self.blocks_null_sink_0, 10))
        self.connect((self.b_de_ds_spreadspect_cc_0_6, 4), (self, 3))
        self.connect((self.b_de_ds_spreadspect_cc_0_7, 2), (self.blocks_null_sink_0, 4))
        self.connect((self.b_de_ds_spreadspect_cc_0_7, 0), (self.blocks_null_sink_0, 6))
        self.connect((self.b_de_ds_spreadspect_cc_0_7, 1), (self.blocks_null_sink_0, 7))
        self.connect((self.b_de_ds_spreadspect_cc_0_7, 3), (self.blocks_null_sink_0, 5))
        self.connect((self.b_de_ds_spreadspect_cc_0_7, 4), (self, 2))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_0, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_2, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_3, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_4, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_5, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_6, 0))
        self.connect((self, 0), (self.b_de_ds_spreadspect_cc_0_7, 0))


    def get_ChipsSysDelay(self):
        return self.ChipsSysDelay

    def set_ChipsSysDelay(self, ChipsSysDelay):
        self.ChipsSysDelay = ChipsSysDelay
        self.b_de_ds_spreadspect_cc_0.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_0.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_2.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_3.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_4.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_5.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_6.set_ChipsSysDelay(self.ChipsSysDelay)
        self.b_de_ds_spreadspect_cc_0_7.set_ChipsSysDelay(self.ChipsSysDelay)

    def get_SF(self):
        return self.SF

    def set_SF(self, SF):
        self.SF = SF
        self.b_de_ds_spreadspect_cc_0.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_0.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_2.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_3.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_4.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_5.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_6.set_SF(self.SF)
        self.b_de_ds_spreadspect_cc_0_7.set_SF(self.SF)

    def get_c0(self):
        return self.c0

    def set_c0(self, c0):
        self.c0 = c0
        self.b_de_ds_spreadspect_cc_0.set_codigo(self.c0)

    def get_c1(self):
        return self.c1

    def set_c1(self, c1):
        self.c1 = c1
        self.b_de_ds_spreadspect_cc_0_0.set_codigo(self.c1)

    def get_c2(self):
        return self.c2

    def set_c2(self, c2):
        self.c2 = c2
        self.b_de_ds_spreadspect_cc_0_7.set_codigo(self.c2)

    def get_c3(self):
        return self.c3

    def set_c3(self, c3):
        self.c3 = c3
        self.b_de_ds_spreadspect_cc_0_6.set_codigo(self.c3)

    def get_c4(self):
        return self.c4

    def set_c4(self, c4):
        self.c4 = c4
        self.b_de_ds_spreadspect_cc_0_5.set_codigo(self.c4)

    def get_c5(self):
        return self.c5

    def set_c5(self, c5):
        self.c5 = c5
        self.b_de_ds_spreadspect_cc_0_4.set_codigo(self.c5)

    def get_c6(self):
        return self.c6

    def set_c6(self, c6):
        self.c6 = c6
        self.b_de_ds_spreadspect_cc_0_3.set_codigo(self.c6)

    def get_c7(self):
        return self.c7

    def set_c7(self, c7):
        self.c7 = c7
        self.b_de_ds_spreadspect_cc_0_2.set_codigo(self.c7)

    def get_g(self):
        return self.g

    def set_g(self, g):
        self.g = g

