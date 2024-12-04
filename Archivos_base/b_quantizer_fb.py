# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_quantizer_fb
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Este es un cuantificador que recibe una senal tipo float, la cuantifica y entrega a tipo byte  (que es lo mismo que char en c++).  Funciona bien para cualquier niveles de cuantificacion que este en el rango del tipo Byte. Así, para el tipo Byte el maximo nivel de cuantizacion es 256 (osea 2^8).  Los parametros usados: Vmax: es el valor maximo de amplitud que puede llegar a alcanzar la senal entrante, bien sea en el rango de los valores negativos o en los positivos, pero aqui se registra ese valor sin signo, osea como un valor positivo o valor absoluto ; NivelesQ - es el numero de niveles de cuantificacion a usar en todo el rango dinamico de la senal
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_quantizer_fb(gr.hier_block2):
    def __init__(self, NivelesQ=256, Vmax=.5):
        gr.hier_block2.__init__(
            self, "b_quantizer_fb",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.NivelesQ = NivelesQ
        self.Vmax = Vmax

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(((NivelesQ/2.)/Vmax))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_char_0, 0), (self, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_NivelesQ(self):
        return self.NivelesQ

    def set_NivelesQ(self, NivelesQ):
        self.NivelesQ = NivelesQ
        self.blocks_multiply_const_vxx_0.set_k(((self.NivelesQ/2.)/self.Vmax))

    def get_Vmax(self):
        return self.Vmax

    def set_Vmax(self, Vmax):
        self.Vmax = Vmax
        self.blocks_multiply_const_vxx_0.set_k(((self.NivelesQ/2.)/self.Vmax))

