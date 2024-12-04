# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_downconverter_fc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Es un downconverter. Los parametros usados son: samp_rate (Hz): es la frecuencia de muestreo que es igual para senal entrante y para la saliente; Fc (Hz) es la frecuencia de la portadora que sera generada; BW (Hz) ancho de banda de la senal bandabase esperada. Nota: es importante resaltar de nuevo, que la senal entrante debe estar muestreada a la misma razon que se espera para la senal saliente.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import threading







class b_downconverter_fc(gr.hier_block2):
    def __init__(self, BW=11000, Fc=16000, samp_rate=44000):
        gr.hier_block2.__init__(
            self, "b_downconverter_fc",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.BW = BW
        self.Fc = Fc
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################

        self.low_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                BW,
                (BW/16.),
                window.WIN_RECTANGULAR,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                BW,
                (BW/16.),
                window.WIN_RECTANGULAR,
                6.76))
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Fc, 2, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, Fc, (-2), 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0_1, 1))


    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16.), window.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16.), window.WIN_RECTANGULAR, 6.76))

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.analog_sig_source_x_0_0_0.set_frequency(self.Fc)
        self.analog_sig_source_x_0_1.set_frequency(self.Fc)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16.), window.WIN_RECTANGULAR, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, (self.BW/16.), window.WIN_RECTANGULAR, 6.76))

