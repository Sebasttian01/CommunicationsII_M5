# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_v_aleatoria_scope_pdf_cdf_f
# Author: Homero Ortega
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Some parameters of a random variable can visualized, like: the mean, the RMS value, the mean power, the PSD,, PDF, CDF the time signal. Parameters used: samp_rate - the sample rate of the signal; N_time - the number of time samples to be shown; N_frec- the number of frequency pointss to be shown
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_cdf_ff import b_cdf_ff  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import E3TRadio
import math
import sip
import threading







class b_v_aleatoria_scope_pdf_cdf_f(gr.hier_block2, Qt.QWidget):
    def __init__(self, N_frec=2014, N_time=2014, V_p=2014, samp_rate=22000):
        gr.hier_block2.__init__(
            self, "b_v_aleatoria_scope_pdf_cdf_f",
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
        self.N_frec = N_frec
        self.N_time = N_time
        self.V_p = V_p
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.Mean_reset = Mean_reset = 1

        ##################################################
        # Blocks
        ##################################################

        _Mean_reset_push_button = Qt.QPushButton('Push here to restart averaging procces')
        _Mean_reset_push_button = Qt.QPushButton('Push here to restart averaging procces')
        self._Mean_reset_choices = {'Pressed': 0, 'Released': 1}
        _Mean_reset_push_button.pressed.connect(lambda: self.set_Mean_reset(self._Mean_reset_choices['Pressed']))
        _Mean_reset_push_button.released.connect(lambda: self.set_Mean_reset(self._Mean_reset_choices['Released']))
        self.top_grid_layout.addWidget(_Mean_reset_push_button, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            N_time, #size
            samp_rate, #samp_rate
            "signal in time", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-V_p, V_p)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['.', 'Im', '', '', '',
            '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0_0_0.set_title('')

        labels = ['VRMS instantaneous', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0_0_0_0.set_min(i, -2)
            self.qtgui_number_sink_0_0_0_0_0_0_0.set_max(i, 2)
            self.qtgui_number_sink_0_0_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_0_0_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0_0.set_title('')

        labels = ['Mean square (Mean Power)', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0_0_0.set_min(i, -2)
            self.qtgui_number_sink_0_0_0_0_0_0.set_max(i, 2)
            self.qtgui_number_sink_0_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0.set_title('')

        labels = ['The mean', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0_0_0_0_0.set_min(i, -2)
            self.qtgui_number_sink_0_0_0_0_0.set_max(i, 2)
            self.qtgui_number_sink_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_rms_xx_0 = blocks.rms_ff(0.0001)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.b_cdf_ff_0 = b_cdf_ff(
            EjeX='potencia',
            Xmax=V_p,
            Xmin=(-V_p),
        )

        self.top_grid_layout.addWidget(self.b_cdf_ff_0, 2, 2, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.E3TRadio_mean_meter_0_0 = E3TRadio.mean_meter(Mean_reset)
        self.E3TRadio_mean_meter_0 = E3TRadio.mean_meter(Mean_reset)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_mean_meter_0, 0), (self.qtgui_number_sink_0_0_0_0_0, 0))
        self.connect((self.E3TRadio_mean_meter_0_0, 0), (self.qtgui_number_sink_0_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.E3TRadio_mean_meter_0_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.qtgui_number_sink_0_0_0_0_0_0_0, 0))
        self.connect((self, 0), (self.E3TRadio_mean_meter_0, 0))
        self.connect((self, 0), (self.b_cdf_ff_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self, 0), (self.qtgui_time_sink_x_0_0_0, 0))


    def get_N_frec(self):
        return self.N_frec

    def set_N_frec(self, N_frec):
        self.N_frec = N_frec

    def get_N_time(self):
        return self.N_time

    def set_N_time(self, N_time):
        self.N_time = N_time

    def get_V_p(self):
        return self.V_p

    def set_V_p(self, V_p):
        self.V_p = V_p
        self.b_cdf_ff_0.set_Xmax(self.V_p)
        self.b_cdf_ff_0.set_Xmin((-self.V_p))
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-self.V_p, self.V_p)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)

    def get_Mean_reset(self):
        return self.Mean_reset

    def set_Mean_reset(self, Mean_reset):
        self.Mean_reset = Mean_reset
        self.E3TRadio_mean_meter_0.set_reset(self.Mean_reset)
        self.E3TRadio_mean_meter_0_0.set_reset(self.Mean_reset)

