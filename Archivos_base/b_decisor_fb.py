# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_decisor_fb
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: para cada muestra entrante produce uno  si supera el Umbral=0, o cero en otro caso
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import threading







class b_decisor_fb(gr.hier_block2):
    def __init__(self):
        gr.hier_block2.__init__(
            self, "b_decisor_fb ",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Variables
        ##################################################
        self.Constelacion = Constelacion = [-1.+0.j ,1.+0.j,  ]
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist(Constelacion, (1,2),
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.MiconstellationObject.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject
        self.digital_constellation_decoder_cb_0.set_constellation(self.MiconstellationObject)

