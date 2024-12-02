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

class v_delay(gr.sync_block):
    """
    toma un vector de tamano N y devuelve un vector igual pero con un corrimiento de M muestras. Usa una memoria interna para que no se pierdan las muestras que se salgan del vector por el corrimiento.
    
    CORREGIR: deberia llamarse v_delay_ff
    """
    def __init__(self, N, M):
        self.N=N  # Es el tamano del vector de entrada y a la vez el max retardo posible
        self.M=M  # es el numero de muestras del retrazo deseado
        self.mem=numpy.zeros(self.N)

        gr.sync_block.__init__(self,
            name="v_delay",
            in_sig=[(numpy.float32, self.N)],
            out_sig=[(numpy.float32, self.N)])


    def work(self, input_items, output_items):
        in0 = input_items[0][0,:]
#        in0 = input_items[0]
        print(in0.shape)
        out = output_items[0]
#        print("out ", out.shape)
#        print("in  ", in0.shape)
        # <+signal processing here+>

        out[0:self.M:]=self.mem[0:self.M:]
        out[self.M:self.N:]=in0[0:self.N-self.M:]
        self.mem[0:self.M:]=in0[self.N-self.M:self.N:]

        out[:]=o1
        return len(output_items[0])

    def set_delay(self, M):
        if M<=self.N:
            self.M=M
        else:
            self.M=self.N




