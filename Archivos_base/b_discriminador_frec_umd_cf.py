# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_discriminador_frec_umd_cf
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Se refierea al Discriminador de frecuencias documentado en: https://user.eng.umd.edu/~tretter/commlab/c6713slides/ch8.pdf, pag 14
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_derivador_ff import b_derivador_ff  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import math
import threading







class b_discriminador_frec_umd_cf(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_discriminador_frec_umd_cf",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Blocks
        ##################################################

        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.b_derivador_ff_0_0 = b_derivador_ff(
            F_muestreo=1,
        )
        self.b_derivador_ff_0 = b_derivador_ff(
            F_muestreo=1,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_derivador_ff_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.b_derivador_ff_0_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.b_derivador_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.b_derivador_ff_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_divide_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_sub_xx_1, 1))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_sub_xx_1, 0))
        self.connect((self.blocks_sub_xx_1, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self, 0), (self.blocks_complex_to_mag_squared_0, 0))


