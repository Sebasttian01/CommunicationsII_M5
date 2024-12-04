# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_sampler_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGIS Universidad Industrial de Santander
# Description: Hace lo mismo que el b_sampler, pero con senales complejas. Por una salida entrega la senal diezmada y por la otra muestreada. El diezmado se realiza  de la manera en que se explica el diezmado en el libro de Tratamiento de Senales y Sistemas de Oppenheim. En ese diezmado se igualan a cero periodicamente un grupo de muestras. El muestreo, que se entrega en la otra salida de este bloque es similar al diezmado, pero las muestras que se igualan a cero son anuladas, es decir, desaparecen de la senal. Por esa razon, la rata de muestreo de la senal diezmada es la misma de la que entra al bloque, pero la rata de muestreo de la senal muestreada es Sps veces menor.
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_sampler import b_sampler  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import threading







class b_sampler_cc(gr.hier_block2):
    def __init__(self, DelayDiez=0, Sps=1):
        gr.hier_block2.__init__(
            self, "b_sampler_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.DelayDiez = DelayDiez
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.b_sampler_0_0_0 = b_sampler(
            DelayDiez=DelayDiez,
            Sps=Sps,
        )
        self.b_sampler_0_0 = b_sampler(
            DelayDiez=DelayDiez,
            Sps=Sps,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_sampler_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.b_sampler_0_0, 1), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.b_sampler_0_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.b_sampler_0_0_0, 1), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.b_sampler_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.b_sampler_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 1))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))


    def get_DelayDiez(self):
        return self.DelayDiez

    def set_DelayDiez(self, DelayDiez):
        self.DelayDiez = DelayDiez
        self.b_sampler_0_0.set_DelayDiez(self.DelayDiez)
        self.b_sampler_0_0_0.set_DelayDiez(self.DelayDiez)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.b_sampler_0_0.set_Sps(self.Sps)
        self.b_sampler_0_0_0.set_Sps(self.Sps)

