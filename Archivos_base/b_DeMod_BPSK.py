# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: b_DeMod_BPSK
# Author: Homero Ortega Boada. Universidad Industrial de Santander
# Copyright: Grupo RadioGis Universidad Industrial de Santander
# Description: Permite demodular una senal BPSK de manera pedagogica para qeue los estudiantes comprendan el proceso interno
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
import E3TRadio
import threading







class b_DeMod_BPSK(gr.hier_block2):
    def __init__(self, DelayAcc=2, DelayDiez=4, Sps=8):
        gr.hier_block2.__init__(
            self, "b_DeMod_BPSK",
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
                gr.io_signature.makev(5, 5, [gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.DelayAcc = DelayAcc
        self.DelayDiez = DelayDiez
        self.Sps = Sps

        ##################################################
        # Blocks
        ##################################################

        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.b_sampler_0 = b_sampler(
            DelayDiez=DelayDiez,
            Sps=Sps,
        )
        self.E3TRadio_decisor_ff_0 = E3TRadio.decisor_ff(0.)
        self.E3TRadio_acumulador_truncado_ff_0 = E3TRadio.acumulador_truncado_ff(Sps,DelayAcc)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_acumulador_truncado_ff_0, 0), (self.b_sampler_0, 0))
        self.connect((self.E3TRadio_acumulador_truncado_ff_0, 0), (self, 3))
        self.connect((self.E3TRadio_decisor_ff_0, 0), (self, 0))
        self.connect((self.b_sampler_0, 0), (self.E3TRadio_decisor_ff_0, 0))
        self.connect((self.b_sampler_0, 0), (self, 1))
        self.connect((self.b_sampler_0, 1), (self, 2))
        self.connect((self.blocks_complex_to_float_0, 0), (self.E3TRadio_acumulador_truncado_ff_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self, 4))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))


    def get_DelayAcc(self):
        return self.DelayAcc

    def set_DelayAcc(self, DelayAcc):
        self.DelayAcc = DelayAcc
        self.E3TRadio_acumulador_truncado_ff_0.set_ka(self.DelayAcc)

    def get_DelayDiez(self):
        return self.DelayDiez

    def set_DelayDiez(self, DelayDiez):
        self.DelayDiez = DelayDiez
        self.b_sampler_0.set_DelayDiez(self.DelayDiez)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.b_sampler_0.set_Sps(self.Sps)

