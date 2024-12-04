"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, ):  # only default arguments here
        """hecho por estudiantes e3t 2021"""
        gr.sync_block.__init__(
            self,
            name='e_EC_fc',   # will show up in GRC
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
       

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        Sec=output_items[0]
        Sec[:]=A*np.exp(1j*Q)
        return len(Sec)
