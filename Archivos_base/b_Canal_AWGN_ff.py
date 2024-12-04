# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Canal_AWGN_ff
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Este bloque es un simulador de un canal AWGN (Additive White Gaussian Noise). De modo que solo tiene tres características: suma ruido blanco a la señal,  restringe el ancho de banda e Introduce un retardo a la señal. Parametros: Ch_NodB - altura de la PSD del ruido blanco bandabase; samp_rate - frecuencia de muestreo de la señal; BW - ancho de banda bandabase, Ch_Toffset - retardo dado en muestraas que el canal introduce
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_noise_dB_f import b_noise_dB_f  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
import cmath
import math
import numpy
import random
import threading







class b_Canal_AWGN_ff(gr.hier_block2):
    def __init__(self, BW=1000, Ch_NodB=1000, Ch_Toffset=0, samp_rate=1000):
        gr.hier_block2.__init__(
            self, "b_Canal_AWGN_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.BW = BW
        self.Ch_NodB = Ch_NodB
        self.Ch_Toffset = Ch_Toffset
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                BW,
                (BW/16),
                window.WIN_HAMMING,
                6.76))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Ch_Toffset)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_noise_dB_f_0 = b_noise_dB_f(
            NodB=Ch_NodB,
            samp_rate=10000,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_noise_dB_f_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16), window.WIN_HAMMING, 6.76))

    def get_Ch_NodB(self):
        return self.Ch_NodB

    def set_Ch_NodB(self, Ch_NodB):
        self.Ch_NodB = Ch_NodB
        self.b_noise_dB_f_0.set_NodB(self.Ch_NodB)

    def get_Ch_Toffset(self):
        return self.Ch_Toffset

    def set_Ch_Toffset(self, Ch_Toffset):
        self.Ch_Toffset = Ch_Toffset
        self.blocks_delay_0.set_dly(int(self.Ch_Toffset))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16), window.WIN_HAMMING, 6.76))

