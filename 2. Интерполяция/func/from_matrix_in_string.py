import numpy as np



# Записал новые значения в виде строки для следующего преобразования
def from_matrix_in_string(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, list1, R1, h2_counter_0, h_inter, df, 
                          len_counter, i_counter, j_counter):

    k = 0

    T1_inter_string = np.zeros((len_counter))
    T2_inter_string = np.zeros((len_counter))
    Rring1_inter_string = np.zeros((len_counter))
    Rring2_inter_string = np.zeros((len_counter))
    Rwmg_inter_string = np.zeros((len_counter))
    Rbody_inter_string = np.zeros((len_counter))
    Rsum_inter_string = np.zeros((len_counter))

    Mx1_inter_string = np.zeros((len_counter))
    Mx2_inter_string = np.zeros((len_counter))
    MxWMG_inter_string = np.zeros((len_counter))
    MxSum_inter_string = np.zeros((len_counter))

    

    for i in range (0, i_counter):
        for j in range (0, j_counter):
            T1_inter_string[k] = a1[i,j]
            T2_inter_string[k] = a2[i,j]
            Rring1_inter_string[k]  = a3[i,j]
            Rring2_inter_string[k]  = a4[i,j]
            Rwmg_inter_string[k] = a5[i,j]
            Rbody_inter_string[k] = a6[i,j]
            Rsum_inter_string[k]= a7[i,j]

            Mx1_inter_string[k]  = a8[i,j]
            Mx2_inter_string[k]  = a9[i,j]
            MxWMG_inter_string[k] = a10[i,j]
            MxSum_inter_string[k] = a11[i,j]

            k += 1


    return (
        T1_inter_string,
        T2_inter_string,
        Rring1_inter_string,
        Rring2_inter_string,
        Rwmg_inter_string,
        Rbody_inter_string,
        Rsum_inter_string,
        Mx1_inter_string,
        Mx2_inter_string,
        MxWMG_inter_string,
        MxSum_inter_string,
    )