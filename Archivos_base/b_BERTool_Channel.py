# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_BERTool_Channel
# Author: Mancipe Andres, Padilla Astrid, Castillo Jeyson
# Description: Este Bloque sirve a la vez como canal de Ruido Blanco Gausiano y como herramienta para calcular y grafica la curva de BER (Bit error Rate) o SER (simbol error ratio) para una senal con modulacion digital. Parametros usados: N_snr - numero de puntos que tendra la curva de BER; EsNomin: valor minimo de la relación Es/No; EsNomax: valor máximo de la relacion Es/No. Las señales de entrada son: in Tx  para los  simbolos transmitidos; in Rx  para los simbolos recibidos; in es la entrante envolvente compleja de la señal modulada. Las salidas del bloque son: out env que es la saliente envolvente compleja con la adicion de ruido AWGN; out ser que son los valores de BER o SER disponibles. IMPORTANTE: que la curva sea BER o sea SER lo define el tipo de senal que se tiene en in Tx y en in Rx, donde se tiene en cada caso una senal M-aria. Asi que si M=2, estamos enviando y recibiendo bits, luego obtenemos curva de BER, pero si M>2 estamos hablando de curva de SER.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import sip
import threading







class b_BERTool_Channel(gr.hier_block2, Qt.QWidget):
    def __init__(self, EsN0max=20, EsN0min=0, N_snr=128, Rs=125, tipo_mod="QPSK"):
        gr.hier_block2.__init__(
            self, "b_BERTool_Channel",
                gr.io_signature.makev(3, 3, [gr.sizeof_gr_complex*1, gr.sizeof_char*1, gr.sizeof_char*1]),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.EsN0max = EsN0max
        self.EsN0min = EsN0min
        self.N_snr = N_snr
        self.Rs = Rs
        self.tipo_mod = tipo_mod

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N_snr,
            EsN0min,
            ((EsN0max-EsN0min)/float(N_snr)),
            "Es/N0 [dB]",
            "10logPe",
            '',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis((-4), 0)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("dB")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = [tipo_mod, '', '', '', '',
            '', '', '', '', '']
        widths = [6, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
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
        self.connect((self.blocks_stream_to_vector_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self, 0), (self.E3TRadio_e_canal_BER_0, 0))
        self.connect((self, 1), (self.E3TRadio_e_BERtool_0, 1))
        self.connect((self, 2), (self.E3TRadio_e_BERtool_0, 2))


    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, ((self.EsN0max-self.EsN0min)/float(self.N_snr)))

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, ((self.EsN0max-self.EsN0min)/float(self.N_snr)))

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, ((self.EsN0max-self.EsN0min)/float(self.N_snr)))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs

    def get_tipo_mod(self):
        return self.tipo_mod

    def set_tipo_mod(self, tipo_mod):
        self.tipo_mod = tipo_mod

