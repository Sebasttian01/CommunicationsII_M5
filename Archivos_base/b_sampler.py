# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_sampler
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Por una salida entrega la senal diezmada y por la otra muestreada. El diezmado se realiza  de la manera en que se explica el diezmado en el libro de Tratamiento de Senales y Sistemas de Oppenheim. En ese diezmado se igualan a cero periodicamente un grupo de muestras. El muestreo, que se entrega en la otra salida de este bloque es similar al diezmado, pero las muestras que se igualan a cero son anuladas, es decir, desaparecen de la senal. Por esa razon, la rata de muestreo de la senal diezmada es la misma de la que entra al bloque, pero la rata de muestreo de la senal muestreada es Sps veces menor.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import E3TRadio
import threading







class b_sampler(gr.hier_block2):
    def __init__(self, DelayDiez=0, Sps=64):
        gr.hier_block2.__init__(
            self, "b_sampler",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.DelayDiez = DelayDiez
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.E3TRadio_diezmoppenh3_ff_0 = E3TRadio.diezmoppenh3_ff(Sps, DelayDiez)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, DelayDiez)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self, 0))
        self.connect((self.E3TRadio_diezmoppenh3_ff_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.E3TRadio_diezmoppenh3_ff_0, 0), (self, 1))
        self.connect((self, 0), (self.E3TRadio_diezmoppenh3_ff_0, 0))


    def get_DelayDiez(self):
        return self.DelayDiez

    def set_DelayDiez(self, DelayDiez):
        self.DelayDiez = DelayDiez
        self.E3TRadio_diezma_ff_0.set_ka(self.DelayDiez)
        self.E3TRadio_diezmoppenh3_ff_0.set_ka(self.DelayDiez)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps

