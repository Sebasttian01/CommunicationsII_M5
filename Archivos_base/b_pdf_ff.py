# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_pdf_ff
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Hecho por Homero Ortega. Recibe an input with values between Xmin and Xmax and calculate the Probaility Density Function (PDF) dinamically.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import b_pdf_ff_pdf_ff as pdf_ff  # embedded python block
import sip
import threading







class b_pdf_ff(gr.hier_block2, Qt.QWidget):
    def __init__(self, EjeX='potencia', Xmax=4., Xmin=(-4.), pdf_max=0.025):
        gr.hier_block2.__init__(
            self, "b_pdf_ff",
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
        self.EjeX = EjeX
        self.Xmax = Xmax
        self.Xmin = Xmin
        self.pdf_max = pdf_max

        ##################################################
        # Variables
        ##################################################
        self.N = N = 1024

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_vector_sink_f_0_0_0 = qtgui.vector_sink_f(
            N,
            Xmin,
            ((Xmax-Xmin)/N),
            EjeX,
            "PDF",
            "Probability Density Function (PDF)",
            1, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(0., pdf_max)
        self.qtgui_vector_sink_f_0_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_ref_level(0)


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
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_win)
        self.pdf_ff = pdf_ff.e_pdf_ff(Xmin=Xmin, Xmax=Xmax, N=N)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, N)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.pdf_ff, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.pdf_ff, 0), (self.qtgui_vector_sink_f_0_0_0, 0))


    def get_EjeX(self):
        return self.EjeX

    def set_EjeX(self, EjeX):
        self.EjeX = EjeX

    def get_Xmax(self):
        return self.Xmax

    def set_Xmax(self, Xmax):
        self.Xmax = Xmax
        self.pdf_ff.Xmax = self.Xmax
        self.qtgui_vector_sink_f_0_0_0.set_x_axis(self.Xmin, ((self.Xmax-self.Xmin)/self.N))

    def get_Xmin(self):
        return self.Xmin

    def set_Xmin(self, Xmin):
        self.Xmin = Xmin
        self.pdf_ff.Xmin = self.Xmin
        self.qtgui_vector_sink_f_0_0_0.set_x_axis(self.Xmin, ((self.Xmax-self.Xmin)/self.N))

    def get_pdf_max(self):
        return self.pdf_max

    def set_pdf_max(self, pdf_max):
        self.pdf_max = pdf_max
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(0., self.pdf_max)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.pdf_ff.N = self.N
        self.qtgui_vector_sink_f_0_0_0.set_x_axis(self.Xmin, ((self.Xmax-self.Xmin)/self.N))

