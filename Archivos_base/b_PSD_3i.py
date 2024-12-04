# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_PSD_3i
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
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







class b_PSD_3i(gr.hier_block2, Qt.QWidget):
    def __init__(self, Amp=1, Ensayos=1000000, N=1024, Subtitulo0='espectro0', Subtitulo1='espectro1', Subtitulo2='espectro2', Titulo='espectro', samp_rate_audio=22000):
        gr.hier_block2.__init__(
            self, "b_PSD_3i",
                gr.io_signature.makev(3, 3, [gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1]),
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
        self.Amp = Amp
        self.Ensayos = Ensayos
        self.N = N
        self.Subtitulo0 = Subtitulo0
        self.Subtitulo1 = Subtitulo1
        self.Subtitulo2 = Subtitulo2
        self.Titulo = Titulo
        self.samp_rate_audio = samp_rate_audio

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N,
            (-samp_rate_audio/2),
            ((samp_rate_audio-1)/N),
            "Frecuencia",
            "Amplitud (Watt/Hz)",
            Titulo,
            3, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis((-1./(4*Ensayos)), (1./Ensayos))
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("Watt/Hz")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = [Subtitulo0, Subtitulo1, Subtitulo2, '', '',
            '', '', '', '', '']
        widths = [4, 4, 4, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.fft_vxx_0_1 = fft.fft_vcc(N, True, window.rectangular(N), True, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(N, True, window.rectangular(N), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(N, True, window.rectangular(N), True, 1)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff(numpy.full(N,1./(Ensayos*N)))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff(numpy.full(N,1./(Ensayos*N)))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(numpy.full(N,1./(Ensayos*N)))
        self.blocks_float_to_complex_0_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(N)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(N)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(N)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.E3TRadio_vector_average_hob_0_1 = E3TRadio.vector_average_hob(N, 1000000000)
        self.E3TRadio_vector_average_hob_0_0 = E3TRadio.vector_average_hob(N, 1000000000)
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, 1000000000)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.E3TRadio_vector_average_hob_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.E3TRadio_vector_average_hob_0_1, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0_1, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.E3TRadio_vector_average_hob_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.E3TRadio_vector_average_hob_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_1, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.qtgui_vector_sink_f_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.qtgui_vector_sink_f_0, 2))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.fft_vxx_0_1, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.fft_vxx_0_1, 0), (self.blocks_complex_to_mag_squared_0_1, 0))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self, 1), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self, 2), (self.blocks_float_to_complex_0_1, 0))


    def get_Amp(self):
        return self.Amp

    def set_Amp(self, Amp):
        self.Amp = Amp

    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.blocks_multiply_const_vxx_0_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.blocks_multiply_const_vxx_0_0_1.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.qtgui_vector_sink_f_0.set_y_axis((-1./(4*self.Ensayos)), (1./self.Ensayos))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.blocks_multiply_const_vxx_0_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.blocks_multiply_const_vxx_0_0_1.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.fft_vxx_0.set_window(window.rectangular(self.N))
        self.fft_vxx_0_0.set_window(window.rectangular(self.N))
        self.fft_vxx_0_1.set_window(window.rectangular(self.N))
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))

    def get_Subtitulo0(self):
        return self.Subtitulo0

    def set_Subtitulo0(self, Subtitulo0):
        self.Subtitulo0 = Subtitulo0

    def get_Subtitulo1(self):
        return self.Subtitulo1

    def set_Subtitulo1(self, Subtitulo1):
        self.Subtitulo1 = Subtitulo1

    def get_Subtitulo2(self):
        return self.Subtitulo2

    def set_Subtitulo2(self, Subtitulo2):
        self.Subtitulo2 = Subtitulo2

    def get_Titulo(self):
        return self.Titulo

    def set_Titulo(self, Titulo):
        self.Titulo = Titulo

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))

