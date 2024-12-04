# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_PSD_VRMS_c
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
import E3TRadio
import numpy
import sip
import threading







class b_PSD_VRMS_c(gr.hier_block2, Qt.QWidget):
    def __init__(self, Ensayos=1000000, Fc=10000, N=1024, samp_rate_audio=22000):
        gr.hier_block2.__init__(
            self, "b_PSD_VRMS_c",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(0, 0, 0),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.Ensayos = Ensayos
        self.Fc = Fc
        self.N = N
        self.samp_rate_audio = samp_rate_audio

        ##################################################
        # Blocks
        ##################################################

        self.mainwidget3 = Qt.QTabWidget()
        self.mainwidget3_widget_0 = Qt.QWidget()
        self.mainwidget3_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_0)
        self.mainwidget3_grid_layout_0 = Qt.QGridLayout()
        self.mainwidget3_layout_0.addLayout(self.mainwidget3_grid_layout_0)
        self.mainwidget3.addTab(self.mainwidget3_widget_0, 'PSD (Watts/Hz)')
        self.mainwidget3_widget_1 = Qt.QWidget()
        self.mainwidget3_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_1)
        self.mainwidget3_grid_layout_1 = Qt.QGridLayout()
        self.mainwidget3_layout_1.addLayout(self.mainwidget3_grid_layout_1)
        self.mainwidget3.addTab(self.mainwidget3_widget_1, 'Espectro Dinamico en Volts/Hz')
        self.top_layout.addWidget(self.mainwidget3)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            N,
            (-samp_rate_audio/2+Fc),
            ((samp_rate_audio-1)/N),
            "Frecuency",
            "Amplitud (V/Hz)",
            'Titulo',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis(0, 0.14)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("V")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_1.addWidget(self._qtgui_vector_sink_f_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.mainwidget3_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N,
            (-samp_rate_audio/2+Fc),
            ((samp_rate_audio-1)/N),
            "Frecuencia",
            "Amplitud (Watt/Hz)",
            'Titulo',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, (6e-6))
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("Watt/Hz")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [3, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
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
        self.mainwidget3_grid_layout_0.addWidget(self._qtgui_vector_sink_f_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.mainwidget3_grid_layout_0.setColumnStretch(c, 1)
        self.fft_vxx_0 = fft.fft_vcc(N, True, window.rectangular(N), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(numpy.full(N,1./(Ensayos*N)))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff(numpy.full(N,1./N))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(N)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(N)
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, 1000000000)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))


    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))
        self.qtgui_vector_sink_f_0_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.blocks_multiply_const_vxx_0.set_k(numpy.full(self.N,1./self.N))
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.fft_vxx_0.set_window(window.rectangular(self.N))
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))
        self.qtgui_vector_sink_f_0_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))
        self.qtgui_vector_sink_f_0_0.set_x_axis((-self.samp_rate_audio/2+self.Fc), ((self.samp_rate_audio-1)/self.N))

