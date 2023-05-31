import numpy as np


def math_interpolation_n2():

    i = 0

    for j in range (0, (len(R_sum)//n2_counter_0)):
        R1 = np.array(df.loc[i:i+n2_counter_0-1, name[l]].values)
        f = interpolate.interp1d(n2, R1, kind = 'cubic')
        list1 = f(np.arange(int(df['n2 [об/мин]'].min()),int(df['n2 [об/мин]'].max())+n_inter,n_inter))
        parametr = np.append(parametr, list1)
        i += n2_counter_0
    i = 0    







(
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
    ) = math_interpolation_n2(
        df, n2_counter_0, h1_counter_0, n1_counter_0, h2_counter_0
    )