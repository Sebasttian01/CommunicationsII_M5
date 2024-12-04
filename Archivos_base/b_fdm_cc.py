# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_fdm_cc
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_signal_mult import b_signal_mult  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
import E3TRadio
import math
import threading







class b_fdm_cc(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_fdm_cc",
                gr.io_signature.makev(4, 4, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200e3
        self.N = N = 4
        self.NLobulos = NLobulos = 4
        self.AnchoCanales = AnchoCanales = samp_rate/(2*N)
        self.Rs = Rs = AnchoCanales/NLobulos
        self.Constelacion = Constelacion = [1+.0j,-1+.0j, .0+1j,0 -1j ]
        self.Rs_user = Rs_user = Rs*N
        self.Bps = Bps = int(math.log(len(Constelacion),2))
        self.sobremuestreo = sobremuestreo = 4
        self.Rb = Rb = Rs_user*Bps
        self.Fguarda = Fguarda = AnchoCanales

        ##################################################
        # Blocks
        ##################################################

        self.low_pass_filter_0_1 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (AnchoCanales/2.),
                (AnchoCanales/8.),
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (AnchoCanales/2.),
                (AnchoCanales/8.),
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (AnchoCanales/2.),
                (AnchoCanales/8.),
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                (AnchoCanales/2.),
                (AnchoCanales/8.),
                window.WIN_HAMMING,
                6.76))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_signal_mult_0_1 = b_signal_mult(
            f=(5*AnchoCanales),
            samp_rate=samp_rate,
        )
        self.b_signal_mult_0_0_0 = b_signal_mult(
            f=(7*AnchoCanales),
            samp_rate=samp_rate,
        )
        self.b_signal_mult_0_0 = b_signal_mult(
            f=(3*AnchoCanales),
            samp_rate=samp_rate,
        )
        self.b_signal_mult_0 = b_signal_mult(
            f=(1*AnchoCanales),
            samp_rate=samp_rate,
        )
        self.E3TRadio_zero_order_hold2_cc_0_0_0_1 = E3TRadio.zero_order_hold2_cc((int(samp_rate/Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0_0 = E3TRadio.zero_order_hold2_cc((int(samp_rate/Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0 = E3TRadio.zero_order_hold2_cc((int(samp_rate/Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0 = E3TRadio.zero_order_hold2_cc((int(samp_rate/Rs)))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_zero_order_hold2_cc_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.E3TRadio_zero_order_hold2_cc_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.E3TRadio_zero_order_hold2_cc_0_0_0_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.E3TRadio_zero_order_hold2_cc_0_0_0_1, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.b_signal_mult_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.b_signal_mult_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.b_signal_mult_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.b_signal_mult_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.low_pass_filter_0, 0), (self.b_signal_mult_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.b_signal_mult_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.b_signal_mult_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.b_signal_mult_0_1, 0))
        self.connect((self, 0), (self.E3TRadio_zero_order_hold2_cc_0_0, 0))
        self.connect((self, 1), (self.E3TRadio_zero_order_hold2_cc_0_0_0, 0))
        self.connect((self, 2), (self.E3TRadio_zero_order_hold2_cc_0_0_0_1, 0))
        self.connect((self, 3), (self.E3TRadio_zero_order_hold2_cc_0_0_0_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_AnchoCanales(self.samp_rate/(2*self.N))
        self.E3TRadio_zero_order_hold2_cc_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0_1.set_retardo((int(self.samp_rate/self.Rs)))
        self.b_signal_mult_0.set_samp_rate(self.samp_rate)
        self.b_signal_mult_0_0.set_samp_rate(self.samp_rate)
        self.b_signal_mult_0_0_0.set_samp_rate(self.samp_rate)
        self.b_signal_mult_0_1.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_AnchoCanales(self.samp_rate/(2*self.N))
        self.set_Rs_user(self.Rs*self.N)

    def get_NLobulos(self):
        return self.NLobulos

    def set_NLobulos(self, NLobulos):
        self.NLobulos = NLobulos
        self.set_Rs(self.AnchoCanales/self.NLobulos)

    def get_AnchoCanales(self):
        return self.AnchoCanales

    def set_AnchoCanales(self, AnchoCanales):
        self.AnchoCanales = AnchoCanales
        self.set_Fguarda(self.AnchoCanales)
        self.set_Rs(self.AnchoCanales/self.NLobulos)
        self.b_signal_mult_0.set_f((1*self.AnchoCanales))
        self.b_signal_mult_0_0.set_f((3*self.AnchoCanales))
        self.b_signal_mult_0_0_0.set_f((7*self.AnchoCanales))
        self.b_signal_mult_0_1.set_f((5*self.AnchoCanales))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, (self.AnchoCanales/2.), (self.AnchoCanales/8.), window.WIN_HAMMING, 6.76))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rs_user(self.Rs*self.N)
        self.E3TRadio_zero_order_hold2_cc_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0_0.set_retardo((int(self.samp_rate/self.Rs)))
        self.E3TRadio_zero_order_hold2_cc_0_0_0_1.set_retardo((int(self.samp_rate/self.Rs)))

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_Bps(int(math.log(len(self.Constelacion),2)))

    def get_Rs_user(self):
        return self.Rs_user

    def set_Rs_user(self, Rs_user):
        self.Rs_user = Rs_user
        self.set_Rb(self.Rs_user*self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs_user*self.Bps)

    def get_sobremuestreo(self):
        return self.sobremuestreo

    def set_sobremuestreo(self, sobremuestreo):
        self.sobremuestreo = sobremuestreo

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_Fguarda(self):
        return self.Fguarda

    def set_Fguarda(self, Fguarda):
        self.Fguarda = Fguarda

