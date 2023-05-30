import pandas as pd
import warnings


# Отключаем FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

def sorting(df):
    Vn_counter_0 = round((df["Vн [км/ч]"].max() - df["Vн [км/ч]"].min()) / 2.5 + 1)
    h1_counter_0 = round((df["h1 [град]"].max() - df["h1 [град]"].min()) / 2.5 + 1)
    n12_counter_0 = round((df["n1 [об/мин]"].max() - df["n1 [об/мин]"].min()) / 250 + 1)

    df_done = pd.DataFrame()

    Vx_0 = df["Vн [км/ч]"].min()
    Vx_step = 2.5

    h_step = 2.5

    n_0 = df["n1 [об/мин]"].min()
    n_step = 250

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
