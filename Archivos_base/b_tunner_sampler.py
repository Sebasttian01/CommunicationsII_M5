# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_tunner_sampler
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Permite sintonizar manualmente el canal, usando visores y reguladores, al punto de entregar la senal correctamente muestreada. Parametros usados: samp_rate (Hz) la frecuencia de muestreo de la senal entrante; sps (muestras) numero de muestras por simbolo en la senal entrante; Delay Tuning (muestras) el retrazo que se introduce a la senal antes de aplicarle el muestreo; PhiTuning (Rad) angulo usado para corregir la desviacion de angulo producida por el canal; F_Tuning (Hz) correccion de la desviacion de frecuencias; Nscope (muestras) numero de bits a mostrar en el scope; Nscope_spanNscope_span numero de bits a mostrar en el osciloscopio donde se selecciona el muestreo; DelayTuningInicial (muestras) es un valor sugerido de arranque para la sintonizacion del retardo para el muestreo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from b_Eye_Diagram import b_Eye_Diagram  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from b_tunner import b_tunner  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import numpy
import sip
import threading







class b_tunner_sampler(gr.hier_block2, Qt.QWidget):
    def __init__(self, AlphaLineasOjo=1.0, DelayTuningInicial=0, GrosorLineasOjo=1, samp_rate=1000, sps=8):
        gr.hier_block2.__init__(
            self, "b_tunner_sampler",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
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
        self.AlphaLineasOjo = AlphaLineasOjo
        self.DelayTuningInicial = DelayTuningInicial
        self.GrosorLineasOjo = GrosorLineasOjo
        self.samp_rate = samp_rate
        self.sps = sps

        ##################################################
        # Variables
        ##################################################
        self.PhiTuning = PhiTuning = 0
        self.F_Tuning = F_Tuning = 0
        self.EyeDelay = EyeDelay = 0
        self.DelayTuning = DelayTuning = DelayTuningInicial

        ##################################################
        # Blocks
        ##################################################

        self._PhiTuning_range = qtgui.Range(0, (numpy.pi)*2, (numpy.pi)*2/200, 0, 200)
        self._PhiTuning_win = qtgui.RangeWidget(self._PhiTuning_range, self.set_PhiTuning, "Rx angle tunining", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._PhiTuning_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._F_Tuning_range = qtgui.Range(0, 10., 10./1000., 0, 200)
        self._F_Tuning_win = qtgui.RangeWidget(self._F_Tuning_range, self.set_F_Tuning, "Rx Frequency tunining", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._F_Tuning_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._DelayTuning_range = qtgui.Range(0, (sps-1), 1, DelayTuningInicial, 200)
        self._DelayTuning_win = qtgui.RangeWidget(self._DelayTuning_range, self.set_DelayTuning, "Retardo antes de muestreo ", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._DelayTuning_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "Rx tunner", #name
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


        labels = ['Entrante', 'Saliente', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
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
        self.b_Eye_Diagram_0_0 = b_Eye_Diagram(
            AlphaLineas=AlphaLineasOjo,
            Delay_i=0,
            GrosorLineas=GrosorLineasOjo,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=sps,
            Title="Eye Diagramm. Parte Imaginaria",
            Ymax=0.2,
            Ymin=(-0.2),
        )

        self.top_grid_layout.addWidget(self.b_Eye_Diagram_0_0, 5, 0, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.b_Eye_Diagram_0 = b_Eye_Diagram(
            AlphaLineas=AlphaLineasOjo,
            Delay_i=0,
            GrosorLineas=GrosorLineasOjo,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=sps,
            Title="Eye Diagramm. Parte Real",
            Ymax=0.2,
            Ymin=(-0.2),
        )

        self.top_grid_layout.addWidget(self.b_Eye_Diagram_0, 4, 0, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._EyeDelay_range = qtgui.Range(0, (sps*4), 1, 0, 200)
        self._EyeDelay_win = qtgui.RangeWidget(self._EyeDelay_range, self.set_EyeDelay, "Retardo para Centrado del Ojo", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._EyeDelay_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_sampler_cc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.b_sampler_cc_0, 1), (self, 0))
        self.connect((self.b_sampler_cc_0, 0), (self.qtgui_const_sink_x_0_0_0, 1))
        self.connect((self.b_sampler_cc_0, 1), (self.qtgui_const_sink_x_0_0_0_0, 0))
        self.connect((self.b_tunner_0, 0), (self.b_sampler_cc_0, 0))
        self.connect((self.b_tunner_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.b_Eye_Diagram_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.b_Eye_Diagram_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.b_Eye_Diagram_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.b_Eye_Diagram_0_0, 1))
        self.connect((self, 0), (self.b_tunner_0, 0))
        self.connect((self, 0), (self.qtgui_const_sink_x_0_0_0, 0))


    def get_AlphaLineasOjo(self):
        return self.AlphaLineasOjo

    def set_AlphaLineasOjo(self, AlphaLineasOjo):
        self.AlphaLineasOjo = AlphaLineasOjo
        self.b_Eye_Diagram_0.set_AlphaLineas(self.AlphaLineasOjo)
        self.b_Eye_Diagram_0_0.set_AlphaLineas(self.AlphaLineasOjo)

    def get_DelayTuningInicial(self):
        return self.DelayTuningInicial

    def set_DelayTuningInicial(self, DelayTuningInicial):
        self.DelayTuningInicial = DelayTuningInicial
        self.set_DelayTuning(self.DelayTuningInicial)

    def get_GrosorLineasOjo(self):
        return self.GrosorLineasOjo

    def set_GrosorLineasOjo(self, GrosorLineasOjo):
        self.GrosorLineasOjo = GrosorLineasOjo
        self.b_Eye_Diagram_0.set_GrosorLineas(self.GrosorLineasOjo)
        self.b_Eye_Diagram_0_0.set_GrosorLineas(self.GrosorLineasOjo)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_0.set_Samprate(self.samp_rate)
        self.b_Eye_Diagram_0_0.set_Samprate(self.samp_rate)
        self.b_tunner_0.set_samp_rate(self.samp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.b_Eye_Diagram_0.set_Sps(self.sps)
        self.b_Eye_Diagram_0_0.set_Sps(self.sps)
        self.b_sampler_cc_0.set_Sps(self.sps)

    def get_PhiTuning(self):
        return self.PhiTuning

    def set_PhiTuning(self, PhiTuning):
        self.PhiTuning = PhiTuning
        self.b_tunner_0.set_phi(self.PhiTuning)

    def get_F_Tuning(self):
        return self.F_Tuning

    def set_F_Tuning(self, F_Tuning):
        self.F_Tuning = F_Tuning
        self.b_tunner_0.set_fdesv((-self.F_Tuning))

    def get_EyeDelay(self):
        return self.EyeDelay

    def set_EyeDelay(self, EyeDelay):
        self.EyeDelay = EyeDelay

    def get_DelayTuning(self):
        return self.DelayTuning

    def set_DelayTuning(self, DelayTuning):
        self.DelayTuning = DelayTuning
        self.b_tunner_0.set_NDelay(self.DelayTuning)

