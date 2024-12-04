# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: s
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Etiqueta de salida. Para no tener que hacer tantas interconexiones
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class s(gr.hier_block2):
    def __init__(self, I=0):
        gr.hier_block2.__init__(
            self, "s",
                gr.io_signature(1, 1, 0*1),
                gr.io_signature(0, 0, 0),
        )

        ##################################################
        # Parameters
        ##################################################
        self.I = I




    def get_I(self):
        return self.I

    def set_I(self, I):
        self.I = I

