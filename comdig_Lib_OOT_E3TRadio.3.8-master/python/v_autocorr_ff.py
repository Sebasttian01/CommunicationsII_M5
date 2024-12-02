#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 open source.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr

class v_autocorr_ff(gr.sync_block):
    """
    Hecho por Homero Ortega. Grupo RadioGis. Universidad Industrial de Santander. Calcula la Funcion de Autocorrelacion de una senal Rx(Tau) para una senal x[n]. Parametros: N - es al mismo tiempo el numero de muestras del vector entrante y el saliente, pero tambien es el rango de valores para Tau, pero dado en numero de muestras, de manera que Tau estara entre -N/2 y (N/2)-1. La Funcion de autocorrelacion se va aplicando a cada ventana de N muestras, pero si seguidamente se usa un bloque que permita promediar todas las fotos de las ventanas de autocorrelacion que resultan, por ejemplo el bloque vector_average_hob, se podra obtener una Funcion de autocorrelacion que se va perfeccionando en el tiempo a medida que se tienen en cuenta mas y mas ventanas.   
    """
    def __init__(self, N=8):
        gr.sync_block.__init__(self,
            name="v_autocorr_ff",
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
            )
        self.N = N

    def work(self, input_items, output_items):
        x=input_items[0]
        y=output_items[0]
        # El tamano de la matriz in0 es L[0]xL[1]=L[0]xN
        L=x.shape
        # el siguiente for es porque x es una matrix 
        # y el comando correlate solo funciona en vectores
        # por lo tanto lo aplicamos a cada fila de la matrix
        for i in list(range(L[0])):
            y[i][:] = np.correlate(x[i],x[i], mode='same')/self.N
        return len(output_items[0])
