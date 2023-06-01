import pandas as pd
import numpy as np
import sys
import os
import multiprocessing


sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
import constants

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "1. Расчёты",
        "1.3 Сортировка результатов расчётов",
    ),
)
from sorting_results import sorting_results
from func.scipy_interpolation_n2 import scipy_interpolation_n2
from func.scipy_interpolation_h2 import scipy_interpolation_h2


kind = constants.KIND[5]
Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER
name = constants.INTERPOLATED_CHARACTERISTICS


def math_interpolation(df):
    # Кол-во значений
    Vn_counter_0 = round((df["Vн [км/ч]"].max() - df["Vн [км/ч]"].min()) / Vn_step + 1)
    h1_counter_0 = round((df["h1 [град]"].max() - df["h1 [град]"].min()) / h_step + 1)
    n1_counter_0 = round(
        (df["n1 [об/мин]"].max() - df["n1 [об/мин]"].min()) / n_step + 1
    )
    h2_counter_0 = round((df["h2 [град]"].max() - df["h2 [град]"].min()) / h_step + 1)
    n2_counter_0 = round(
        (df["n2 [об/мин]"].max() - df["n2 [об/мин]"].min()) / n_step + 1
    )

    """Интерполяция по n2"""

    (
        T1_inter_n2,T2_inter_n2,Rring1_inter_n2,Rring2_inter_n2,
        Rwmg_inter_n2,Rbody_inter_n2,Rsum_inter_n2,Mx1_inter_n2,
        Mx2_inter_n2,MxWMG_inter_n2,MxSum_inter_n2,list1,
    ) = scipy_interpolation_n2(
        df, Vn_counter_0, h1_counter_0, n1_counter_0, h2_counter_0, n2_counter_0
    )

    """Интерполяция по h2"""

    (
        T1_inter_h2_matrix, T2_inter_h2_matrix,Rring1_inter_h2_matrix,Rring2_inter_h2_matrix,
        Rwmg_inter_h2_matrix,Rbody_inter_h2_matrix,Rsum_inter_h2_matrix,
        Mx1_inter_h2_matrix,Mx2_inter_h2_matrix,MxWMG_inter_h2_matrix,
        MxSum_inter_h2_matrix
        ) = scipy_interpolation_h2(
        df,h2_counter_0, h1_counter_0,n1_counter_0,
        T1_inter_n2,T2_inter_n2,Rring1_inter_n2,Rring2_inter_n2,Rwmg_inter_n2,
        Rbody_inter_n2, Rsum_inter_n2,Mx1_inter_n2, Mx2_inter_n2,
        MxWMG_inter_n2,MxSum_inter_n2, list1,
    )
    return len(T1_inter_h2_matrix), T1_inter_h2_matrix

if __name__ == '__main__':
    df_1, df_2 = sorting_results()
    print(math_interpolation(df_1))
