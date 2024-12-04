# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Nyquist_Filter_ff
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: It is the float version of Nyquist Filter in a proof period. Parameters: Sps - the number of samples per simbol the filter will produce; ntaps- the number of components in the impulse response
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import math
import numpy
import threading







class b_Nyquis_Filter_ff(gr.hier_block2):
    def __init__(self, Ganancia=1., Sps=8, ntaps=16):
        gr.hier_block2.__init__(
            self, "b_Nyquist_Filter_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ganancia = Ganancia
        self.Sps = Sps
        self.ntaps = ntaps

        ##################################################
        # Variables
        ##################################################
        self.ntaps_min = ntaps_min = -int(ntaps/2)
        self.ntaps_max = ntaps_max = abs(ntaps_min)-1+math.ceil(ntaps/2.-abs(ntaps_min))
        self.n = n = numpy.linspace(ntaps_min,ntaps_max,ntaps)
        self.h = h = numpy.sinc(n/Sps)
        self.Amp = Amp = numpy.amax(h)

        ##################################################
        # Blocks
        ##################################################

        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(Sps, h/Amp)
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f(h, True, 1, [])
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(Ganancia)


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

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h(numpy.sinc(self.n/self.Sps))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_n(numpy.linspace(self.ntaps_min,self.ntaps_max,self.ntaps))
        self.set_ntaps_max(abs(self.ntaps_min)-1+math.ceil(self.ntaps/2.-abs(self.ntaps_min)))
        self.set_ntaps_min(-int(self.ntaps/2))

    def get_ntaps_min(self):
        return self.ntaps_min

    def set_ntaps_min(self, ntaps_min):
        self.ntaps_min = ntaps_min
        self.set_n(numpy.linspace(self.ntaps_min,self.ntaps_max,self.ntaps))
        self.set_ntaps_max(abs(self.ntaps_min)-1+math.ceil(self.ntaps/2.-abs(self.ntaps_min)))

    def get_ntaps_max(self):
        return self.ntaps_max

    def set_ntaps_max(self, ntaps_max):
        self.ntaps_max = ntaps_max
        self.set_n(numpy.linspace(self.ntaps_min,self.ntaps_max,self.ntaps))

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
        self.set_h(numpy.sinc(self.n/self.Sps))

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_Amp(numpy.amax(self.h))
        self.blocks_vector_source_x_0_0.set_data(self.h, [])
        self.interp_fir_filter_xxx_0_0.set_taps(self.h/self.Amp)

    def get_Amp(self):
        return self.Amp

    def set_Amp(self, Amp):
        self.Amp = Amp
        self.interp_fir_filter_xxx_0_0.set_taps(self.h/self.Amp)
