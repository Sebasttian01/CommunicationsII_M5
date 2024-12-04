# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_Eye_Diagram_simple_c
# Author: Done by: Homero Ortega Boada. Universidad Industrial de Santander
# Description: Let you to see the eye diagram of complex signals. Parametros usados: Delay_i - es un retardo para que el ojo se centre al gusto del usuario
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
import sip
import threading







class b_Eye_Diagram_simple_c(gr.hier_block2, Qt.QWidget):
    def __init__(self, AlphaLineas=0.5, Delay_i=0, GrosorLineas=20, Kint=1, N_eyes=2, Samprate1=1000, Sps1=64, Title="Eye Diagramm", Ymax=2, Ymin=(-2)):
        gr.hier_block2.__init__(
            self, "b_Eye_Diagram_simple_c",
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
        self.AlphaLineas = AlphaLineas
        self.Delay_i = Delay_i
        self.GrosorLineas = GrosorLineas
        self.Kint = Kint
        self.N_eyes = N_eyes
        self.Samprate1 = Samprate1
        self.Sps1 = Sps1
        self.Title = Title
        self.Ymax = Ymax
        self.Ymin = Ymin

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = Title
        self.Sps = Sps = Sps1*Kint
        self.Samprate = Samprate = Samprate1*Kint
        self.Delay = Delay = Delay_i

        ##################################################
        # Blocks
        ##################################################

        self._Delay_range = qtgui.Range(0, Sps, 1, Delay_i, 200)
        self._Delay_win = qtgui.RangeWidget(self._Delay_range, self.set_Delay, "Mueva aqui para Centrar el Ojo", "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Delay_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("Diagrama de Ojo "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=Kint,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
            (int(Sps*N_eyes)), #size
            Samprate, #samp_rate
            'Im.'+Title, #name
            10, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(Ymin, Ymax)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)


        labels = ['D', 'D', 'D', 'D', 'D',
            'D', 'D', 'D', 'D', 'D']
        widths = [GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas,
            GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas,
            AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(10):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            (int(Sps*N_eyes)), #size
            Samprate, #samp_rate
            'Re.'+Title, #name
            10, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(Ymin, Ymax)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['D', 'D', 'D', 'D', 'D',
            'D', 'D', 'D', 'D', 'D']
        widths = [GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas,
            GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas, GrosorLineas]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas,
            AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas, AlphaLineas]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(10):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_delay_0_7 = blocks.delay(gr.sizeof_float*1, (Sps*2+Delay))
        self.blocks_delay_0_6_0 = blocks.delay(gr.sizeof_float*1, (Sps*1+Delay))
        self.blocks_delay_0_6 = blocks.delay(gr.sizeof_float*1, (Sps*1+Delay))
        self.blocks_delay_0_5_0 = blocks.delay(gr.sizeof_float*1, (Sps*8+Delay))
        self.blocks_delay_0_5 = blocks.delay(gr.sizeof_float*1, (Sps*8+Delay))
        self.blocks_delay_0_4_0 = blocks.delay(gr.sizeof_float*1, (Sps*7+Delay))
        self.blocks_delay_0_4 = blocks.delay(gr.sizeof_float*1, (Sps*7+Delay))
        self.blocks_delay_0_3_1 = blocks.delay(gr.sizeof_float*1, (Sps*6+Delay))
        self.blocks_delay_0_3_0_1 = blocks.delay(gr.sizeof_float*1, (Sps*9+Delay))
        self.blocks_delay_0_3_0_0_0 = blocks.delay(gr.sizeof_float*1, Delay)
        self.blocks_delay_0_3_0_0 = blocks.delay(gr.sizeof_float*1, Delay)
        self.blocks_delay_0_3_0 = blocks.delay(gr.sizeof_float*1, (Sps*9+Delay))
        self.blocks_delay_0_3 = blocks.delay(gr.sizeof_float*1, (Sps*6+Delay))
        self.blocks_delay_0_2_0 = blocks.delay(gr.sizeof_float*1, (Sps*5+Delay))
        self.blocks_delay_0_2 = blocks.delay(gr.sizeof_float*1, (Sps*5+Delay))
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_float*1, (Sps*4+Delay))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, (Sps*4+Delay))
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, (Sps*3+Delay))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, (Sps*3+Delay))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, (Sps*2+Delay))
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_1_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_2, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_2_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_3, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_3_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_3_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_3_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_3_0_1, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_3_1, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_4, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_4_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_5, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_5_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_delay_0_6, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_6_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_7, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 2))
        self.connect((self.blocks_delay_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 2))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_0_0, 3))
        self.connect((self.blocks_delay_0_1_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 3))
        self.connect((self.blocks_delay_0_2, 0), (self.qtgui_time_sink_x_0_0_0, 4))
        self.connect((self.blocks_delay_0_2_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 4))
        self.connect((self.blocks_delay_0_3, 0), (self.qtgui_time_sink_x_0_0_0, 5))
        self.connect((self.blocks_delay_0_3_0, 0), (self.qtgui_time_sink_x_0_0_0, 8))
        self.connect((self.blocks_delay_0_3_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 9))
        self.connect((self.blocks_delay_0_3_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 9))
        self.connect((self.blocks_delay_0_3_0_1, 0), (self.qtgui_time_sink_x_0_0_0_0, 8))
        self.connect((self.blocks_delay_0_3_1, 0), (self.qtgui_time_sink_x_0_0_0_0, 5))
        self.connect((self.blocks_delay_0_4, 0), (self.qtgui_time_sink_x_0_0_0, 6))
        self.connect((self.blocks_delay_0_4_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 6))
        self.connect((self.blocks_delay_0_5, 0), (self.qtgui_time_sink_x_0_0_0, 7))
        self.connect((self.blocks_delay_0_5_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 7))
        self.connect((self.blocks_delay_0_6, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_delay_0_6_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_delay_0_7, 0), (self.qtgui_time_sink_x_0_0_0_0, 1))
        self.connect((self, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0_0, 0))


    def get_AlphaLineas(self):
        return self.AlphaLineas

    def set_AlphaLineas(self, AlphaLineas):
        self.AlphaLineas = AlphaLineas

    def get_Delay_i(self):
        return self.Delay_i

    def set_Delay_i(self, Delay_i):
        self.Delay_i = Delay_i
        self.set_Delay(self.Delay_i)

    def get_GrosorLineas(self):
        return self.GrosorLineas

    def set_GrosorLineas(self, GrosorLineas):
        self.GrosorLineas = GrosorLineas

    def get_Kint(self):
        return self.Kint

    def set_Kint(self, Kint):
        self.Kint = Kint
        self.set_Samprate(self.Samprate1*self.Kint)
        self.set_Sps(self.Sps1*self.Kint)

    def get_N_eyes(self):
        return self.N_eyes

    def set_N_eyes(self, N_eyes):
        self.N_eyes = N_eyes

    def get_Samprate1(self):
        return self.Samprate1

    def set_Samprate1(self, Samprate1):
        self.Samprate1 = Samprate1
        self.set_Samprate(self.Samprate1*self.Kint)

    def get_Sps1(self):
        return self.Sps1

    def set_Sps1(self, Sps1):
        self.Sps1 = Sps1
        self.set_Sps(self.Sps1*self.Kint)

    def get_Title(self):
        return self.Title

    def set_Title(self, Title):
        self.Title = Title
        self.set_variable_qtgui_label_0(self.Title)

    def get_Ymax(self):
        return self.Ymax

    def set_Ymax(self, Ymax):
        self.Ymax = Ymax
        self.qtgui_time_sink_x_0_0_0.set_y_axis(self.Ymin, self.Ymax)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(self.Ymin, self.Ymax)

    def get_Ymin(self):
        return self.Ymin

    def set_Ymin(self, Ymin):
        self.Ymin = Ymin
        self.qtgui_time_sink_x_0_0_0.set_y_axis(self.Ymin, self.Ymax)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(self.Ymin, self.Ymax)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0))))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.blocks_delay_0.set_dly(int((self.Sps*2+self.Delay)))
        self.blocks_delay_0_0.set_dly(int((self.Sps*3+self.Delay)))
        self.blocks_delay_0_0_0.set_dly(int((self.Sps*3+self.Delay)))
        self.blocks_delay_0_1.set_dly(int((self.Sps*4+self.Delay)))
        self.blocks_delay_0_1_0.set_dly(int((self.Sps*4+self.Delay)))
        self.blocks_delay_0_2.set_dly(int((self.Sps*5+self.Delay)))
        self.blocks_delay_0_2_0.set_dly(int((self.Sps*5+self.Delay)))
        self.blocks_delay_0_3.set_dly(int((self.Sps*6+self.Delay)))
        self.blocks_delay_0_3_0.set_dly(int((self.Sps*9+self.Delay)))
        self.blocks_delay_0_3_0_1.set_dly(int((self.Sps*9+self.Delay)))
        self.blocks_delay_0_3_1.set_dly(int((self.Sps*6+self.Delay)))
        self.blocks_delay_0_4.set_dly(int((self.Sps*7+self.Delay)))
        self.blocks_delay_0_4_0.set_dly(int((self.Sps*7+self.Delay)))
        self.blocks_delay_0_5.set_dly(int((self.Sps*8+self.Delay)))
        self.blocks_delay_0_5_0.set_dly(int((self.Sps*8+self.Delay)))
        self.blocks_delay_0_6.set_dly(int((self.Sps*1+self.Delay)))
        self.blocks_delay_0_6_0.set_dly(int((self.Sps*1+self.Delay)))
        self.blocks_delay_0_7.set_dly(int((self.Sps*2+self.Delay)))

    def get_Samprate(self):
        return self.Samprate

    def set_Samprate(self, Samprate):
        self.Samprate = Samprate
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.Samprate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.Samprate)

    def get_Delay(self):
        return self.Delay

    def set_Delay(self, Delay):
        self.Delay = Delay
        self.blocks_delay_0.set_dly(int((self.Sps*2+self.Delay)))
        self.blocks_delay_0_0.set_dly(int((self.Sps*3+self.Delay)))
        self.blocks_delay_0_0_0.set_dly(int((self.Sps*3+self.Delay)))
        self.blocks_delay_0_1.set_dly(int((self.Sps*4+self.Delay)))
        self.blocks_delay_0_1_0.set_dly(int((self.Sps*4+self.Delay)))
        self.blocks_delay_0_2.set_dly(int((self.Sps*5+self.Delay)))
        self.blocks_delay_0_2_0.set_dly(int((self.Sps*5+self.Delay)))
        self.blocks_delay_0_3.set_dly(int((self.Sps*6+self.Delay)))
        self.blocks_delay_0_3_0.set_dly(int((self.Sps*9+self.Delay)))
        self.blocks_delay_0_3_0_0.set_dly(int(self.Delay))
        self.blocks_delay_0_3_0_0_0.set_dly(int(self.Delay))
        self.blocks_delay_0_3_0_1.set_dly(int((self.Sps*9+self.Delay)))
        self.blocks_delay_0_3_1.set_dly(int((self.Sps*6+self.Delay)))
        self.blocks_delay_0_4.set_dly(int((self.Sps*7+self.Delay)))
        self.blocks_delay_0_4_0.set_dly(int((self.Sps*7+self.Delay)))
        self.blocks_delay_0_5.set_dly(int((self.Sps*8+self.Delay)))
        self.blocks_delay_0_5_0.set_dly(int((self.Sps*8+self.Delay)))
        self.blocks_delay_0_6.set_dly(int((self.Sps*1+self.Delay)))
        self.blocks_delay_0_6_0.set_dly(int((self.Sps*1+self.Delay)))
        self.blocks_delay_0_7.set_dly(int((self.Sps*2+self.Delay)))

