# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_discriminador_frec_cf
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Se refierea al Discriminador de frecuencias que en el libro de Haykin, capitulo 2.7 esta representado como H1(f). BW es el ancho de banda de la senal entrante.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_derivador_cc import b_derivador_cc  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import math
import threading







class b_discriminador_frec_cf(gr.hier_block2):
    def __init__(self, BW=1000):
        gr.hier_block2.__init__(
            self, "b_discriminador_frec_cf",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.BW = BW

        ##################################################
        # Variables
        ##################################################
        self.pendiente = pendiente = 1.

        ##################################################
        # Blocks
        ##################################################

        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_cc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_cc(pendiente)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(pendiente)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_derivador_cc_0_0 = b_derivador_cc(
            F_muestreo=1.,
        )
        self.b_derivador_cc_0 = b_derivador_cc(
            F_muestreo=1.,
        )
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, BW*2*math.pi*1.j)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.b_derivador_cc_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.b_derivador_cc_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self, 0))
        self.connect((self, 0), (self.b_derivador_cc_0, 0))
        self.connect((self, 0), (self.b_derivador_cc_0_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))


    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.analog_const_source_x_0.set_offset(self.BW*2*math.pi*1.j)

    def get_pendiente(self):
        return self.pendiente

    def set_pendiente(self, pendiente):
        self.pendiente = pendiente
        self.blocks_multiply_const_vxx_0.set_k(self.pendiente)
        self.blocks_multiply_const_vxx_0_1.set_k(self.pendiente)

