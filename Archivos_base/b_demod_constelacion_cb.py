# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_demod_constelacion_cb
# Author: Grupo RadioGis Universidad Industrial de Santander
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import numpy
import threading







class b_demod_constelacion_cb(gr.hier_block2):
    def __init__(self, Constelacion=[(1.41 + 1.41*1j),  (-1.41 + 1.41*1j), (-1.41 - 1.41*1j), (1.41 - 1.41*1j)]):
        gr.hier_block2.__init__(
            self, "b_demod_constelacion_cb",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Constelacion = Constelacion

        ##################################################
        # Variables
        ##################################################
        self.M = M = len(Constelacion)
        self.mapa = mapa = numpy.arange(M)
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist(Constelacion, mapa,
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.MiconstellationObject.set_npwr(1.0)

        ##################################################
        # Blocks
        ##################################################

        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self, 0))
        self.connect((self, 0), (self.digital_constellation_decoder_cb_0, 0))


    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_mapa(numpy.arange(self.M))

    def get_mapa(self):
        return self.mapa

    def set_mapa(self, mapa):
        self.mapa = mapa

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject
        self.digital_constellation_decoder_cb_0.set_constellation(self.MiconstellationObject)

