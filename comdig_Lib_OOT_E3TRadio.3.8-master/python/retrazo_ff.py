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

class retrazo_ff(gr.sync_block):
    """
    Retraza la senal R muestras de un maximo de Rmax. Nota Rmax debe ser mayor o igual al volumen maximo de datos que pueden tener los streams de entrada al bloque
    """
    def __init__(self, Rmax, R):
        gr.sync_block.__init__(self,
            name="retrazo_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        # El retrazo maximo, el actual y la memoria temporal
        self.Rmax=Rmax
        self.R=R
        self.Mem=numpy.zeros(Rmax)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        L=len(in0)
        # desplaza la memoria
        self.Mem[0:self.Rmax-L:]=self.Mem[L:self.Rmax]
        # la memoria recibe la entrada en cola
        self.Mem[self.Rmax-L:self.Rmax:]=in0[0:L:]
        # devuelve senal con retrazo
        out[0:L]=self.Mem[self.Rmax-L-self.R:self.Rmax-self.R]

        return len(output_items[0])

    def set_retardo(self, NuevoRetrazo):
        self.R=NuevoRetrazo


