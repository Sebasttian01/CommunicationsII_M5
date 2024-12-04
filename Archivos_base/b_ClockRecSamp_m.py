# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_ClockRecSamp_m
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Es un Clock o Timming Recovery con muestreo pero manual. Recibe una senal con modulacion digital basada en constelaciones, que llega sobremuestreada a la razon de Sps muestras por simbolo, proveniente de un canal, usted selecciona manualmente el mejor instante de muestreo con la ayuda de un diagrama de ojo que este bloque le brinda, selecciona el instante en que el ojo aparece mas abierto, finalmente el bloque produce la senal muestreada en el instante seleccionado por usted. En este sentido, este bloque es un decimador, pues por cada Sps muestras produce solo una. Entrega entonces una senal con una frecuencia de muestreo igual a la rata de simbolos. Parametros usados: samp_rate (Hz) - es la rata de muestreo de la senal recibida; Sps (muestras) - es el numero de muestras por simbolo que trae la senal entrante
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import QtCore
from b_Eye_Diagram_c import b_Eye_Diagram_c  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import E3TRadio
import sip
import threading







class b_ClockRecSamp_m(gr.hier_block2, Qt.QWidget):
    def __init__(self, Sps=64, samp_rate=64):
        gr.hier_block2.__init__(
            self, "b_ClockRecSamp_m",
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
        self.Sps = Sps
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.TimingDelay = TimingDelay = 0
        self.Delay = Delay = Sps-TimingDelay

        ##################################################
        # Blocks
        ##################################################

        self._TimingDelay_range = qtgui.Range(0, (Sps-1), 1, 0, 200)
        self._TimingDelay_win = qtgui.RangeWidget(self._TimingDelay_range, self.set_TimingDelay, "Seleccione instante en que ojo esta mas abierto", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._TimingDelay_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            '', #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-1.5), 1.5)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2.5), 2.5)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['Recibida', 'Muestreada', '', '', '',
            '', '', '', '', '']
        widths = [1, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["black", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=TimingDelay,
            Sps=Sps,
        )
        self.b_Eye_Diagram_c_0 = b_Eye_Diagram_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=1.5,
            Ymin=(-1.5),
        )

        self.top_grid_layout.addWidget(self.b_Eye_Diagram_c_0, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.E3TRadio_zero_order_hold2_cc_0 = E3TRadio.zero_order_hold2_cc(Sps)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_zero_order_hold2_cc_0, 0), (self.qtgui_const_sink_x_0_0, 1))
        self.connect((self.b_sampler_cc_0, 1), (self.E3TRadio_zero_order_hold2_cc_0, 0))
        self.connect((self.b_sampler_cc_0, 0), (self.b_Eye_Diagram_c_0, 0))
        self.connect((self.b_sampler_cc_0, 1), (self, 0))
        self.connect((self, 0), (self.b_Eye_Diagram_c_0, 1))
        self.connect((self, 0), (self.b_sampler_cc_0, 0))
        self.connect((self, 0), (self.qtgui_const_sink_x_0_0, 0))


    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Delay(self.Sps-self.TimingDelay)
        self.E3TRadio_zero_order_hold2_cc_0.set_retardo(self.Sps)
        self.b_Eye_Diagram_c_0.set_Sps(self.Sps)
        self.b_sampler_cc_0.set_Sps(self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_c_0.set_Samprate(self.samp_rate)

    def get_TimingDelay(self):
        return self.TimingDelay

    def set_TimingDelay(self, TimingDelay):
        self.TimingDelay = TimingDelay
        self.set_Delay(self.Sps-self.TimingDelay)
        self.b_sampler_cc_0.set_DelayDiez(self.TimingDelay)

    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay

