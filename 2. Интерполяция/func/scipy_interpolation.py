import numpy as np
from scipy import interpolate


import constants


kind = constants.KIND[5]

def scipy_interpolation(df, matrix1, matrix2, step, step_inter, param, x, list1):
    R2 = []
    R3 = []

    i = 0
    j = 0
    k = 0

    for i in range (0, len(list1)):
        R1 = np.array(matrix1[:,i:i+1])
        R4 = []
        for j in range (0, len(R1),step):
            R2 = R1[j:j+step].transpose()
            f = interpolate.interp1d(x, R2, kind = kind)
            R3 = (f(np.arange(df[param].min(), df[param].max()+step_inter, step_inter)))
            R4 = np.array(np.append(R4, R3))
            R5 = np.zeros((len(R4),1)) 
            for k in range(0, len(R4)):
                R5[k] = R4 [k]
        matrix2[:, i:i+1] = R5

    return matrix2