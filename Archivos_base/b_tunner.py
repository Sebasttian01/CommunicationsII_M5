# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_tunner
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Permite sintonizar la fase y la frecuencia de una senal que llega por un USRP
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import cmath
import math
import threading







class b_tunner(gr.hier_block2):
    def __init__(self, Ganancia_ajuste_dB=0, NDelay=0, fdesv=0, phi=0, samp_rate=1000):
        gr.hier_block2.__init__(
            self, "b_tunner",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ganancia_ajuste_dB = Ganancia_ajuste_dB
        self.NDelay = NDelay
        self.fdesv = fdesv
        self.phi = phi
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, NDelay)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fdesv, (math.pow(10,Ganancia_ajuste_dB/20.)), 0, 0)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cmath.exp(1j * phi))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))


    def get_Ganancia_ajuste_dB(self):
        return self.Ganancia_ajuste_dB

    def set_Ganancia_ajuste_dB(self, Ganancia_ajuste_dB):
        self.Ganancia_ajuste_dB = Ganancia_ajuste_dB
        self.analog_sig_source_x_0.set_amplitude((math.pow(10,self.Ganancia_ajuste_dB/20.)))

    def get_NDelay(self):
        return self.NDelay

    def set_NDelay(self, NDelay):
        self.NDelay = NDelay
        self.blocks_delay_0.set_dly(int(self.NDelay))

    def get_fdesv(self):
        return self.fdesv

    def set_fdesv(self, fdesv):
        self.fdesv = fdesv
        self.analog_sig_source_x_0.set_frequency(self.fdesv)

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi
        self.analog_const_source_x_1_0.set_offset(cmath.exp(1j * self.phi))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

