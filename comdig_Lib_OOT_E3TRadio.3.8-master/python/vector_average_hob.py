 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
from gnuradio import gr

class vector_average_hob(gr.sync_block):
    """
    El bloque vector_averager_hob recibe una senal con tramas de tamano fijo de N valores y va entregando una trama del mismo tamano que corresponde a la trama media de todas las tramas que va recibiendo. 
Los parametros usados son:
N:        Es el tamano del vector o trama
Nensayos: Es el umbral que limita el numero maximo de promedios correctamente realizados. Cuando a la funcion se le ha invocado un numero de veces mayor a Nensayos, el promedio continua realizandose, pero considerando que el numero de promedios realizado hasta el momento ya no se incrementa, sino que es igual a Nensayos. 
    """

    def __init__(self, N, Nensayos):
        gr.sync_block.__init__(self, name="vector_average_hob", in_sig=[(numpy.float32, N)], out_sig=[(numpy.float32, N)])

        # Nuestras variables especificas
        self.N=N
        self.Nensayos=numpy.uint64=Nensayos
        self.med=numpy.empty(N,dtype=numpy.float64)
        self.count=numpy.uint64=0

    def work(self, input_items, output_items):

        # Traducción de matrices 3D a 2D 
        in0 = input_items[0]
        out0=output_items[0]
        
        # El tamano de la matriz in0 es L[0]xL[1]=L[0]xN
        L=in0.shape

        # conteo de funciones muestras (filas de matriz) procesadas
        if self.count < self.Nensayos:
            self.count += L[0] 

        # La media de las funciones muestras (filas de matriz) que tiene in0
        mean=in0.mean(0) 	

        # ajuste de la media ya calculada, con la media de in0
        self.med = (self.med*(self.count-L[0])+mean*L[0])/self.count

        # Entrega de resultado
        out0[:]=self.med
        return len(out0)
