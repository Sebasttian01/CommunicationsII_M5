# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_binary_bipolar_source1_f
# Author: Homero Ortega Boada. Universidad Industrial de Santader
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Genera una senal binaria bipolar aleatoria tipo float. Parametros usados: Spb (Samples per bit), es para cuando desees que la senal binaria aparezca en forma discreta con un determinado numero de muestras en cada bit
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_binary_bipolar_source1_f(gr.hier_block2):
    def __init__(self, Am=1.):
        gr.hier_block2.__init__(
            self, "b_binary_bipolar_source1_f",
                gr.io_signature(0, 0, 0),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Am = Am

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Am)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1.)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))


    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.blocks_multiply_const_vxx_0.set_k(self.Am)

