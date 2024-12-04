# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_QT_tunner_sampler
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Description: Permite sintonizar manualmente el canal al punto de entregar la senal correctamente muestreada. Parametros usados: samp_rate (Hz) la frecuencia de muestreo de la senal entrante; sps (muestras) numero de muestras por simbolo en la senal entrante; Delay Tuning (muestras) el retrazo que se introduce a la senal antes de aplicarle el muestreo; PhiTuning (Rad) angulo usado para corregir la desviacion de angulo producida por el canal; F_Tuning (Hz) correccion de la desviacion de frecuencias; Nscope (muestras) numero de bits a mostrar en el scope
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from b_tunner import b_tunner  # grc-generated hier_block
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import cmath
import math
import numpy
import random
import sip
import threading







class b_QT_tunner_sampler(gr.hier_block2, Qt.QWidget):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_QT_tunner_sampler",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 2000
        self.run_stop = run_stop = True
        self.phi = phi = 0.
        self.PhiTuning = PhiTuning = 0
        self.Nscope_span = Nscope_span = 24
        self.Kruido = Kruido = 0.01
        self.Foffset = Foffset = 0
        self.F_Tuning = F_Tuning = 0
        self.DelayTuning = DelayTuning = 0

        ##################################################
        # Blocks
        ##################################################

        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Tiempo')
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, 'Constelacion')
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, 'Espectro')
        self.pestana_widget_3 = Qt.QWidget()
        self.pestana_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_3)
        self.pestana_grid_layout_3 = Qt.QGridLayout()
        self.pestana_layout_3.addLayout(self.pestana_grid_layout_3)
        self.pestana.addTab(self.pestana_widget_3, 'Tunner')
        self.top_grid_layout.addWidget(self.pestana, 3, 0, 1, 4)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phi_range = qtgui.Range(-numpy.pi, numpy.pi, numpy.pi/100., 0., 200)
        self._phi_win = qtgui.RangeWidget(self._phi_range, self.set_phi, "Angulo", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._phi_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._PhiTuning_range = qtgui.Range(0, (numpy.pi)*2, (numpy.pi)*2/200, 0, 200)
        self._PhiTuning_win = qtgui.RangeWidget(self._PhiTuning_range, self.set_PhiTuning, "Rx angle tunining", "counter_slider", float, QtCore.Qt.Horizontal)
        self.pestana_grid_layout_3.addWidget(self._PhiTuning_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        self._F_Tuning_range = qtgui.Range(0, 10., 10./1000., 0, 200)
        self._F_Tuning_win = qtgui.RangeWidget(self._F_Tuning_range, self.set_F_Tuning, "Rx Frequency tunining", "counter_slider", float, QtCore.Qt.Horizontal)
        self.pestana_grid_layout_3.addWidget(self._F_Tuning_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        self._DelayTuning_range = qtgui.Range(0, (sps-1), 1, 0, 200)
        self._DelayTuning_win = qtgui.RangeWidget(self._DelayTuning_range, self.set_DelayTuning, "Retardo antes de muestreo ", "counter_slider", int, QtCore.Qt.Horizontal)
        self.pestana_grid_layout_3.addWidget(self._DelayTuning_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox("Inicial/Parar")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.items())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_1_0_0_0 = qtgui.time_sink_c(
            (Nscope_span*sps), #size
            samp_rate, #samp_rate
            "Rx Sample Tunning", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_axis(-0.5, 0.5)

        self.qtgui_time_sink_x_1_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_stem_plot(False)


        labels = ['Rx I', 'Rx Q', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0.qwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_win, 3, 0, 1, 2)
        for r in range(3, 4):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 2):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "Rx sampled", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0_0.set_y_axis((-0.2), 0.2)
        self.qtgui_const_sink_x_0_0_0_0.set_x_axis((-0.2), 0.2)
        self.qtgui_const_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0_0.enable_axis_labels(True)


        labels = ['Rx', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_const_sink_x_0_0_0_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "Rx canal", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_0.set_y_axis((-0.2), 0.2)
        self.qtgui_const_sink_x_0_0_0.set_x_axis((-0.2), 0.2)
        self.qtgui_const_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_0.enable_axis_labels(True)


        labels = ['Rx', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.pestana_grid_layout_3.addWidget(self._qtgui_const_sink_x_0_0_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.pestana_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_3.setColumnStretch(c, 1)
        self.b_tunner_0 = b_tunner(
            Ganancia_ajuste_dB=0,
            NDelay=DelayTuning,
            fdesv=(-F_Tuning),
            phi=PhiTuning,
            samp_rate=samp_rate,
        )
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=0,
            Sps=sps,
        )
        self._Kruido_range = qtgui.Range(0, 1, 0.005, 0.01, 200)
        self._Kruido_win = qtgui.RangeWidget(self._Kruido_range, self.set_Kruido, "Nivel del Ruido", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Kruido_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Foffset_range = qtgui.Range(0, 5, 0.01, 0, 200)
        self._Foffset_win = qtgui.RangeWidget(self._Foffset_range, self.set_Foffset, "Offset de frec.", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Foffset_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_sampler_cc_0, 1), (self, 0))
        self.connect((self.b_sampler_cc_0, 0), (self.qtgui_const_sink_x_0_0_0, 1))
        self.connect((self.b_sampler_cc_0, 1), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.b_sampler_cc_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 1))
        self.connect((self.b_tunner_0, 0), (self.b_sampler_cc_0, 0))
        self.connect((self.b_tunner_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 0))
        self.connect((self, 0), (self.b_tunner_0, 0))
        self.connect((self, 0), (self.qtgui_const_sink_x_0_0_0, 0))


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.b_sampler_cc_0.set_Sps(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_tunner_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0_0.set_samp_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_phi(self):
        return self.phi

    def set_phi(self, phi):
        self.phi = phi

    def get_PhiTuning(self):
        return self.PhiTuning

    def set_PhiTuning(self, PhiTuning):
        self.PhiTuning = PhiTuning
        self.b_tunner_0.set_phi(self.PhiTuning)

    def get_Nscope_span(self):
        return self.Nscope_span

    def set_Nscope_span(self, Nscope_span):
        self.Nscope_span = Nscope_span

    def get_Kruido(self):
        return self.Kruido

    def set_Kruido(self, Kruido):
        self.Kruido = Kruido

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset

    def get_F_Tuning(self):
        return self.F_Tuning

    def set_F_Tuning(self, F_Tuning):
        self.F_Tuning = F_Tuning
        self.b_tunner_0.set_fdesv((-self.F_Tuning))

    def get_DelayTuning(self):
        return self.DelayTuning

    def set_DelayTuning(self, DelayTuning):
        self.DelayTuning = DelayTuning
        self.b_tunner_0.set_NDelay(self.DelayTuning)

