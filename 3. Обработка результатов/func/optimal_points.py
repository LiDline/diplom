import pandas as pd
from numpy import arange, zeros

import constants


Vn_step = constants.VX_STEP_INTER
Mx_max = constants.MX_MAX
R_max = constants.R_MAX

def optimal_points(df, full=None):

    df_done = pd.DataFrame()
    df_promez = pd.DataFrame()
    j = Vn_step

    if full == "3d":
    # max Vн с учётом шага, т.е. если шаг = 0.5, а Vн max = 27.5, то счётчик = 27.5 * 2
        for i in arange(Vn_step, df['Vн [км/ч]'].max() * (1 / Vn_step) + Vn_step, Vn_step):  
            df_promez = df[
                        (df['Mx сум [Н*м]'] > -Mx_max) & (df['Mx сум [Н*м]'] < Mx_max) & (df['Vн [км/ч]'] == i)  # Ограничения
                       &(df['n1 [об/мин]'] > 0) & (df['n2 [об/мин]'] < 0)
                       &(df['Тв1 [Н]'] > 0) & (df['Тв2 [Н]'] > 0)
                       &(df['W сум [Вт]'] > 0)
                      ]
            df_done = pd.concat([df_done, df_promez], ignore_index=True)
            j += Vn_step
        return df_done
    

    counter = round((df['Vн [км/ч]'].max() * (1 / Vn_step) + Vn_step) / Vn_step)
    counter_W, W_min_for_counter, Vx_for_counter = zeros(counter), zeros(counter), zeros(counter)
    k = 0

    for i in arange(Vn_step, df['Vн [км/ч]'].max() * (1 / Vn_step) + Vn_step, Vn_step):  
        df_promez = df[
                    (df['Mx сум [Н*м]'] > -Mx_max) & (df['Mx сум [Н*м]'] < Mx_max) & (df['Vн [км/ч]'] == i)  # Ограничения
                   &(df['R сум [Н]'] > -R_max) & (df['R сум [Н]'] < R_max)
                   &(df['n1 [об/мин]'] > 0) & (df['n2 [об/мин]'] < 0)
                   &(df['Тв1 [Н]'] > 0) & (df['Тв2 [Н]'] > 0)
                   &(df['W сум [Вт]'] > 0)
                  ]
        counter_W[k] = round(len(df_promez['W сум [Вт]']))
        W_min_for_counter[k] = df_promez['W сум [Вт]'].min()
        Vx_for_counter[k] = j
        k += 1
    
        df_done = pd.concat([df_done, df_promez], ignore_index=True)
        j += Vn_step

    if full == "optimal":
        res = pd.DataFrame()
        for i in arange(Vn_step, df['Vн [км/ч]'].max() * (1 / Vn_step) + Vn_step, Vn_step):
            df_promez = df_done[(df_done['Vн [км/ч]'] == i)]
            res = res.append(df_promez[(df_promez['W сум [Вт]'] == df_promez['W сум [Вт]'].min())], ignore_index=True)
        return res
    
    return df_done, counter_W, W_min_for_counter, Vx_for_counter