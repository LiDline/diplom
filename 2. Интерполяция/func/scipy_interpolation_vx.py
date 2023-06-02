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
param = constants.COLUMNS_AFTER_TRANSITION[0]


def scipy_interpolation_vx(
        T1_inter_h1_string,T2_inter_h1_string,Rring1_inter_h1_string,Rring2_inter_h1_string,
        Rwmg_inter_h1_string,Rbody_inter_h1_string,Rsum_inter_h1_string,
        Mx1_inter_h1_string,Mx2_inter_h1_string,MxWMG_inter_h1_string,MxSum_inter_h1_string,
        df, Vn_counter_0
):

    Vn_counter_h1 = (len(np.arange(int(df['n2 [об/мин]'].min()),int(df['n2 [об/мин]'].max())+n_inter,n_inter)) * len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) * 
                    len(np.arange(int(df['n1 [об/мин]'].min()),int(df['n1 [об/мин]'].max())+n_inter,n_inter)) * len(np.arange(df['h1 [град]'].min(), df['h1 [град]'].max()+h_inter, h_inter)))
    

    i_counter_1 = len(T1_inter_h1_string)//Vn_counter_h1
    j_counter_1 = Vn_counter_h1

    (
        T1_inter_Vx_matrix,T2_inter_Vx_matrix,Rring1_inter_Vx_matrix,Rring2_inter_Vx_matrix,
        Rwmg_inter_Vx_matrix, Rbody_inter_Vx_matrix, Rsum_inter_Vx_matrix,
        Mx1_inter_Vx_matrix, Mx2_inter_Vx_matrix, MxWMG_inter_Vx_matrix, MxSum_inter_Vx_matrix
    ) = in_matrix_from_string(
        T1_inter_h1_string,T2_inter_h1_string,Rring1_inter_h1_string,Rring2_inter_h1_string,
        Rwmg_inter_h1_string,Rbody_inter_h1_string,Rsum_inter_h1_string,
        Mx1_inter_h1_string,Mx2_inter_h1_string,MxWMG_inter_h1_string,MxSum_inter_h1_string,
        i_counter_1, j_counter_1
    )


    Vx = np.arange(df[param].min(), df[param].max() + Vn_step, Vn_step)

    T1_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())
                              ))
    T2_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Rring1_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Rring2_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Rwmg_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Rbody_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Rsum_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))

    Mx1_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    Mx2_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    MxWMG_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))
    MxSum_inter_Vx = np.zeros((len(np.arange(df[param].min(), df[param].max()+Vx_inter, Vx_inter)), 
                              len(T1_inter_Vx_matrix[:1,:].transpose())))

    list = len(T1_inter_Vx_matrix[:1,:].transpose())
    arguments = [
        (df, T1_inter_Vx_matrix, T1_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, T2_inter_Vx_matrix, T2_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Rring1_inter_Vx_matrix, Rring1_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Rring2_inter_Vx_matrix, Rring2_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Rwmg_inter_Vx_matrix, Rwmg_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Rbody_inter_Vx_matrix, Rbody_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Rsum_inter_Vx_matrix, Rsum_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Mx1_inter_Vx_matrix, Mx1_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, Mx2_inter_Vx_matrix, Mx2_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, MxWMG_inter_Vx_matrix, MxWMG_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
        (df, MxSum_inter_Vx_matrix, MxSum_inter_Vx, Vn_counter_0, Vx_inter, param, Vx, list),
    ]

    with multiprocessing.Pool() as pool:
        results = pool.map(perform_scipy_interpolation, arguments)
    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11 = results

    len_counter = (len(np.arange(df['Vн [км/ч]'].min(), df['Vн [км/ч]'].max()+Vx_inter, Vx_inter))*
                              len(T1_inter_Vx_matrix[:1,:].transpose()))
    i_counter_2 = len(np.arange(df['Vн [км/ч]'].min(), df['Vн [км/ч]'].max()+Vx_inter, Vx_inter))
    j_counter_2 = len(T1_inter_Vx_matrix[:1,:].transpose())

    (
        T1_inter_Vx_string,T2_inter_Vx_string,Rring1_inter_Vx_string,Rring2_inter_Vx_string,
        Rwmg_inter_Vx_string,Rbody_inter_Vx_string,Rsum_inter_Vx_string,
        Mx1_inter_Vx_string,Mx2_inter_Vx_string,MxWMG_inter_Vx_string,MxSum_inter_Vx_string
    ) = from_matrix_in_string(
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,
        len_counter, i_counter_2, j_counter_2
    )

    print('Интерполяция по Vx завершена.')

    return (
        T1_inter_Vx_string,T2_inter_Vx_string,Rring1_inter_Vx_string,Rring2_inter_Vx_string,
        Rwmg_inter_Vx_string,Rbody_inter_Vx_string,Rsum_inter_Vx_string,
        Mx1_inter_Vx_string,Mx2_inter_Vx_string,MxWMG_inter_Vx_string,MxSum_inter_Vx_string,
        Vn_counter_h1
    )