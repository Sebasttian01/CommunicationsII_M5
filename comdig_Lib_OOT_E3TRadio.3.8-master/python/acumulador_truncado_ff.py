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
import math
from gnuradio import gr

class acumulador_truncado_ff(gr.sync_block):
    """ Es un acumulador que se resetea cada N muestras. El reseteo no implica retornar a cero sino a la amplitud de la primera muestra. Arranca en la muestra M y termina en la M+N-1. Este bloque es hecho en la E3T de la UIS. 
    
PARA CORREGIR: Una revision en 2020 determino que el codigo de este bloque no esta optimizado a operaciones vectoriales. Quiza buenos ejemplos sean el bloque averager, el power_meter y el vector_average_hob.
    """
    def __init__(self, N, M):

        self.N=N
        # Antes decia: self.M=M. Lo que ahora se ha hecho es que el valor M sea redondeado para que siempre sea menor a N
        self.M=int(math.fmod(M,N))
        self.accum=0
        self.count=0
    
        gr.sync_block.__init__(self,
            name="acumulador_truncado_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>
        for i in range (0,len(in0)):

            # El algoritmo 
            if self.count == self.M:
                # self.accum=0.
                self.accum=in0[i]
            else:
                self.accum += in0[i]
            # out[i]=self.accum/self.N
            out[i]=self.accum

            # Este es el contado de muestras del vector que hay en mi imaginacion

            if self.count < self.N-1:
                self.count += 1
            else:
                self.count =0
       
        return len(output_items[0])

    def set_ka(self, M):
        self.M=M


