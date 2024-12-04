# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_PSD_VRMS
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







class b_PSD_VRMS(gr.hier_block2, Qt.QWidget):
    def __init__(self, Amp=1, Ensayos=1000000, N=1024, samp_rate_audio=22000):
        gr.hier_block2.__init__(
            self, "b_PSD_VRMS",
                gr.io_signature(1, 1, gr.sizeof_float*1),
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
        self.samp_rate_audio = samp_rate_audio

        ##################################################
        # Blocks
        ##################################################

        self.mainwidget3 = Qt.QTabWidget()
        self.mainwidget3_widget_0 = Qt.QWidget()
        self.mainwidget3_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_0)
        self.mainwidget3_grid_layout_0 = Qt.QGridLayout()
        self.mainwidget3_layout_0.addLayout(self.mainwidget3_grid_layout_0)
        self.mainwidget3.addTab(self.mainwidget3_widget_0, 'Espectro Dinamico en Volts/Hz')
        self.mainwidget3_widget_1 = Qt.QWidget()
        self.mainwidget3_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_1)
        self.mainwidget3_grid_layout_1 = Qt.QGridLayout()
        self.mainwidget3_layout_1.addLayout(self.mainwidget3_grid_layout_1)
        self.mainwidget3.addTab(self.mainwidget3_widget_1, 'Especto Dinamico en dB')
        self.mainwidget3_widget_2 = Qt.QWidget()
        self.mainwidget3_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_2)
        self.mainwidget3_grid_layout_2 = Qt.QGridLayout()
        self.mainwidget3_layout_2.addLayout(self.mainwidget3_grid_layout_2)
        self.mainwidget3.addTab(self.mainwidget3_widget_2, 'PSD (Watts/Hz)')
        self.mainwidget3_widget_3 = Qt.QWidget()
        self.mainwidget3_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_3)
        self.mainwidget3_grid_layout_3 = Qt.QGridLayout()
        self.mainwidget3_layout_3.addLayout(self.mainwidget3_grid_layout_3)
        self.mainwidget3.addTab(self.mainwidget3_widget_3, 'PSD en dB')
        self.mainwidget3_widget_4 = Qt.QWidget()
        self.mainwidget3_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.mainwidget3_widget_4)
        self.mainwidget3_grid_layout_4 = Qt.QGridLayout()
        self.mainwidget3_layout_4.addLayout(self.mainwidget3_grid_layout_4)
        self.mainwidget3.addTab(self.mainwidget3_widget_4, 'Senal en tiempo')
        self.top_layout.addWidget(self.mainwidget3)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            N,
            (-samp_rate_audio/2),
            ((samp_rate_audio-1)/N),
            "Frecuency",
            "Amplitud (V/Hz)",
            '',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis((-0.01), 0.1)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("V")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.mainwidget3_grid_layout_0.addWidget(self._qtgui_vector_sink_f_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.mainwidget3_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N,
            (-samp_rate_audio/2),
            ((samp_rate_audio-1)/N),
            "Frecuencia",
            "Amplitud (Watt/Hz)",
            '',
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis((-1./(4*Ensayos)), (1./Ensayos))
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("Watt/Hz")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
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
        self.mainwidget3_grid_layout_2.addWidget(self._qtgui_vector_sink_f_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.mainwidget3_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            32, #size
            samp_rate_audio, #samp_rate
            "Osciloscopio", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-Amp, Amp)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Tx', 'Rx', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 3)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 3):
            self.mainwidget3_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_1.set_title("VRMS")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_4.addWidget(self._qtgui_number_sink_0_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.mainwidget3_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.mainwidget3_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1.set_title("P")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_4.addWidget(self._qtgui_number_sink_0_0_1_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.mainwidget3_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.mainwidget3_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_1.set_title("P (dB)")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_1.set_min(i, -1)
            self.qtgui_number_sink_0_0_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_1.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_4.addWidget(self._qtgui_number_sink_0_0_0_1_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.mainwidget3_grid_layout_4.setRowStretch(r, 1)
        for c in range(2, 3):
            self.mainwidget3_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_audio, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_3.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 0, 1, 3)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 3):
            self.mainwidget3_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate_audio, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.mainwidget3_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 1, 3)
        for r in range(0, 1):
            self.mainwidget3_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 3):
            self.mainwidget3_grid_layout_1.setColumnStretch(c, 1)
        self.fft_vxx_0 = fft.fft_vcc(N, True, window.rectangular(N), True, 1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_rms_xx_0_0 = blocks.rms_ff(0.0001)
        self.blocks_nlog10_ff_0_2 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(numpy.full(N,1./(Ensayos*N)))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff(numpy.full(N,1./N))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(N)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(N)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.E3TRadio_vector_average_hob_0 = E3TRadio.vector_average_hob(N, 1000000000)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_vector_average_hob_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.E3TRadio_vector_average_hob_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_nlog10_ff_0_2, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.qtgui_number_sink_0_0_1, 0))
        self.connect((self.blocks_nlog10_ff_0_2, 0), (self.qtgui_number_sink_0_0_0_1, 0))
        self.connect((self.blocks_rms_xx_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_rms_xx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_rms_xx_0_0, 0), (self.qtgui_number_sink_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self, 0), (self.blocks_rms_xx_0_0, 0))
        self.connect((self, 0), (self.qtgui_time_sink_x_0, 0))


    def get_Amp(self):
        return self.Amp

    def set_Amp(self, Amp):
        self.Amp = Amp
        self.qtgui_time_sink_x_0.set_y_axis(-self.Amp, self.Amp)

    def get_Ensayos(self):
        return self.Ensayos

    def set_Ensayos(self, Ensayos):
        self.Ensayos = Ensayos
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.qtgui_vector_sink_f_0.set_y_axis((-1./(4*self.Ensayos)), (1./self.Ensayos))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.blocks_multiply_const_vxx_0.set_k(numpy.full(self.N,1./self.N))
        self.blocks_multiply_const_vxx_0_0.set_k(numpy.full(self.N,1./(self.Ensayos*self.N)))
        self.fft_vxx_0.set_window(window.rectangular(self.N))
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))
        self.qtgui_vector_sink_f_0_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate_audio)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate_audio)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate_audio)
        self.qtgui_vector_sink_f_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))
        self.qtgui_vector_sink_f_0_0.set_x_axis((-self.samp_rate_audio/2), ((self.samp_rate_audio-1)/self.N))

