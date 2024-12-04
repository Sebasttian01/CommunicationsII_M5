# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_antennaarraylinearz_p
# Author: Homero Ortega
# Copyright: Grupo de Investigacion RadioGIS Universidad Industrial de Santander
# Description: Simula el comportamiento del hardware de un arreglo de antenas más basico que es el caso en que los radiadores están dispuestos de manera lineal, sobre el eje z, donde Dz es la distancia entre los radiadores dada en longitudes de onda, por ejemplo Dz=0.5 significa media longitud de onda. N es el numeo de radiadores, distancias es la distantacia desde z=0 hasta cada radiador; fases son los desfases que sufre cada señal para llegar a un punto de observación ubicado en un angulo theta_i
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
import b_antennaarraylinearz_p_epy_block_0 as epy_block_0  # embedded python block
import numpy as np
import threading







class b_antennaarraylinearz_p(gr.hier_block2):
    def __init__(self, Dz=0.5, phi_i_gr=0):
        gr.hier_block2.__init__(
            self, "b_antennaarraylinearz_p",
                gr.io_signature.makev(5, 5, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_float*1, gr.sizeof_gr_complex*1]),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Dz = Dz
        self.phi_i_gr = phi_i_gr

        ##################################################
        # Variables
        ##################################################
        self.N = N = 4
        self.distancias = distancias = Dz*np.array(range(N))

        ##################################################
        # Blocks
        ##################################################

        self.epy_block_0 = epy_block_0.blk(N=N, distancias=distancias)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.epy_block_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.epy_block_0, 1), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.epy_block_0, 2), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.epy_block_0, 3), (self.blocks_multiply_xx_0_0_0_0, 1))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self, 2), (self.blocks_multiply_xx_0_0_0_0, 0))
        self.connect((self, 3), (self.epy_block_0, 0))
        self.connect((self, 4), (self.blocks_multiply_xx_0_0_0, 0))


    def get_Dz(self):
        return self.Dz

    def set_Dz(self, Dz):
        self.Dz = Dz
        self.set_distancias(self.Dz*np.array(range(self.N)))

    def get_phi_i_gr(self):
        return self.phi_i_gr

    def set_phi_i_gr(self, phi_i_gr):
        self.phi_i_gr = phi_i_gr

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_distancias(self.Dz*np.array(range(self.N)))
        self.epy_block_0.N = self.N

    def get_distancias(self):
        return self.distancias

    def set_distancias(self, distancias):
        self.distancias = distancias
        self.epy_block_0.distancias = self.distancias

