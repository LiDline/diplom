import numpy as np
import multiprocessing


import constants
from func.in_matrix_from_string import in_matrix_from_string
from func.perform_scipy_interpolation import perform_scipy_interpolation
from func.from_matrix_in_string import from_matrix_in_string


h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
param = constants.COLUMNS_AFTER_TRANSITION[2]


def scipy_interpolation_n1(
        df,T1_inter_h2_string, T2_inter_h2_string,Rring1_inter_h2_string,Rring2_inter_h2_string,
        Rwmg_inter_h2_string,Rbody_inter_h2_string,Rsum_inter_h2_string,
        Mx1_inter_h2_string,Mx2_inter_h2_string,MxWMG_inter_h2_string,
        MxSum_inter_h2_string,h1_counter_0,n1_counter_0
        ):

    Vn_counter_n1 = (h1_counter_0 * len(np.arange(0,int(df[param].max())+n_inter,n_inter)) *
                                                len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) *
                                                len(np.arange(0,int(df[param].max())+n_inter,n_inter)))
    

    # Записал новые значения в виде матрицы, где каждая строка - это n1
    i_counter_1 = len(T1_inter_h2_string)//(len(np.arange(0,int(df[param].max())+n_inter,n_inter))*
                                  len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)))
    j_counter_1 = (len(np.arange(0,int(df[param].max())+n_inter,n_inter))*
                                  len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)))
    (
      T1_inter_n1_matrix,T2_inter_n1_matrix,Rring1_inter_n1_matrix,Rring2_inter_n1_matrix,
      Rwmg_inter_n1_matrix, Rbody_inter_n1_matrix, Rsum_inter_n1_matrix,
      Mx1_inter_n1_matrix, Mx2_inter_n1_matrix, MxWMG_inter_n1_matrix, MxSum_inter_n1_matrix
    ) = in_matrix_from_string(T1_inter_h2_string, T2_inter_h2_string,Rring1_inter_h2_string,Rring2_inter_h2_string,
        Rwmg_inter_h2_string,Rbody_inter_h2_string,Rsum_inter_h2_string,
        Mx1_inter_h2_string,Mx2_inter_h2_string,MxWMG_inter_h2_string,
        MxSum_inter_h2_string,
        i_counter_1,j_counter_1
        )
    
    R1 = np.array(T1_inter_n1_matrix[:,:1])
    n1 = np.arange(df[param].min(), df[param].max()+n_step, n_step)

    T1_inter_n1 = np.zeros((len(R1)//n1_counter_0*  #количество диапазонов 750 до 1500 для n1
                               len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    T2_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))

    Rring1_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    Rring2_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    Rwmg_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    Rbody_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    Rsum_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))

    Mx1_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    Mx2_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    MxWMG_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))
    MxSum_inter_n1 = np.zeros((len(R1)//n1_counter_0*len(np.arange(df[param].min(), df[param].max()+n_inter, n_inter)),
                               len(T1_inter_n1_matrix[:1,:].transpose())))

    list = len(T1_inter_n1_matrix[:1,:].transpose())    # Высчитывалось вручную
    arguments = [
        (df, T1_inter_n1_matrix, T1_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, T2_inter_n1_matrix, T2_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Rring1_inter_n1_matrix, Rring1_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Rring2_inter_n1_matrix, Rring2_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Rwmg_inter_n1_matrix, Rwmg_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Rbody_inter_n1_matrix, Rbody_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Rsum_inter_n1_matrix, Rsum_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Mx1_inter_n1_matrix, Mx1_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, Mx2_inter_n1_matrix, Mx2_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, MxWMG_inter_n1_matrix, MxWMG_inter_n1, n1_counter_0, n_inter, param, n1, list),
        (df, MxSum_inter_n1_matrix, MxSum_inter_n1, n1_counter_0, n_inter, param, n1, list),
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(perform_scipy_interpolation, arguments)
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11 = results
    
    # Количество диапазонов значений n1 0 до 1000
    len_counter = (len(R1)//n1_counter_0*
                           len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter))*
                            len(T1_inter_n1_matrix[:1,:].transpose()))
    i_counter_2 = len(R1)//n1_counter_0*len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter))
    j_counter_2 = len(T1_inter_n1_matrix[:1,:].transpose())

    return from_matrix_in_string(   # Записал новые значения в виде строки для следующего преобразования
        b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11,
        len_counter, i_counter_2, j_counter_2
    ) 