# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_de_ds_spreadspect_cc
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: multiplica la entrada dsss por codigo para producir una senal inversa al Direc Sequence Spread Spectrum (DSSS). El cuidado que hay que tener es que el Spreading Factor (SF) se cuadra desde afuera, para la cual la senal de la informacion debe entrar con un sobremuestreo SF. Los parametros usados son: codigo - es el codigo que se usara para producir la senal DSSS; CodeDelay (muestras) permite introducir un retrazo en la aplicacion del codigo lo cual es util para tener en cuenta que la senal a des ensanchar puede llegar con un retrazo
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from b_accum_cc import b_accum_cc  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
import threading







class b_de_ds_spreadspect_cc(gr.hier_block2):
    def __init__(self, ChipsSysDelay=0, SF=8, codigo=(1,1,1,1,1,1,1,1)):
        gr.hier_block2.__init__(
            self, "b_de_ds_spreadspect_cc",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(5, 5, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.ChipsSysDelay = ChipsSysDelay
        self.SF = SF
        self.codigo = codigo

        ##################################################
        # Variables
        ##################################################
        self.AccDelay = AccDelay = int((float(ChipsSysDelay)/SF-ChipsSysDelay/SF)*SF)
        self.SamplerDelay = SamplerDelay = ((AccDelay+SF-1)/SF-int((AccDelay+SF-1)/SF))*SF

        ##################################################
        # Blocks
        ##################################################

        self.blocks_vector_source_x_0 = blocks.vector_source_c(codigo, True, 1, [])
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1./SF)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, ChipsSysDelay)
        self.b_sampler_cc_0 = b_sampler_cc(
            DelayDiez=SamplerDelay,
            Sps=SF,
        )
        self.b_accum_cc_0 = b_accum_cc(
            M=AccDelay,
            N=SF,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_accum_cc_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.b_sampler_cc_0, 1), (self, 0))
        self.connect((self.b_sampler_cc_0, 0), (self, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self, 4))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_sampler_cc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 3))
        self.connect((self.blocks_multiply_xx_0, 0), (self.b_accum_cc_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 2))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.blocks_multiply_xx_0, 0))


    def get_ChipsSysDelay(self):
        return self.ChipsSysDelay

    def set_ChipsSysDelay(self, ChipsSysDelay):
        self.ChipsSysDelay = ChipsSysDelay
        self.set_AccDelay(int((float(self.ChipsSysDelay)/self.SF-self.ChipsSysDelay/self.SF)*self.SF))
        self.blocks_delay_0.set_dly(int(self.ChipsSysDelay))

    def get_SF(self):
        return self.SF

    def set_SF(self, SF):
        self.SF = SF
        self.set_AccDelay(int((float(self.ChipsSysDelay)/self.SF-self.ChipsSysDelay/self.SF)*self.SF))
        self.set_SamplerDelay(((self.AccDelay+self.SF-1)/self.SF-int((self.AccDelay+self.SF-1)/self.SF))*self.SF)
        self.b_accum_cc_0.set_N(self.SF)
        self.b_sampler_cc_0.set_Sps(self.SF)
        self.blocks_multiply_const_vxx_0.set_k(1./self.SF)

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
        self.blocks_vector_source_x_0.set_data(self.codigo, [])

    def get_AccDelay(self):
        return self.AccDelay

    def set_AccDelay(self, AccDelay):
        self.AccDelay = AccDelay
        self.set_SamplerDelay(((self.AccDelay+self.SF-1)/self.SF-int((self.AccDelay+self.SF-1)/self.SF))*self.SF)
        self.b_accum_cc_0.set_M(self.AccDelay)

    def get_SamplerDelay(self):
        return self.SamplerDelay

    def set_SamplerDelay(self, SamplerDelay):
        self.SamplerDelay = SamplerDelay
        self.b_sampler_cc_0.set_DelayDiez(self.SamplerDelay)

