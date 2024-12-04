import numpy as np
from gnuradio import gr

class blk(gr.sync_block):  
#    """Multiplica dos senales tipo char"""
    def __init__(self,):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='e_Multiply_bb',   # will show up in GRC
            in_sig=[np.int8, np.int8],
            out_sig=[np.int8]
        )

    def work(self, input_items, output_items):
        output_items[0][:] = input_items[0]*input_items[1]
        return len(output_items[0])
