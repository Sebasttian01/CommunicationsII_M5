import numpy as np
from gnuradio import gr
import matplotlib.pyplot as plt

class vec_diagrama_ojo2_f(gr.sync_block):
    """
    Diagrama de ojo. Hecho por Homero Ortega Boada. Universida Industrial de Santander.
N: es el numero de muestras que ocupara el ojo, se recomienda que N=Sps*2, donde Sps es el numero de muestras por simbolo.
samp_rate: es la frecuencia de muestreo de la senal.
    """
    def __init__(self, N=64, samp_rate=32000, Ncurvas=100):
        gr.sync_block.__init__(self,
            name="e_vec_diagrama_ojo2_f",
            in_sig=[(np.float32, N)],
            out_sig=None)
        #########################################
        ##        Parametros                   ##
        #########################################
        self.Sps = int(N/2)
        self.Tsamp=1./samp_rate
        Tb=self.Sps*self.Tsamp
        self.t = np.linspace(-Tb,Tb, 2*self.Sps)
        self.Ncurvas=Ncurvas
        self.contador=0

    def work(self, input_items, output_items):
        in0 = input_items[0] # in0 es un 2D array (como una matrix)
        s=in0[0]    # Esto traduce el 2D array a 1D array (a un vector)
        #plt.plot(self.t,s)             
        #plt.pause(self.Tsamp)
        if self.contador < self.Ncurvas:
            plt.plot(self.t,s)
            plt.pause(self.Tsamp)
            self.contador += 1
        else:
            self.contador=0
            plt.clf()
        return len(input_items[0])
