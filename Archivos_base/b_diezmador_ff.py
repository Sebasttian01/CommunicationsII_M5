# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_diezmador_ff
# Author: Homero Ortega
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_diezmador_ff(gr.hier_block2):
    def __init__(self, Paso=2):
        gr.hier_block2.__init__(
            self, "b_diezmador_ff",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Paso = Paso

        ##################################################
        # Blocks
        ##################################################

        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.E3TRadio_diezmador_cc_0 = E3TRadio.diezmador_cc(Paso)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezmador_cc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.E3TRadio_diezmador_cc_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))


    def get_Paso(self):
        return self.Paso

    def set_Paso(self, Paso):
        self.Paso = Paso

