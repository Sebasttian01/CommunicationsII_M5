# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_BERTool_ff
# Author: Homero Ortega Boada
# Description: Este Bloque sirve a la vez como canal de Ruido Blanco Gausiano y como herramienta para calcular la curva de BER (Bit error Rate) para una senal binaria real. Pero tambien se puede usar para señales M-arias reales como M-PAM. Se pueden usar señales que han pasado por un filtroformador de pulsos. En caso de que la entrada sea una señal binara, siempre que se hable de simbolos es lo mismo que hablar de bits, es decir, los simbolos son bits puros. Parametros usados: Sps - es el número muestras por simbolo, en caso de no usar un filtro formador de pulsos Sps=1, recuerde que Sps=samp_reate/Sps; Rs - es la rata de simbolos; N_snr - numero de puntos que tendra la curva de BER; EsNomin: valor minimo de la relación Es/No; EsNomax: valor máximo de la relacion Es/No. Las señales de entrada son: in Tx  para los  simbolos transmitidos; in Rx  para los simbolos recibidos; in es la señal enviada. La salida son dos senales: out - es la Curva de BER o SER a graficar;  out_env - es la señal que sale del canal AWGN, que es la misma entrante pero con ruido ; out que son los valores de BER o SER disponibles. IMPORTANTE: que la curva sea BER o sea SER lo define el tipo de senal que se tiene en in Tx y en in Rx, donde se tiene en cada caso una senal M-aria. Asi que si M=2, estamos enviando y recibiendo simbolos, luego obtenemos curva de BER, pero si M>2 estamos hablando de curva de SER.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_BERTool_ff(gr.hier_block2):
    def __init__(self, EsN0max=20, EsN0min=0, N_snr=128, Rs=125, Sps=1):
        gr.hier_block2.__init__(
            self, "b_BERTool_ff",
                gr.io_signature.makev(3, 3, [gr.sizeof_float*1, gr.sizeof_char*1, gr.sizeof_char*1]),
                gr.io_signature.makev(2, 2, [gr.sizeof_float*1, gr.sizeof_float*N_snr]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.EsN0max = EsN0max
        self.EsN0min = EsN0min
        self.N_snr = N_snr
        self.Rs = Rs
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, N_snr)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.E3TRadio_zero_order_hold_bb_0_0 = E3TRadio.zero_order_hold_bb(Sps)
        self.E3TRadio_zero_order_hold_bb_0 = E3TRadio.zero_order_hold_bb(Sps)
        self.E3TRadio_e_canal_BER_0 = E3TRadio.e_canal_BER(N_snr, EsN0min/2., EsN0max/2., Rs*Sps, Rs)
        self.E3TRadio_e_BERtool_0 = E3TRadio.e_BERtool(N_snr)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_e_BERtool_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.E3TRadio_e_canal_BER_0, 1), (self.E3TRadio_e_BERtool_0, 0))
        self.connect((self.E3TRadio_e_canal_BER_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.E3TRadio_zero_order_hold_bb_0, 0), (self.E3TRadio_e_BERtool_0, 1))
        self.connect((self.E3TRadio_zero_order_hold_bb_0_0, 0), (self.E3TRadio_e_BERtool_0, 2))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.E3TRadio_e_canal_BER_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_stream_to_vector_0, 0), (self, 1))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self, 1), (self.E3TRadio_zero_order_hold_bb_0, 0))
        self.connect((self, 2), (self.E3TRadio_zero_order_hold_bb_0_0, 0))


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

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.E3TRadio_zero_order_hold_bb_0.set_retardo(self.Sps)
        self.E3TRadio_zero_order_hold_bb_0_0.set_retardo(self.Sps)

