"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from scipy import integrate
import scipy.stats

class e_cdf_ff(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Hecho por Homero Ortega. Xmin is the minimum value that the input signal can take, Xmax is the maximum value that the input signal can take; N es the number of steps the signal will be analized in amplitud and is the number of samples in the input vector"""

    def __init__(self, Xmin=-1., Xmax=1., N=1024):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_cdf_ff',   # will show up in GRC
            in_sig=[(np.float32, N)],
            out_sig=[(np.float32,N)]
        )
        self.Xmin = Xmin
        self.Xmax = Xmax
        self.N = N
        self.X=np.linspace(self.Xmin,self.Xmax,self.N) # Se le pueden dar menos valores, pero el bloque seria de tipo decimador
        self.counts=np.array([0.]*self.N)
        self.N_hist=0. #numero de histogramas procesados
        
    def work(self, input_items, output_items):
        
        x=input_items[0] # las muestras entrantes a analizar
        h=np.histogram(x,bins=self.N, range=(self.Xmin, self.Xmax)) # h[0] es el histograma propiamente, h[1] los bins
        hist_dist=scipy.stats.rv_histogram(h) # objeto que identifica muchos parametros de un histograma incluyento cdf

        cdf=hist_dist.cdf(self.X) # cdf instantanea

        self.N_hist += 1     # se eleva el contador de histrogramas calculados
        self.counts += cdf  # cdf acumulada
        output_items[0][:]=self.counts/(self.N_hist)   # cdf promediada

        return len(output_items[0])
