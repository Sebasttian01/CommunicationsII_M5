# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_quantizer_fx
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Este es un cuantificaador que recibe una senal tipo float, la cuantifica y entrega en 4 posibles tipos de salida (Byte, short, int  o float).  Funciona bien para cualquier niveles de cuantificacion que este en el rango del tipo de salida de su interes. Por ejemplo, si va a usar la salida tipo Byte, el maximo nivel de cuantizacion es 256 (osea 2^8), si es la tipo short, ese valor es 65536 (osea 2^16), si es tipo int, se supone que ese valor es 2^32. El tipo float lo usamos mas que todo para poder visualizar la senal cuantificada directamente en un osciloscopio.  Los parametros usados: Vmax: es el valor maximo de amplitud que puede llegar a alcanzar la senal entrante, bien sea en el rango de los valores negativos o en los positivos, pero aqui se registra ese valor sin signo, osea como un valor positivo o valor absoluto ; NivelesQ - es el numero de niveles de cuantificacion a usar en todo el rango dinamico de la senal
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_quantizer_fx(gr.hier_block2):
    def __init__(self, NivelesQ=256, Vmax=.5):
        gr.hier_block2.__init__(
            self, "b_quantizer_fx",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature.makev(4, 4, [gr.sizeof_short*1, gr.sizeof_float*1, gr.sizeof_int*1, gr.sizeof_char*1]),
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
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_int_0 = blocks.float_to_int(1, 1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_char_0, 0), (self, 3))
        self.connect((self.blocks_float_to_int_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_float_to_int_0, 0), (self, 2))
        self.connect((self.blocks_float_to_short_0, 0), (self, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_int_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))
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

