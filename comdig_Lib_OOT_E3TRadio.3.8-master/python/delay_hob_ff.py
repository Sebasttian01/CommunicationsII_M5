#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class delay_hob_ff(gr.sync_block):
    """
    Retraza la senal. M es el numero de muestras
    de ese retrazo y N es el tope previsto como valor maximo para M. 
    Ese tope es previsto porque M puede ser variado en caliente. 
    Hecho por Homero Ortega, Universidad Industriald de Santander
    """
    def __init__(self, NN, M):
        gr.sync_block.__init__(self,
            name="delay_hob_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        # NN es el numero tope de muestras que se puede aceptar
        self.NN=NN
        self.M=M  # es el numero de muestras del retrazo deseado
        self.mem=numpy.zeros(NN)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>

        N=len(in0)
        out[0:self.M:]=self.mem[0:self.M:]
        out[self.M:N:]=in0[0:N-self.M:]
        self.mem[0:self.M:]=in0[N-self.M:N:]

        return len(output_items[0])

    def set_delay(self, M):
        if M<=self.NN:
            self.M=M
        else:
            self.M=self.NN



