# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_antennaarraylinearz_3d
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
import numpy
import threading







class b_antennaarraylinearz_3d(gr.hier_block2):
    def __init__(self, Dz=0.5, phi_i_gr=numpy.linspace(-numpy.pi, numpy.pi, 10), theta_i_gr=numpy.array([0,1,2,3])):
        gr.hier_block2.__init__(
            self, "b_antennaarraylinearz_3d",
                gr.io_signature.makev(4, 4, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Dz = Dz
        self.phi_i_gr = phi_i_gr
        self.theta_i_gr = theta_i_gr

        ##################################################
        # Variables
        ##################################################
        self.N = N = 4
        self.distancias = distancias = Dz*numpy.array(range(N))
        self.fases = fases = -2*numpy.pi*distancias*numpy.cos(theta_i_gr*numpy.pi/180)
        self.L_angu = L_angu = 10

        ##################################################
        # Blocks
        ##################################################

        self.blocks_multiply_const_vxx_1_2 = blocks.multiply_const_cc(numpy.exp(1j*fases[3]))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_cc(numpy.exp(1j*fases[2]))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(numpy.exp(1j*fases[1]))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(numpy.exp(1j*fases[0]))
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self, 1), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self, 2), (self.blocks_multiply_const_vxx_1_2, 0))
        self.connect((self, 3), (self.blocks_multiply_const_vxx_1_1, 0))


    def get_Dz(self):
        return self.Dz

    def set_Dz(self, Dz):
        self.Dz = Dz
        self.set_distancias(self.Dz*numpy.array(range(self.N)))

    def get_phi_i_gr(self):
        return self.phi_i_gr

    def set_phi_i_gr(self, phi_i_gr):
        self.phi_i_gr = phi_i_gr

    def get_theta_i_gr(self):
        return self.theta_i_gr

    def set_theta_i_gr(self, theta_i_gr):
        self.theta_i_gr = theta_i_gr
        self.set_fases(-2*numpy.pi*self.distancias*numpy.cos(self.theta_i_gr*numpy.pi/180))

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_distancias(self.Dz*numpy.array(range(self.N)))

    def get_distancias(self):
        return self.distancias

    def set_distancias(self, distancias):
        self.distancias = distancias
        self.set_fases(-2*numpy.pi*self.distancias*numpy.cos(self.theta_i_gr*numpy.pi/180))

    def get_fases(self):
        return self.fases

    def set_fases(self, fases):
        self.fases = fases
        self.blocks_multiply_const_vxx_1.set_k(numpy.exp(1j*self.fases[0]))
        self.blocks_multiply_const_vxx_1_0.set_k(numpy.exp(1j*self.fases[1]))
        self.blocks_multiply_const_vxx_1_1.set_k(numpy.exp(1j*self.fases[2]))
        self.blocks_multiply_const_vxx_1_2.set_k(numpy.exp(1j*self.fases[3]))

    def get_L_angu(self):
        return self.L_angu

    def set_L_angu(self, L_angu):
        self.L_angu = L_angu

