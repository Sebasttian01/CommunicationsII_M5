"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from scipy import integrate

class e_vector_integrate_ff(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Hecho por Homero Ortega. Integrates de input signal en the lenght N of the vector. step is the distance between samples. So that every N samples integration is reset"""

    def __init__(self, step=0.01, N=1024):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_vector_integrate_ff',   # will show up in GRC
            in_sig=[(np.float32, N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N
        self.step = step

    def work(self, input_items, output_items):
        output_items[0][:]=integrate.cumtrapz(input_items[0],dx=self.step,initial=0)
        # print("dx=",self.step)
        return len(output_items[0])

