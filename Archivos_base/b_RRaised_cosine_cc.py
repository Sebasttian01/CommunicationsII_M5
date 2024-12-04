# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_RRaised_cosine_cc
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander
# Description: It is the Root Raised Cosine Filter. Usually gnuradio comes with the square root variant, but this is the right one. Parameters: rolloff - is the rolloff factor or Exccess Bandwidth;  sps - the number of samples per simbol the filter will produce; ntaps- the number of components in the impulse response. Note that if you use two such blocks one in the transmiter (Tx) and one in the receiver (Rx) to obtain a matched filter, equivalent to a RC Filter that satisfies the Nyquist ISI Criterion, the configuration have to be this way: At the Tx give: interpolation=samples per symbol, ntaps= samples per symbol * number of taps; at the receiver give:  intepolation=1; ntaps=number of taps
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import numpy
import threading







class b_RRaised_cosine_cc(gr.hier_block2):
    def __init__(self, Ganancia=1., Interpolation=1, ntaps=16, rolloff=1, sps=8):
        gr.hier_block2.__init__(
            self, "b_RRaised_cosine_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ganancia = Ganancia
        self.Interpolation = Interpolation
        self.ntaps = ntaps
        self.rolloff = rolloff
        self.sps = sps

        ##################################################
        # Variables
        ##################################################
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(1, sps, 1, rolloff, ntaps)
        self.Amp = Amp = numpy.amax(rrc_taps)

        ##################################################
        # Blocks
        ##################################################

        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccc(Interpolation, rrc_taps/Amp)
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c(rrc_taps, True, 1, [])
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Ganancia)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self, 1))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_Ganancia(self):
        return self.Ganancia

    def set_Ganancia(self, Ganancia):
        self.Ganancia = Ganancia
        self.blocks_multiply_const_vxx_0.set_k(self.Ganancia)

    def get_Interpolation(self):
        return self.Interpolation

    def set_Interpolation(self, Interpolation):
        self.Interpolation = Interpolation

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1, self.rolloff, self.ntaps))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1, self.rolloff, self.ntaps))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(1, self.sps, 1, self.rolloff, self.ntaps))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.set_Amp(numpy.amax(self.rrc_taps))
        self.blocks_vector_source_x_0_0.set_data(self.rrc_taps, [])
        self.interp_fir_filter_xxx_0_0.set_taps(self.rrc_taps/self.Amp)

    def get_Amp(self):
        return self.Amp

    def set_Amp(self, Amp):
        self.Amp = Amp
        self.interp_fir_filter_xxx_0_0.set_taps(self.rrc_taps/self.Amp)

