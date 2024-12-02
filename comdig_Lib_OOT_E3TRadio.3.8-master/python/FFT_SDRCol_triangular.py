#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 RadioGIS-ANE.
#                Proyecto SDR-COL.

import numpy
from gnuradio import gr

class FFT_SDRCol_triangular(gr.sync_block):
    """
    Este bloque funciona de manera similar a la FFT, solo que usa la base de funciones triangulares en vez de las tradicionales. N es el numero de muestras del vector de entrada. Este codigo no esta suficientemente optimizado aun, pero funciona muy bien
    """
    def __init__(self, N):
        self.N = N
        gr.sync_block.__init__(self,
        name="FFT_SDRCol.Triangular",
        in_sig=[(numpy.complex64, self.N)],
        out_sig=[(numpy.complex64, self.N)])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        N = self.N

        
#           """Pesos Triangulares Complejos"""
        def W(nk, N):
    #       
           nk %= N
           W = 2 * abs( 2.0 * nk / N - 1) - 1 + 0j
           W[nk < N/2] += (1 - abs(4.0 * nk / N - 1))[nk < N/2] * 1j
           W[nk >= N/2] += (abs(4.0 * nk / N - 3) - 1)[nk >= N/2] * 1j
           
           return W
        
        N_min = min(N, 2)
    
        n = numpy.arange(N_min)
        k = n[:, None]
        M = W(n*k, N_min)

        for i, x in enumerate(in0):

            X = numpy.dot(M, x.reshape((N_min, -1)))

            while X.shape[0] < N:
                X_even = X[:, :X.shape[1] / 2]
                X_odd = X[:, X.shape[1] / 2:]
                factor = W(numpy.arange(X.shape[0]), X.shape[0]*2)[:, None]
                X = numpy.vstack([X_even + factor * X_odd, X_even - factor * X_odd])
            X=X.ravel()
            Y = numpy.hstack([X[N/2:],X[:N/2]])
            out[i][:] = Y
        return len(output_items[0])
