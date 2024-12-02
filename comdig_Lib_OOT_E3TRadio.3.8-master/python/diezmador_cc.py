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

class diezmador_cc(gr.decim_block):
    """
    paso: Es el numero de muestras en que saltara el diezmador. Esto significa que se borraran paso-1 muestras.
    inicio: punto de inicio es 0.
    nota: Tenga en cuenta que la frecuencia de muestreo baja (samp_rate_new = samp_rate_old/paso).

EJEMPLO: Entrada = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
	 paso = 3
	 Salida = Entrada[0::paso] = [ 1, 4, 7, 10] 
    """

    def __init__(self,  paso):
        self.paso = paso 

        gr.decim_block.__init__(self,
        name="diezmador_cc",
        in_sig=[numpy.complex64],
        out_sig=[numpy.complex64], decim = paso)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        out[:] = in0[::self.paso]

        return len(output_items[0])






















