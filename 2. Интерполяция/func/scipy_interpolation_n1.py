import numpy as np


import constants
from func.in_matrix_from_string import in_matrix_from_string
from func.from_matrix_in_string import from_matrix_in_string


kind = constants.KIND[5]
Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
name = constants.INTERPOLATED_CHARACTERISTICS


def scipy_interpolation_n1(
        df,T1_inter_h2_string, T2_inter_h2_string,Rring1_inter_h2_string,Rring2_inter_h2_string,
        Rwmg_inter_h2_string,Rbody_inter_h2_string,Rsum_inter_h2_string,
        Mx1_inter_h2_string,Mx2_inter_h2_string,MxWMG_inter_h2_string,
        MxSum_inter_h2_string,h1_counter_0,list1
        ):

    Vn_counter_n1 = (h1_counter_0 * len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter)) *
                                                len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) *
                                                len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter)))
    

    # Записал новые значения в виде матрицы, где каждая строка - это n1
    i_counter_1 = len(T1_inter_h2_string)//(len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter))*
                                  len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)))
    j_counter_1 = (len(np.arange(0,int(df['n2 [об/мин]'].max())+n_inter,n_inter))*
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