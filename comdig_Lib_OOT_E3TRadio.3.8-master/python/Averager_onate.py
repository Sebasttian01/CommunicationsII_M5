#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
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
from numpy import *
import numpy as np
from gnuradio import gr


class Averager_onate(gr.sync_block):
    """
    Va promediando un vector de N muestras. El resultado es un nuevo vector que se va actualizando a medida que se renueva el vector en la entrada de modo que el vector de salida es el promedio de todos los vectores que van pasando por la entrada. N es la longitud del vector de entrada y por consiguiente tambien el de la salida.

PARA CORREGIR: El codigo de este bloque no esta optimizado a operaciones vectoriales.Quiza un ejemplo a seguir sea el bloque averager, el power_meter y el vector_average_hob.
    """
    def __init__(self, N):
        self.N = N
        gr.sync_block.__init__(self,
        name="Averager_onate",
        in_sig=[numpy.float32],
        out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+
        n=0;
        in0=array(in0)
        #print (in0)
        a=len(in0);
        c=np.zeros((1,a));
        #print(N)
        while n != self.N:
            c=c+in0
            n=n+1
        #print(n)
        final=c/n
        out[:]=final

            
        return len(output_items[0])

