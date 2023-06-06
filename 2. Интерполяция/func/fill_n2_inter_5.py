import numpy as np

def fill_n2_inter_5(chunk):
    start, end, list = chunk
    n2_inter_5 = []
    for i in range(start, end):
        n2_inter_5 = np.append(n2_inter_5, list)
    return n2_inter_5