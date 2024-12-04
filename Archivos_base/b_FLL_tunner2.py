# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_FLL_tunner2
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Description: Recibe una senal digital con modulacion basada en constelaciones, luego de pasar por un canal que introduce desviaciones en fase y frecuencia, para entregar una constelacion estable, pues corrige esas desviaciones. Parametros usados: Constellation - es el mvector que contiene los puntos de la constelacion usada, lo cual sirve de base para poder realizar las correcciones.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import math
import numpy as np
import threading







class b_FLL_tunner2(gr.hier_block2):
    def __init__(self, Constellation=(1,0)):
        gr.hier_block2.__init__(
            self, "b_FLL_tunner2",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Constellation = Constellation

        ##################################################
        # Variables
        ##################################################
        self.M = M = len(Constellation)
        self.my_constell_obj = my_constell_obj = digital.constellation_calcdist(Constellation, np.arange(0,M),
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.my_constell_obj.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.digital_constellation_receiver_cb_0 = digital.constellation_receiver_cb(my_constell_obj, (2*math.pi/100.0), (-0.25), 0.25)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_constellation_receiver_cb_0, 2), (self.blocks_null_sink_0, 1))
        self.connect((self.digital_constellation_receiver_cb_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_constellation_receiver_cb_0, 3), (self.blocks_null_sink_0, 2))
        self.connect((self.digital_constellation_receiver_cb_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.digital_constellation_receiver_cb_0, 4), (self, 0))
        self.connect((self, 0), (self.digital_constellation_receiver_cb_0, 0))


    def get_Constellation(self):
        return self.Constellation

    def set_Constellation(self, Constellation):
        self.Constellation = Constellation
        self.set_M(len(self.Constellation))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M

    def get_my_constell_obj(self):
        return self.my_constell_obj

    def set_my_constell_obj(self, my_constell_obj):
        self.my_constell_obj = my_constell_obj

