# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_ds_spreadspect_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: multiplica la entrada por codigo para producir una senal en Direc Sequence Spread Spectrum (DSSS). El cuidado que hay que tener es que el Spreading Factor (SF) se cuadra desde afuera, para la cual la senal de la informacion debe entrar con un sobremuestreo SF. Los parametros usados son: codigo - es el codigo que se usara para producir la senal DSSS
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_ds_spreadspect_cc(gr.hier_block2):
    def __init__(self, SF=8, codigo=(1,1,1,1,1,1,1,1)):
        gr.hier_block2.__init__(
            self, "b_ds_spreadspect_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.SF = SF
        self.codigo = codigo

        ##################################################
        # Blocks
        ##################################################

        self.blocks_vector_source_x_0 = blocks.vector_source_c(codigo, True, 1, [])
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(SF)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self, 2))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self, 1))
        self.connect((self, 0), (self.E3TRadio_zero_order_hold2_cc_0, 0))


    def get_SF(self):
        return self.SF

    def set_SF(self, SF):
        self.SF = SF
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.SF)

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
        self.blocks_vector_source_x_0.set_data(self.codigo, [])

