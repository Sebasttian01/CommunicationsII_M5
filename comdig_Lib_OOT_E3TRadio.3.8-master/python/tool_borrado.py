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

class decisor_ff_old(gr.sync_block):
    """
    Entrega como salida 1 si la entrada supera el umbral. 0 si no lo supera. Tanto la entrada como la salida es un valor de tipo float
    """
    def __init__(self, Umbral=0):
        gr.sync_block.__init__(self,
            name="decisor_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.Umbral=Umbral


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        a=numpy.zeros(len(in0))
        # <+signal processing here+>
        for i in range(0,len(in0)):
            if in0[i]>self.Umbral:
                a[i]=1.
            else:
                a[i]=0.

        out[:] = a
        return len(output_items[0])

