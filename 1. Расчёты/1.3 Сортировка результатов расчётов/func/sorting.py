import pandas as pd
import warnings


import constants
# Отключаем FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

Vx_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS

def sorting(df):
    df['h2 [град]'] *=-1
    df['n2 [об/мин]'] *=-1
    # Пережиток с CFX, там у DI нельзя ставить 0
    df.loc[(df['n1 [об/мин]'] == 0.01), 'n1 [об/мин]'] = 0 
    df.loc[(df['n2 [об/мин]'] == 0.01), 'n2 [об/мин]'] = 0   

    Vn_counter_0 = round((df["Vн [км/ч]"].max() - df["Vн [км/ч]"].min()) / Vx_step + 1)
    h1_counter_0 = round((df["h1 [град]"].max() - df["h1 [град]"].min()) / h_step + 1)
    n12_counter_0 = round((df["n1 [об/мин]"].max() - df["n1 [об/мин]"].min()) / n_step + 1)
    df_done = pd.DataFrame()

    Vx_0 = df["Vн [км/ч]"].min()
    n_0 = df["n1 [об/мин]"].min()

    for i in range(0, Vn_counter_0):  # Смотрю куски по Vн
        df_Vx = pd.DataFrame()
        df_Vx = df[(df["Vн [км/ч]"] == Vx_0)]
        df_h1_2 = pd.DataFrame()
        h1 = df["h1 [град]"].min()

        for j in range(0, h1_counter_0):  # Смотрю куски по h1
            df_h1_1 = pd.DataFrame()
            df_h1_1 = df_Vx[(df_Vx["h1 [град]"] == h1)]

            df_n_1 = pd.DataFrame()
            df_n_2 = pd.DataFrame()
            n = n_0

            for k in range(0, n12_counter_0):  # Смотрю куски по n1
                df_n_1 = df_h1_1[(df_h1_1["n1 [об/мин]"] == n)]
                n += n_step
                df_n_2 = df_n_2.append(df_n_1, ignore_index=True)

            df_h1_2 = df_h1_2.append(df_n_2, ignore_index=True)
            h1 += h_step

        df_done = df_done.append(df_h1_2, ignore_index=True)
        Vx_0 += Vx_step

    return df_done.reset_index(drop=True)   
