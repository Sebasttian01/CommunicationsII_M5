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

class decisor_fi(gr.sync_block):
    """
    Entrega un uno si el valor entrante supera el Umbral=0 o un cero si no lo supera. La entrada es tipo float, la salida tipo entero. Este bloque no esta bien probado, puede tener errores. Nota: no importa que valor le des a la variable Umbral, se considerará que Umbral = 0
    """
    def __init__(self, Umbral):
        gr.sync_block.__init__(self,
            name="decisor_fi",
            in_sig=[numpy.float32],
            out_sig=[numpy.int])
#            out_sig=[numpy.bool_])

#        self.Umbral=Umbral


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # <+signal processing here+>
#        a=numpy.zeros(len(in0),dtype=numpy.uint8)
#        a=numpy.zeros(len(in0),dtype=numpy.bool_)
#        for i in range(0,len(in0)):
#            if in0[i]>self.Umbral:
#                a[i]=numpy.int(1)
#            else:
#                a[i]=numpy.int(0)
#        out[:] = a
        out[:]=numpy.ceil(numpy.clip(in0,0,1)).astype('int')
        return len(output_items[0])

