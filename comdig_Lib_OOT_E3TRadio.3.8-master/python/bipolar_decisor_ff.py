"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class bipolar_decisor_ff(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Hecho por Homero Ortega Boada, UIS 2020. Entrega como salida 1 si la entrada supera el umbral cero, pero -1 si no lo supera. Tanto la entrada como la salida es un valor de tipo float. Se ha logrado vectorizar la operacion asi: al vector de entrada in0 se le aplica un limitador entre 0 y 1. Osea que los valores mayores a 1 se convierten a 1, los menores de cero a cero, con lo cual tendremos valores entre cero y 1. Luego se aplica un redondeo hacia arriba, con lo cual solo tendremos 0s o 1s. Luego se multiplica todo por2 y se resta 1, con lo cual solo tendremos -1s y 1s"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='bipolar_decisor_ff',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32])
        #self.Umbral=Umbral

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # Signal processing
        out[:] = np.ceil(np.clip(in0,0,1))*2-1
        #out[:] = [float(v>self.Umbral) for v in in0]
        return len(output_items[0])
