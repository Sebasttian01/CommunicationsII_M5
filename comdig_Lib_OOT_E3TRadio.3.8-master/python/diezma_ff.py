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

class diezma_ff(gr.decim_block):
    """
    Realiza un diezmado del mundo real. N es la distancia entre las muestras a diezmar, M es el punto de inicio.
    El codigo esta en diezma_ff.py. Escrito por Homero Ortega. Universidad Industrial de Santander. Colombia. 

PARA CORREGIR: Una revision en 2020 determino qu el codigo de este bloque no esta optimizado a operaciones vectoriales. Un buen ejemplo de optimizacion es el bloque:diezmador_cc
    """
    def __init__(self, N,M):
        self.N=N
        self.M=M
        gr.decim_block.__init__(self,
            name="diezma_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], decim=N)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
#        print("Lo ",len(out))
#        print("Li ",len(in0))
# <+signal processing here+>
#        out=numpy.zeros(len(in0))
#        j=0
#        for i in range(0,len(in0)):

#            if in0[i] != 0:
#                out[j]=in0[i]
#                j += 1

        out[:] = in0[self.M::self.N]

        return len(output_items[0])

# La siguiente funcion sirve para cambiar en caliente el valor M
    def set_ka(self, M):
        self.M=M

