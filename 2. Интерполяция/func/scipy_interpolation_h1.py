import numpy as np
import multiprocessing


import constants
from func.perform_scipy_interpolation import perform_scipy_interpolation
from func.in_matrix_from_string import in_matrix_from_string
from func.from_matrix_in_string import from_matrix_in_string


Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
param = constants.COLUMNS_AFTER_TRANSITION[1]

def scipy_interpolation_h1(T1_inter_n1_string,T2_inter_n1_string,Rring1_inter_n1_string,Rring2_inter_n1_string,
        Rwmg_inter_n1_string,Rbody_inter_n1_string,Rsum_inter_n1_string,
        Mx1_inter_n1_string,Mx2_inter_n1_string,MxWMG_inter_n1_string,MxSum_inter_n1_string,
        df, T1_inter_n1_matrix, list1, Vn_counter_0, h1_counter_0):

    Vn_counter_h1 = (len(np.arange(df[param].min(), df[param].max()+h_inter, h_inter)) * 
                                                len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter)) *
                                                len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) *
                                                len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter)))

    # Записал новые значения в виде матрицы, где каждая строка - это h1
    
    i_counter_1 = len(T1_inter_n1_string)//(len(T1_inter_n1_matrix[:1,:].transpose())*len(list1))
    j_counter_1 = len(T1_inter_n1_matrix[:1,:].transpose())*len(list1)

    (
        T1_inter_h1_matrix,T2_inter_h1_matrix,Rring1_inter_h1_matrix,Rring2_inter_h1_matrix,
        Rwmg_inter_h1_matrix, Rbody_inter_h1_matrix, Rsum_inter_h1_matrix,
        Mx1_inter_h1_matrix, Mx2_inter_h1_matrix, MxWMG_inter_h1_matrix, MxSum_inter_h1_matrix
    ) = in_matrix_from_string(
        T1_inter_n1_string,T2_inter_n1_string,Rring1_inter_n1_string,Rring2_inter_n1_string,
        Rwmg_inter_n1_string,Rbody_inter_n1_string,Rsum_inter_n1_string,
        Mx1_inter_n1_string,Mx2_inter_n1_string,MxWMG_inter_n1_string,MxSum_inter_n1_string,
        i_counter_1, j_counter_1
    )

    R1 = np.array(T1_inter_h1_matrix[:,:1])
    h1 = np.arange(df[param].min(), df[param].max()+2.5, 2.5)
    
    T1_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())
                              ))
    T2_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Rring1_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Rring2_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Rwmg_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Rbody_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Rsum_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))


    Mx1_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    Mx2_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    MxWMG_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))
    MxSum_inter_h1 = np.zeros((len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0, 
                              len(T1_inter_h1_matrix[:1,:].transpose())))  

    list = len(T1_inter_h1_matrix[:1,:].transpose())
    arguments = [
        (df, T1_inter_h1_matrix, T1_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, T2_inter_h1_matrix, T2_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Rring1_inter_h1_matrix, Rring1_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Rring2_inter_h1_matrix, Rring2_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Rwmg_inter_h1_matrix, Rwmg_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Rbody_inter_h1_matrix, Rbody_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Rsum_inter_h1_matrix, Rsum_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Mx1_inter_h1_matrix, Mx1_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, Mx2_inter_h1_matrix, Mx2_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, MxWMG_inter_h1_matrix, MxWMG_inter_h1, h1_counter_0, h_inter, param, h1, list),
        (df, MxSum_inter_h1_matrix, MxSum_inter_h1, h1_counter_0, h_inter, param, h1, list),
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(perform_scipy_interpolation, arguments)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = results

    # Количество диапазонов значений h1 от 20 до 30
    len_counter = (len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*
                                len(T1_inter_h1_matrix[:1,:].transpose())*Vn_counter_0)
    i_counter_2 = len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter))*Vn_counter_0
    j_counter_2 = len(T1_inter_h1_matrix[:1,:].transpose())

    (
        T1_inter_h1_string,T2_inter_h1_string,Rring1_inter_h1_string,Rring2_inter_h1_string,
        Rwmg_inter_h1_string,Rbody_inter_h1_string,Rsum_inter_h1_string,
        Mx1_inter_h1_string,Mx2_inter_h1_string,MxWMG_inter_h1_string,MxSum_inter_h1_string
    ) = from_matrix_in_string(   # Записал новые значения в виде строки для следующего преобразования
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,
        len_counter, i_counter_2, j_counter_2
    )

    return (
        T1_inter_h1_string,T2_inter_h1_string,Rring1_inter_h1_string,Rring2_inter_h1_string,
        Rwmg_inter_h1_string,Rbody_inter_h1_string,Rsum_inter_h1_string,
        Mx1_inter_h1_string,Mx2_inter_h1_string,MxWMG_inter_h1_string,MxSum_inter_h1_string
    )