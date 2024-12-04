# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_ds_spreadspect_ff
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: multiplica la entrada por codigo para producir una senal en Direc Sequence Spread Spectrum (DSSS) para una entrada y salida flotante. El cuidado que hay que tener es que el Spreading Factor (SF) se cuadra desde afuera, para la cual la senal de la informacion debe entrar con un sobremuestreo SF. Los parametros usados son: codigo - es el codigo que se usara para producir la senal DSSS; retardo (muestras) es para tener en cuenta que la senal entrante puede estar llegando con un retardo, el cual debe ser compensado con un retardo en la entrada del codigo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_ds_spreadspect_ff(gr.hier_block2):
    def __init__(self, codigo=(1,1,1,1,1,1,1,1), retardo=0):
        gr.hier_block2.__init__(
            self, "b_ds_spreadspect_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.codigo = codigo
        self.retardo = retardo

        ##################################################
        # Blocks
        ##################################################

        self.blocks_vector_source_x_0 = blocks.vector_source_f(codigo, True, 1, [])
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, retardo)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 1))


    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
        self.blocks_vector_source_x_0.set_data(self.codigo, [])

    def get_retardo(self):
        return self.retardo

    def set_retardo(self, retardo):
        self.retardo = retardo
        self.blocks_delay_0.set_dly(int(self.retardo))

