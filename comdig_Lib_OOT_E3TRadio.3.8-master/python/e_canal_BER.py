#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
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
import numpy as np
import random
import math
from gnuradio import gr

class e_canal_BER(gr.sync_block):
    """
Es un canal AWGN (Additive White Gaussian Noise, en banda base), Recibe la envolvente compleja de una senal con modulacion digital. El bloque tiene dos salidas: out0, out1. En out0 entrega la misma senal recibida pero con ruido blanco gausiano aditivo con diferentes valores de potencia que corresponden a diferentes valores Es/No; en out1 entrega un valor de Es/No aplicado a cada muestra de out0. Este bloque se diferencia de otros bloques tradicionales de canal AWGN en lo siguiente: Tiene internamente una funcion que mide la potencia promedio de la senal entrante Ps, de modo que puede calcular Es=Ps/Rs; Al ir variando la potencia del ruido Pn se logra variar la relacion Es/No para que tome N posibles valores entre EsN0min y EsN0max. Con esto ha completado el primer ensayo para que otro sea el bloque que calcule la Curva de BER. Pero alli no para, sino que sigue realizando tantos ensayos como lo permita el tiempo de simulacion, para que el bloque que calcula la Curva de BER la pueda ir perfeccionando cada vez mas.

Datos de configuracion del bloque:
N: Es el numero de puntos discretos que va a tener la curva de BER. Tambien corresponde al numero de valores que tomará la relacion Es/No
EsN0min: El minimo valor a tener en cuenta para Es/No
EsN0max: El maximo valor a tener en cuenta para Es/No
Rs: es la rata de simbolos.
B: Es una caracteristica de la senal entrante, corresponde a la frecuencia de muestreo de la señal entrante y puede ser mayor o igual a Rs. 
Es: es la energia de un simbolo

Senales de entrada:
In0: Envolvente compleja de señal con modulacion digital.

Senales de salida: 
out0: es la salida del canal, es decir, la misma señal entrante pero a la cual se le ha sumado un ruido para satisfacer una determinado valor para la relación Es/No
out1: Es el valor Es/No aplicado a la salida actual.

Algunas variables internas son:
No: es la Densidad espectral del potencia del ruido blanco.
SNR-Db: es la relacion senal a ruido en dB

NOTA IMPORTANTE: 
* Nos preguntamos si este bloque no deberia llamarse e_canal_BER, pues no manera bits, ni relacion alguna con ellos, solo simbolos. El nombre mas apropiado seria e_canal_EsN0
* Este bloque no conoce el numero de bits por simbolo, por lo tanto no puede determinar la relacion Eb/No y lo que calcula es la BER con respecto a Es/No.
* La Envolvente compleja puede tener varias muestras por simbolo (Sps), por ejemplo cuando ha pasado por un bloque de Wave Forming, por ello SampRate puede ser mayor o igual a Rs. SampRate=Rs*Sps. El problema es que en este caso, la salida out0 tendra tambien Sps valores por simbolo, lo cual debe ser tenido en cuenta por los bloques que usen esta senal.
* Es es calculado como: Es = Ps x Ts, donde Ps es la potencia promedio de la senal entrante (se mide internamente) y Ts es la duracion de cada simbolo o Ts = 1 / Rs. Entendemos que eso implica imaginar que los simbolos tienen forma rectangular, lo cual puede ser valido cuando la senal entrante trae modulacion digital basada en puntos de constelacion como es el caso de: BPSK, QPSK, MPSK, MQAM. En otras palabras, es una idealizacion pensada en una herramienta de analisis de Curvas de BER para comparar diferentes tipos de modulacion en condiciones similares.

PARA CORREGIR: este bloque no debria llamarse e_canal_BER sino canal_BER_cc
"""
    def __init__(self, N=8, EsN0min=0, EsN0max=16,B=100,Rs=1):  # only default arguments here
        gr.sync_block.__init__(
        self,
        name='e_canal_BER',
        in_sig=[np.complex64],
        out_sig=[np.complex64, np.int32])
        self.N = N
        self.B=B
        self.Rs=Rs

        self.EsN0dB=np.linspace(EsN0min,EsN0max,N)
        self.k=0  # recuerda cual es el valor de SNR actual
     
    def work(self, input_items, output_items):
        L=len(input_items[0])
        Rs=self.Rs
        B1=self.B
        # calculo de la varianza (potencia promedio normalizada) de la senal entrante
        Pin=np.mean(np.absolute(input_items[0])**2)
        ###############################################################  
        ##  Esta es donde esta el mehoyo y se puede optimizar mejor  ##
        ##  Algo que se podria hacer es que le de mas atencion a los 
        ##  valores altos de Es/No que es donde es mas dificil de ob-##
        ##  tener la BER. Al parecer la forma facil de hacerlo es    ##
        ##  hacer que el vector EsN0dB vaya cambiando, ya que por    ##
        ##  es estatico y es el que define que valores de EsN0dB usar##
        ## Otro aspecto que se puede mejorar es que: los bloques que ##
        ## se benefician de este bloque, tienen que convertir lo que ##
        ## le entregamos a un vecotr de tamano N. Para esa gracia,   ##
        ## lo conveniente sería exigir que las señales que entran y  ##
        ## salen de este bloque sean de tipo vectorial, con tamano N. ##
        ## Supongo que ya tenemos un valor fijo para L=N nos liberaremos
        ## de los for e if de abajo                                  ##
        ###############################################################
        for i in range(0,L): 
            output_items[0][i] = input_items[0][i]+noise_c(self.EsN0dB[self.k], Pin,Rs,B1)
            output_items[1][i] = self.k # Aqui hay error, debe devolver no k sino el EsNodB aplicado
            if self.k < self.N-1:
                self.k += 1
            else:
                self.k=0
        return len(output_items[0])

#############################################################################
## calculo de una muestra de ruido
## Rb: Rata de bit
## B: Es el ancho de banda pasobanda que va a ocupar el ruido blanco, que no
##    no es otra cosa que 2 veces el ancho de banda que tiene la envolvente
##    compleja del ruido blanco que estamos generando. Estamos considerando que
##    B es igual a la frecuencia de muestreo de la senal
## N: es el numero de elementos en el vector
## P_s: es la varianza (potencia promedio) de la senal entrante. 
## SNR_dB: es la relacion senal a ruido en dB del ruido respecto a P_signal
#############################################################################

def noise_c(EsN0_dB,P_s,Rs,B):
    EsN0=pow(10.,EsN0_dB/10.) 
    SNR=EsN0*Rs/B
    P_n = P_s/SNR  # la potencia del ruido
    Vrms = math.sqrt(P_n) 
    # random.normal() pide la desviacion standard pero es el mismo Valor RMS
    # Vrms es el Valor RMS de la Envolvente compleja del ruido, pero la vamos
    # a generar como un ruido real mas un ruido imaginario. Pero esas dos
    # senales tienen un valor RMS un tanto diferente: Vrms_q=Vrms/math.sqrt(2.)
    Vrms_q= Vrms/math.sqrt(2.)
    n=np.random.normal(0.,Vrms_q)+np.random.normal(0.,Vrms_q)*1.j

    return n
