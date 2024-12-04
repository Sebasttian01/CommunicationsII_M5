# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_BERTool
# Author: Homero Ortega Boada
# Description: Este Bloque sirve a la vez como canal de Ruido Blanco Gausiano y como herramienta para calcular la curva de BER (Bit error Rate) o SER (simbol error ratio) para una senal con modulacion digital. Parametros usados: N_snr - numero de puntos que tendra la curva de BER; EsNomin: valor minimo de la relación Es/No; EsNomax: valor máximo de la relacion Es/No. Las señales de entrada son: in Tx  para los  simbolos transmitidos; in Rx  para los simbolos recibidos; in es la entrante envolvente compleja de la señal modulada. La salida son dos senales: out - es la Curva de BER o SER a graficar;  out_env - que es la saliente envolvente compleja con la adicion de ruido AWGN; out ser que son los valores de BER o SER disponibles. IMPORTANTE: que la curva sea BER o sea SER lo define el tipo de senal que se tiene en in Tx y en in Rx, donde se tiene en cada caso una senal M-aria. Asi que si M=2, estamos enviando y recibiendo bits, luego obtenemos curva de BER, pero si M>2 estamos hablando de curva de SER.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_BERTool(gr.hier_block2):
    def __init__(self, EsN0max=20, EsN0min=0, N_snr=128, Rs=125):
        gr.hier_block2.__init__(
            self, "b_BERTool",
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_char*1, gr.sizeof_char*1]),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_float*N_snr]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.EsN0max = EsN0max
        self.EsN0min = EsN0min
        self.N_snr = N_snr
        self.Rs = Rs

        ##################################################
        # Blocks
        ##################################################

        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, N_snr)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 0)
        self.E3TRadio_e_canal_BER_0 = E3TRadio.e_canal_BER(N_snr, EsN0min, EsN0max, Rs, Rs)
        self.E3TRadio_e_BERtool_0 = E3TRadio.e_BERtool(N_snr)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_e_BERtool_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.E3TRadio_e_canal_BER_0, 1), (self.E3TRadio_e_BERtool_0, 0))
        self.connect((self.E3TRadio_e_canal_BER_0, 0), (self, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self, 1))
        self.connect((self, 0), (self.E3TRadio_e_canal_BER_0, 0))
        self.connect((self, 1), (self.E3TRadio_e_BERtool_0, 1))
        self.connect((self, 2), (self.E3TRadio_e_BERtool_0, 2))


    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

