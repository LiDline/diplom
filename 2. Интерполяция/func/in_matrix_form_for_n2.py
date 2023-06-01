import numpy as np


def in_matrix_form_for_n2(
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
    list1,
):
    k = 0

    T1_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    T2_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Rring1_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Rring2_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Rwmg_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Rbody_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Rsum_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))

    Mx1_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    Mx2_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    MxWMG_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))
    MxSum_inter_n2_matrix = np.zeros((len(T1_inter_n2) // len(list1), len(list1)))

    for i in range(0, len(T1_inter_n2) // len(list1)):
        for j in range(0, len(list1)):
            T1_inter_n2_matrix[i, j] = T1_inter_n2[k]
            T2_inter_n2_matrix[i, j] = T2_inter_n2[k]

            Rring1_inter_n2_matrix[i, j] = Rring1_inter_n2[k]
            Rring2_inter_n2_matrix[i, j] = Rring2_inter_n2[k]

            Rwmg_inter_n2_matrix[i, j] = Rwmg_inter_n2[k]
            Rbody_inter_n2_matrix[i, j] = Rbody_inter_n2[k]
            Rsum_inter_n2_matrix[i, j] = Rsum_inter_n2[k]

            Mx1_inter_n2_matrix[i, j] = Mx1_inter_n2[k]
            Mx2_inter_n2_matrix[i, j] = Mx2_inter_n2[k]
            MxWMG_inter_n2_matrix[i, j] = MxWMG_inter_n2[k]
            MxSum_inter_n2_matrix[i, j] = MxSum_inter_n2[k]

            k += 1

    return (
        T1_inter_n2_matrix,
        T2_inter_n2_matrix,
        Rring1_inter_n2_matrix,
        Rring2_inter_n2_matrix,
        Rwmg_inter_n2_matrix,
        Rbody_inter_n2_matrix,
        Rsum_inter_n2_matrix,
        Mx1_inter_n2_matrix,
        Mx2_inter_n2_matrix,
        MxWMG_inter_n2_matrix,
        MxSum_inter_n2_matrix
    )