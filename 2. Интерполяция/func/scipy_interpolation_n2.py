import numpy as np
from scipy import interpolate
import pandas as pd


import constants


kind = constants.KIND[5]
Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
name = constants.INTERPOLATED_CHARACTERISTICS

"""Интерполяция по n2"""

def scipy_interpolation_n2(df, Vn_counter_0, h1_counter_0, n1_counter_0, h2_counter_0, n2_counter_0):

    n2 = np.array(df.loc[:n2_counter_0-1, 'n2 [об/мин]'].values, np.float64)
    R_sum = np.array(df.loc[:, 'R сум [Н]'].values)
    df_Vx = pd.DataFrame()
    df_Vx = df[(df['Vн [км/ч]'] == df['Vн [км/ч]'].min())]
    len_Vx1 = len(df_Vx['Vн [км/ч]'])

    parametr = []
    list1 = []

    Vn_counter_n2 = h1_counter_0*n1_counter_0*h2_counter_0*len(np.arange(int(df['n2 [об/мин]'].min()),int(df['n2 [об/мин]'].max())+n_inter,n_inter))
    len_inter1 = Vn_counter_n2 * (len(R_sum)//len_Vx1)

    for l in range (0, len(name)):
        for i in range (0, len(R_sum), n2_counter_0):
            R1 = np.array(df.loc[i:i+n2_counter_0-1, name[l]].values)
            f = interpolate.interp1d(n2, R1, kind = kind)
            list1 = f(np.arange(int(df['n2 [об/мин]'].min()),int(df['n2 [об/мин]'].max())+n_inter,n_inter))
            parametr = np.append(parametr, list1)    
        l += 1
        
    T1_inter_n2 = parametr[name.index('Тв1 [Н]')*len_inter1 : name.index('Тв1 [Н]')*len_inter1+len_inter1]
    T2_inter_n2 = parametr[name.index('Тв2 [Н]')*len_inter1 : name.index('Тв2 [Н]')*len_inter1+len_inter1]

    Rring1_inter_n2 = parametr[name.index('Rк1 [Н]')*len_inter1 : name.index('Rк1 [Н]')*len_inter1+len_inter1]
    Rring2_inter_n2 = parametr[name.index('Rк2 [Н]')*len_inter1 : name.index('Rк2 [Н]')*len_inter1+len_inter1]

    Rwmg_inter_n2 = parametr[name.index('R ВМГ [Н]')*len_inter1 : name.index('R ВМГ [Н]')*len_inter1+len_inter1]

    Rbody_inter_n2 = parametr[name.index('R тела [Н]')*len_inter1 : name.index('R тела [Н]')*len_inter1+len_inter1]

    Rsum_inter_n2 = parametr[name.index('R сум [Н]')*len_inter1 : name.index('R сум [Н]')*len_inter1+len_inter1]

    Mx1_inter_n2 = parametr[name.index('Mвx1 [Н*м]')*len_inter1 : name.index('Mвx1 [Н*м]')*len_inter1+len_inter1]
    Mx2_inter_n2 = parametr[name.index('Mвx2 [Н*м]')*len_inter1 : name.index('Mвx2 [Н*м]')*len_inter1+len_inter1]

    MxWMG_inter_n2 = parametr[name.index('Mx ВМГ [Н*м]')*len_inter1 : name.index('Mx ВМГ [Н*м]')*len_inter1+len_inter1]

    MxSum_inter_n2 = parametr[name.index('Mx сум [Н*м]')*len_inter1 : name.index('Mx сум [Н*м]')*len_inter1+len_inter1]

    return (
        T1_inter_n2,
        T2_inter_n2,
        Rring1_inter_n2,
        Rring2_inter_n2,
        Rwmg_inter_n2,
        Rbody_inter_n2,
        Rsum_inter_n2,
        Mx1_inter_n2,
        Mx2_inter_n2,
        MxWMG_inter_n2,
        MxSum_inter_n2,
        list1
    ) 
