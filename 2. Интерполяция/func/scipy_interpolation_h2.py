import numpy as np
import multiprocessing


from func.perform_scipy_interpolation import perform_scipy_interpolation
from func.in_matrix_from_string import in_matrix_from_string
from func.from_matrix_in_string import from_matrix_in_string
import constants


Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
name = constants.INTERPOLATED_CHARACTERISTICS

"""Интерполяция по h2"""



def scipy_interpolation_h2(
    df,
    h2_counter_0,h1_counter_0,n1_counter_0,
    T1_inter_n2,T2_inter_n2,Rring1_inter_n2,Rring2_inter_n2,
    Rwmg_inter_n2,Rbody_inter_n2,Rsum_inter_n2,
    Mx1_inter_n2,Mx2_inter_n2,MxWMG_inter_n2,MxSum_inter_n2,
    list1,
):
   
    h2 = np.arange(df["h2 [град]"].min(), df["h2 [град]"].max() + h_step, h_step)
    Vn_counter_h2 = (
        h1_counter_0
        * n1_counter_0
        * len(
            np.arange(df["h2 [град]"].min(), df["h2 [град]"].max() + h_inter, h_inter)
        )
        * len(np.arange(0, int(df["n2 [об/мин]"].max()) + n_inter, n_inter))
    )

    # Записал новые значения в виде матрицы, где каждая строка - это h2
    i_counter_1 = len(T1_inter_n2) // len(list1)
    j_counter_1 = len(list1)
    (
        T1_inter_n2_matrix,T2_inter_n2_matrix,Rring1_inter_n2_matrix,Rring2_inter_n2_matrix,
        Rwmg_inter_n2_matrix, Rbody_inter_n2_matrix,Rsum_inter_n2_matrix,
        Mx1_inter_n2_matrix,Mx2_inter_n2_matrix, MxWMG_inter_n2_matrix,MxSum_inter_n2_matrix,
        
    ) = in_matrix_from_string(
        T1_inter_n2,T2_inter_n2,Rring1_inter_n2,Rring2_inter_n2,
        Rwmg_inter_n2,Rbody_inter_n2,Rsum_inter_n2,
        Mx1_inter_n2,Mx2_inter_n2,MxWMG_inter_n2,MxSum_inter_n2,
        i_counter_1,j_counter_1
    )

    R1 = np.array(T1_inter_n2_matrix[:,:1])

    T1_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*  #количество диапазонов от 20 до 30
                               len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)), len(list1)))
    T2_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Rring1_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Rring2_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Rwmg_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Rbody_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Rsum_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
        
    Mx1_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    Mx2_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    MxWMG_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))
    MxSum_inter_h2_matrix = np.zeros((len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)),
                            len(list1)))   

    arguments = [
        (df, T1_inter_n2_matrix, T1_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, T2_inter_n2_matrix, T2_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Rring1_inter_n2_matrix, Rring1_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Rring2_inter_n2_matrix, Rring2_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Rwmg_inter_n2_matrix, Rwmg_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Rbody_inter_n2_matrix, Rbody_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Rsum_inter_n2_matrix, Rsum_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Mx1_inter_n2_matrix, Mx1_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, Mx2_inter_n2_matrix, Mx2_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, MxWMG_inter_n2_matrix, MxWMG_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
        (df, MxSum_inter_n2_matrix, MxSum_inter_h2_matrix, h2_counter_0, h_inter, 'h2 [град]', h2, list1),
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(perform_scipy_interpolation, arguments)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = results

    # Количество диапазонов значений h2 от 20 до 30
    len_counter = len(list1)*len(R1)//h2_counter_0*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))
    i_counter_2 = len(R1)//h2_counter_0 * len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))
    j_counter_2 = len(list1)

    return from_matrix_in_string(   # Записал новые значения в виде строки для следующего преобразования
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, list1, R1, h2_counter_0, h_inter, df, 
        len_counter, i_counter_2, j_counter_2
    )
