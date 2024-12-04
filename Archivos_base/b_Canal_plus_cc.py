# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Canal_plus_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Este bloque es un simulador de un canal discreto, sencillo. La simplicidad de este canal esta en aplicar solo lo siguiente: ruido, desviacion de frecuencia, desviacion de angulo, fluctuaciones de magnitud, perdidas de propagacion. Para las fluctuaciones se supone que el umbral de amplitud de la senal que entra al canal es 1, como es el caso de los USRP. Parametros usados: samp_rate_Tx (Hz) es la frecuencia de muestreo del USRP transmisor;  Ch_Phoffset (Rad) permite programar el angulo de la portadora usada en transmision y la usada en recepcion; Ch_Toffset (muestras)  es el retardo que la senal sufre al pasar por el canal; No (dB) es el valor No (o PSD) dado en decibeles del ruido blanco del canal; Ch_Loss_dB (en dB de potencia) nivel de atenuacion que la senal transmitida sufre en el proceso de propagacion; Fluctuation - es el porcentaje de fluctuaciones en magnitud (un numero entero entre 0 y 100); Tfluct - es el periodo, dado en numero de muestras, en que ocurren las fluctuaciones
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_noise_dB_cc import b_noise_dB_cc  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import E3TRadio
import cmath
import math
import numpy
import random
import threading







class b_Canal_plus_cc(gr.hier_block2):
    def __init__(self, Ch_Loss_dB=10., Ch_NodB=1000, Ch_Phoffset=0., Ch_Toffset=0, Fluctuacion=10.0, Foffset=0., T_fluct=1, samp_rate=1000):
        gr.hier_block2.__init__(
            self, "b_Canal_plus_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ch_Loss_dB = Ch_Loss_dB
        self.Ch_NodB = Ch_NodB
        self.Ch_Phoffset = Ch_Phoffset
        self.Ch_Toffset = Ch_Toffset
        self.Fluctuacion = Fluctuacion
        self.Foffset = Foffset
        self.T_fluct = T_fluct
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.Ch_Loss = Ch_Loss = math.pow(10, Ch_Loss_dB/20.)

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1/Ch_Loss+0j)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, Ch_Toffset)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-1))
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.b_noise_dB_cc_0 = b_noise_dB_cc(
            NodB=Ch_NodB,
            samp_rate=samp_rate,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Foffset, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, (Fluctuacion/100.), 0)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cmath.exp(1j * Ch_Phoffset))
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.E3TRadio_Zero_Order_Hold_0 = E3TRadio.Zero_Order_Hold(T_fluct)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.E3TRadio_Zero_Order_Hold_0, 0), (self, 2))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 2))
        self.connect((self.b_noise_dB_cc_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.b_noise_dB_cc_0, 0), (self, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_abs_xx_0_0, 0), (self.E3TRadio_Zero_Order_Hold_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_abs_xx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self, 0), (self.blocks_delay_0, 0))


    def get_Ch_Loss_dB(self):
        return self.Ch_Loss_dB

    def set_Ch_Loss_dB(self, Ch_Loss_dB):
        self.Ch_Loss_dB = Ch_Loss_dB
        self.set_Ch_Loss(math.pow(10, self.Ch_Loss_dB/20.))

    def get_Ch_NodB(self):
        return self.Ch_NodB

    def set_Ch_NodB(self, Ch_NodB):
        self.Ch_NodB = Ch_NodB
        self.b_noise_dB_cc_0.set_NodB(self.Ch_NodB)

    def get_Ch_Phoffset(self):
        return self.Ch_Phoffset

    def set_Ch_Phoffset(self, Ch_Phoffset):
        self.Ch_Phoffset = Ch_Phoffset
        self.analog_const_source_x_1_0.set_offset(cmath.exp(1j * self.Ch_Phoffset))

    def get_Ch_Toffset(self):
        return self.Ch_Toffset

    def set_Ch_Toffset(self, Ch_Toffset):
        self.Ch_Toffset = Ch_Toffset
        self.blocks_delay_0.set_dly(int(self.Ch_Toffset))

    def get_Fluctuacion(self):
        return self.Fluctuacion

    def set_Fluctuacion(self, Fluctuacion):
        self.Fluctuacion = Fluctuacion
        self.analog_noise_source_x_0.set_amplitude((self.Fluctuacion/100.))

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset
        self.analog_sig_source_x_0.set_frequency(self.Foffset)

    def get_T_fluct(self):
        return self.T_fluct

    def set_T_fluct(self, T_fluct):
        self.T_fluct = T_fluct
        self.E3TRadio_Zero_Order_Hold_0.set_retardo(self.T_fluct)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.b_noise_dB_cc_0.set_samp_rate(self.samp_rate)

    def get_Ch_Loss(self):
        return self.Ch_Loss

    def set_Ch_Loss(self, Ch_Loss):
        self.Ch_Loss = Ch_Loss
        self.blocks_multiply_const_vxx_0.set_k(1/self.Ch_Loss+0j)

