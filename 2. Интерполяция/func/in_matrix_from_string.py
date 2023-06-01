import numpy as np


def in_matrix_from_string(
    T1_inter_string,T2_inter_string,Rring1_inter_string, Rring2_inter_string,
    Rwmg_inter_string, Rbody_inter_string,Rsum_inter_string,
    Mx1_inter_string,Mx2_inter_string,MxWMG_inter_string,MxSum_inter_string,
    i_counter, j_counter
):
    k = 0

    T1_inter_matrix = np.zeros((i_counter, j_counter))
    T2_inter_matrix = np.zeros((i_counter, j_counter))
    Rring1_inter_matrix = np.zeros((i_counter, j_counter))
    Rring2_inter_matrix = np.zeros((i_counter, j_counter))
    Rwmg_inter_matrix = np.zeros((i_counter, j_counter))
    Rbody_inter_matrix = np.zeros((i_counter, j_counter))
    Rsum_inter_matrix = np.zeros((i_counter, j_counter))

    Mx1_inter_matrix = np.zeros((i_counter, j_counter))
    Mx2_inter_matrix = np.zeros((i_counter, j_counter))
    MxWMG_inter_matrix = np.zeros((i_counter, j_counter))
    MxSum_inter_matrix = np.zeros((i_counter, j_counter))

    for i in range(0, i_counter):
        for j in range(0, j_counter):
            T1_inter_matrix[i, j] = T1_inter_string[k]
            T2_inter_matrix[i, j] = T2_inter_string[k]

            Rring1_inter_matrix[i, j] = Rring1_inter_string[k]
            Rring2_inter_matrix[i, j] = Rring2_inter_string[k]

            Rwmg_inter_matrix[i, j] = Rwmg_inter_string[k]
            Rbody_inter_matrix[i, j] = Rbody_inter_string[k]
            Rsum_inter_matrix[i, j] = Rsum_inter_string[k]

            Mx1_inter_matrix[i, j] = Mx1_inter_string[k]
            Mx2_inter_matrix[i, j] = Mx2_inter_string[k]
            MxWMG_inter_matrix[i, j] = MxWMG_inter_string[k]
            MxSum_inter_matrix[i, j] = MxSum_inter_string[k]

            k += 1

    return (
        T1_inter_matrix,
        T2_inter_matrix,
        Rring1_inter_matrix,
        Rring2_inter_matrix,
        Rwmg_inter_matrix,
        Rbody_inter_matrix,
        Rsum_inter_matrix,
        Mx1_inter_matrix,
        Mx2_inter_matrix,
        MxWMG_inter_matrix,
        MxSum_inter_matrix
    )