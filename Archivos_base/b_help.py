# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_help
# Author: Homero Ortega Boada
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Guardando aqui todos los bloques de programacion embebida
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import b_help_wform as wform  # embedded python module
import threading







class b_help(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_help",
                gr.io_signature(0, 0, 0),
                gr.io_signature(0, 0, 0),
        )

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000




    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

