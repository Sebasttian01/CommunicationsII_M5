# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_meter_power_ff
# Author: Homero Ortega
# Description: Mide potencia promedio en watts y en dB a senales reales. Tambien el Valor RMS. G_prom: es la ganancia para el filtro promediador, entre mas pequeno sea este valor, el promediado es de mas largo plazo y por tanto, el valor es mas estable
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_meter_power_ff(gr.hier_block2):
    def __init__(self, G_prom=0.0001):
        gr.hier_block2.__init__(
            self, "b_meter_power_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature.makev(3, 3, [gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.G_prom = G_prom

        ##################################################
        # Blocks
        ##################################################

        self.blocks_rms_xx_0 = blocks.rms_ff(G_prom)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(20, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self, 1))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self, 2))
        self.connect((self, 0), (self.blocks_rms_xx_0, 0))


    def get_G_prom(self):
        return self.G_prom

    def set_G_prom(self, G_prom):
        self.G_prom = G_prom
        self.blocks_rms_xx_0.set_alpha(self.G_prom)

