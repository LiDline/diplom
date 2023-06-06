import numpy as np


import constants


h_inter = constants.H_STEP_INTER

def fill_h2_inter_5(chunk):
    start, end, list_n2, df = chunk
    h2_inter_5 = []
    k = df['h2 [град]'].min()

    for i in range(start, end):
        if k <= df['h2 [град]'].max():
            list20 = [k] * len(list_n2)
            h2_inter_5 = np.append(h2_inter_5, list20)
            k += h_inter
        else:
            k = df['h2 [град]'].min()
            list20 = [k] * len(list_n2)
            h2_inter_5 = np.append(h2_inter_5, list20)
            k += h_inter

    return h2_inter_5