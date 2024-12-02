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

class zero_order_hold2_cc(gr.interp_block):
    """
    Es un retenedor de orden cero. De modo que cada muestra que recibe la repite k veces, donde k es el tiempo discreto de retencion. Hecho por Homero Ortega, Universidad Industrial de Santander, Colombia
    
    CORREGIR: Parece que las operaciones pueden ser mejor vectorizadas
    """
    def __init__(self, k):
        self.k=k
        gr.interp_block.__init__(self,
            name="zero_order_hold2_cc",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64], interp=k)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>
        j=0
        for i in range (len(in0)):
            for x in range(self.k):
                out[j] =  in0[i]
                j += 1 
        return len(output_items[0])

# Este es el caller que permite cambiar en caliente el coeficiente el retardo
# el xml debe ser informado que esta es la funcion a llamar para ese tipo de cambios
    def set_retardo(self, k):
        self.k=k

