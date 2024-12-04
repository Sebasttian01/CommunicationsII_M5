# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_USRP_2_USRP_v2
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Este bloque es el simulador de un canal inalambrico que incluye 2 USRPs, uno en la parte transmisora y otro en la receptora. Se puede usar cuando no se tengan USRP fisicos a la mano. Parametros usados: samp_rate_Tx (Hz) es la frecuencia de muestreo del USRP transmisor; Bandwidth_Tx  (Hz) ancho de banda programado en el USRP transmisor; Center freq Tx (Hz) frecuencia central del USRP Transmisor; samp_rate_Rx, Bandwidth_Rx, Center freq Rx  son equivalentes a los anteriores pero para el USRP receptor;  Toffset (numero de muestras de offset. como la rata de muestras de la senal entrante puede ser diferente a la saliente, en este caso se toman de la senal entrante) permtite programar un tiempo de retardo de la senal en propagacion;  Phoffset (Rad) permite programar una desviacion entre el angulo de la portadora usada en transmision y la usada en recepcion; No (dB) es el valor No (o PSD) dado en decibeles del ruido blanco del canal; Katt (en dB de potencia) nivel de atenuacion que la senal transmitida sufre en el proceso de propagacion.
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
import cmath
import math
import numpy
import random
import threading







class b_USRP_2_USRP_v2(gr.hier_block2):
    def __init__(self, Ch_Loss_dB=10., Ch_NodB=1000, Ch_Phoffset=((numpy.pi)*2*random.random()), Ch_Toffset=5, Rx_B=1000, Rx_Fc=200000000, Rx_Gain_dB=10., Rx__samp_rate=1000, Tx_B=1000, Tx_Fc=200000000, Tx_Gain_dB=10., Tx__samp_rate=1000):
        gr.hier_block2.__init__(
            self, "b_USRP_2_USRP_v2",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ch_Loss_dB = Ch_Loss_dB
        self.Ch_NodB = Ch_NodB
        self.Ch_Phoffset = Ch_Phoffset
        self.Ch_Toffset = Ch_Toffset
        self.Rx_B = Rx_B
        self.Rx_Fc = Rx_Fc
        self.Rx_Gain_dB = Rx_Gain_dB
        self.Rx__samp_rate = Rx__samp_rate
        self.Tx_B = Tx_B
        self.Tx_Fc = Tx_Fc
        self.Tx_Gain_dB = Tx_Gain_dB
        self.Tx__samp_rate = Tx__samp_rate

        ##################################################
        # Variables
        ##################################################
        self.Gain_Tx_Loss_dB = Gain_Tx_Loss_dB = Tx_Gain_dB  - Ch_Loss_dB
        self.B_Txx = B_Txx = (Tx_B>0)*Tx_B+(Tx_B==0)*Tx__samp_rate
        self.B_Rxx = B_Rxx = (Rx_B>0)*Rx_B+(Rx_B==0)*Rx__samp_rate
        self.Gain_Tx_Loss = Gain_Tx_Loss = math.pow(10, Gain_Tx_Loss_dB/20.)
        self.Gain_Rx = Gain_Rx = math.pow(10, Rx_Gain_dB/20.)
        self.Foffset = Foffset = Tx_Fc-Rx_Fc
        self.Bmin = Bmin = min(B_Txx, B_Rxx)

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(Gain_Rx+0j)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Gain_Tx_Loss+0j)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, Ch_Toffset)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.b_noise_dB_cc_0 = b_noise_dB_cc(
            NodB=Ch_NodB,
            samp_rate=10000,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(Rx__samp_rate, analog.GR_COS_WAVE, Foffset, 1, 0, 0)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cmath.exp(1j * Ch_Phoffset))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.b_noise_dB_cc_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.b_noise_dB_cc_0, 0), (self, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_Ch_Loss_dB(self):
        return self.Ch_Loss_dB

    def set_Ch_Loss_dB(self, Ch_Loss_dB):
        self.Ch_Loss_dB = Ch_Loss_dB
        self.set_Gain_Tx_Loss_dB(self.Tx_Gain_dB  - self.Ch_Loss_dB)

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

    def get_Rx_B(self):
        return self.Rx_B

    def set_Rx_B(self, Rx_B):
        self.Rx_B = Rx_B
        self.set_B_Rxx((self.Rx_B>0)*self.Rx_B+(self.Rx_B==0)*self.Rx__samp_rate)

    def get_Rx_Fc(self):
        return self.Rx_Fc

    def set_Rx_Fc(self, Rx_Fc):
        self.Rx_Fc = Rx_Fc
        self.set_Foffset(self.Tx_Fc-self.Rx_Fc)

    def get_Rx_Gain_dB(self):
        return self.Rx_Gain_dB

    def set_Rx_Gain_dB(self, Rx_Gain_dB):
        self.Rx_Gain_dB = Rx_Gain_dB
        self.set_Gain_Rx(math.pow(10, self.Rx_Gain_dB/20.))

    def get_Rx__samp_rate(self):
        return self.Rx__samp_rate

    def set_Rx__samp_rate(self, Rx__samp_rate):
        self.Rx__samp_rate = Rx__samp_rate
        self.set_B_Rxx((self.Rx_B>0)*self.Rx_B+(self.Rx_B==0)*self.Rx__samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.Rx__samp_rate)

    def get_Tx_B(self):
        return self.Tx_B

    def set_Tx_B(self, Tx_B):
        self.Tx_B = Tx_B
        self.set_B_Txx((self.Tx_B>0)*self.Tx_B+(self.Tx_B==0)*self.Tx__samp_rate)

    def get_Tx_Fc(self):
        return self.Tx_Fc

    def set_Tx_Fc(self, Tx_Fc):
        self.Tx_Fc = Tx_Fc
        self.set_Foffset(self.Tx_Fc-self.Rx_Fc)

    def get_Tx_Gain_dB(self):
        return self.Tx_Gain_dB

    def set_Tx_Gain_dB(self, Tx_Gain_dB):
        self.Tx_Gain_dB = Tx_Gain_dB
        self.set_Gain_Tx_Loss_dB(self.Tx_Gain_dB  - self.Ch_Loss_dB)

    def get_Tx__samp_rate(self):
        return self.Tx__samp_rate

    def set_Tx__samp_rate(self, Tx__samp_rate):
        self.Tx__samp_rate = Tx__samp_rate
        self.set_B_Txx((self.Tx_B>0)*self.Tx_B+(self.Tx_B==0)*self.Tx__samp_rate)

    def get_Gain_Tx_Loss_dB(self):
        return self.Gain_Tx_Loss_dB

    def set_Gain_Tx_Loss_dB(self, Gain_Tx_Loss_dB):
        self.Gain_Tx_Loss_dB = Gain_Tx_Loss_dB
        self.set_Gain_Tx_Loss(math.pow(10, self.Gain_Tx_Loss_dB/20.))

    def get_B_Txx(self):
        return self.B_Txx

    def set_B_Txx(self, B_Txx):
        self.B_Txx = B_Txx
        self.set_Bmin(min(self.B_Txx, self.B_Rxx))

    def get_B_Rxx(self):
        return self.B_Rxx

    def set_B_Rxx(self, B_Rxx):
        self.B_Rxx = B_Rxx
        self.set_Bmin(min(self.B_Txx, self.B_Rxx))

    def get_Gain_Tx_Loss(self):
        return self.Gain_Tx_Loss

    def set_Gain_Tx_Loss(self, Gain_Tx_Loss):
        self.Gain_Tx_Loss = Gain_Tx_Loss
        self.blocks_multiply_const_vxx_0.set_k(self.Gain_Tx_Loss+0j)

    def get_Gain_Rx(self):
        return self.Gain_Rx

    def set_Gain_Rx(self, Gain_Rx):
        self.Gain_Rx = Gain_Rx
        self.blocks_multiply_const_vxx_0_0.set_k(self.Gain_Rx+0j)

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset
        self.analog_sig_source_x_0.set_frequency(self.Foffset)

    def get_Bmin(self):
        return self.Bmin

    def set_Bmin(self, Bmin):
        self.Bmin = Bmin

