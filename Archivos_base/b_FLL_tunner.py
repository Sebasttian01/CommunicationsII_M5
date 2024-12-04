# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_FLL_tunner
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Description: Recibe una senal digital con modulacion basada en constelaciones, luego de pasar por un canal que introduce desviaciones en fase y frecuencia, para entregar una constelacion estable, pues corrige esas desviaciones. Parametros usados: Constellation Object - es el modelo que contiene toda la informacion de la constelacion usada, lo cual sirve de base para poder realizar las correcciones. El constellation Object se puede crear mediante el bloque "Constellation Object"
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import math
import threading







class b_FLL_tunner(gr.hier_block2):
    def __init__(self, ConstellationObject=0):
        gr.hier_block2.__init__(
            self, "b_FLL_tunner",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.ConstellationObject = ConstellationObject

        ##################################################
        # Blocks
        ##################################################

        self.digital_constellation_receiver_cb_0 = digital.constellation_receiver_cb(ConstellationObject, (2*math.pi/100.0), (-0.25), 0.25)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_constellation_receiver_cb_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_constellation_receiver_cb_0, 3), (self.blocks_null_sink_0, 2))
        self.connect((self.digital_constellation_receiver_cb_0, 2), (self.blocks_null_sink_0, 1))
        self.connect((self.digital_constellation_receiver_cb_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.digital_constellation_receiver_cb_0, 4), (self, 0))
        self.connect((self, 0), (self.digital_constellation_receiver_cb_0, 0))


    def get_ConstellationObject(self):
        return self.ConstellationObject

    def set_ConstellationObject(self, ConstellationObject):
        self.ConstellationObject = ConstellationObject

