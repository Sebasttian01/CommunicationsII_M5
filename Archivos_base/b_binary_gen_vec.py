# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_binary_vect_source_f
# Author: Homero Ortega Boada. Universidad Industrial de Santader
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: This is a binary vector generator. Its is useful to produce a paquet of bits that generates repeatly. The paquet of bits corresponds to the binary version of the parameter Vector. Examples for the parameter Vector are:   [100]  or  [101, 54, 12]. What the block does is to traslate the values of the vector to bits and then to type float
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_binary_gen_vec(gr.hier_block2):
    def __init__(self, Vector=0):
        gr.hier_block2.__init__(
            self, "b_binary_vect_source_f",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Vector = Vector

        ##################################################
        # Blocks
        ##################################################

        self.blocks_vector_source_x_0 = blocks.vector_source_b(Vector, True, 1, [])
        self.blocks_unpack_k_bits_bb_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0, 0), (self.blocks_char_to_float_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_unpack_k_bits_bb_0_0, 0))


    def get_Vector(self):
        return self.Vector

    def set_Vector(self, Vector):
        self.Vector = Vector
        self.blocks_vector_source_x_0.set_data(self.Vector, [])

