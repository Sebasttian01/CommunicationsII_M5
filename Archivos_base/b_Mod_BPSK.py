# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Mod_BPSK_Zeroh
# Author: Homero Ortega Boada. Universidad industrial de Santander
# Description: Entrega una senal BPSK lista para ser entregada a un USRP, pero usando un zero order hold (osea que no usa filtro coseno alzado). Le entrada son unos o ceros tipo float
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_Mod_BPSK(gr.hier_block2):
    def __init__(self, Sps=8):
        gr.hier_block2.__init__(
            self, "b_Mod_BPSK_Zeroh",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(Sps)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))


    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.Sps)

