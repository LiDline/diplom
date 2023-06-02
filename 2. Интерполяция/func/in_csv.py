import pandas as pd
import numpy as np


import constants


Vn_step = constants.VX_STEP_ANSYS
h_step = constants.H_STEP_ANSYS
n_step = constants.N_STEP_ANSYS
n_inter = constants.N_STEP_INTER
h_inter = constants.H_STEP_INTER
Vx_inter = constants.VX_STEP_INTER


def in_csv(
        T1_inter_Vx_string,T2_inter_Vx_string,Rring1_inter_Vx_string,Rring2_inter_Vx_string,
        Rwmg_inter_Vx_string,Rbody_inter_Vx_string,Rsum_inter_Vx_string,
        Mx1_inter_Vx_string,Mx2_inter_Vx_string,MxWMG_inter_Vx_string,MxSum_inter_Vx_string,
        df,list1,Vn_counter_h1
):
    
    print()
    print('Создание таблицы...')

    """n2"""

    n2_inter_5 = []

    for i in range (0, len(T1_inter_Vx_string)//len(list1)):
        n2_inter_5 = np.append(n2_inter_5, np.arange(int(df['n2 [об/мин]'].min()),int(df['n2 [об/мин]'].max())+n_inter,n_inter))
        
    print('--n2')

    """h2"""

    h2_inter_5 = []
    list20 = []
    k = df['h2 [град]'].min()   

    for i in range (0, (len(T1_inter_Vx_string)//len(list1))):
        if k <= df['h2 [град]'].max():
            list20 = [k]*len(range(int(df['n2 [об/мин]'].min()), int(df['n2 [об/мин]'].max())+n_inter, n_inter))
            h2_inter_5 = np.append(h2_inter_5, list20)
            k += h_inter
        else:
            k = df['h2 [град]'].min()
            list20 = [k]*len(range(int(df['n2 [об/мин]'].min()), int(df['n2 [об/мин]'].max())+n_inter, n_inter))
            h2_inter_5 = np.append(h2_inter_5, list20)
            k += h_inter

    print('--h2')

    """n1"""

    n1_inter_5 = []
    list21 = []
    k = int(df['n1 [об/мин]'].min())
    for i in range (0, len(T1_inter_Vx_string)//
                    (len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter))*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)))):
        if k <= df['n1 [об/мин]'].max():
            list21 = [k]*len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter))*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))
            n1_inter_5 = np.append(n1_inter_5, list21)
            k += n_inter
        else:
            k = int(df['n1 [об/мин]'].min())
            list21 = [k]*len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter))*len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))
            n1_inter_5 = np.append(n1_inter_5, list21)
            k += n_inter
    
    print('--n1')

    """h1"""

    list22 = []
    h1_inter_5 = []
    k = df['h1 [град]'].min()

    for i in range (0, (len(T1_inter_Vx_string) //
                     (len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter)) *
                     len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) * 
                     (len(np.arange(df['n1 [об/мин]'].min(), df['n1 [об/мин]'].max()+n_inter, n_inter)))))):
        if k <= df['h1 [град]'].max():
            list22 = [k]*((len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter)) * 
            len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) * 
            (len(np.arange(df['n1 [об/мин]'].min(), df['n1 [об/мин]'].max()+n_inter, n_inter)))))
            h1_inter_5 = np.append(h1_inter_5, list22)
            k += h_inter
        else:
            k = df['h1 [град]'].min()
            list22 = [k]*((len(np.arange(df['n2 [об/мин]'].min(), df['n2 [об/мин]'].max()+n_inter, n_inter)) * 
            len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter)) * 
            (len(np.arange(df['n1 [об/мин]'].min(), df['n1 [об/мин]'].max()+n_inter, n_inter)))))
            h1_inter_5 = np.append(h1_inter_5, list22)
            k += h_inter
    
    print('--h1')

    """Vx"""

    list22 = []
    Vx_inter_5 = []
    k = (df['Vн [км/ч]'].min())
    for i in range (0, len(T1_inter_Vx_string)//Vn_counter_h1):
        list22 = [k]*Vn_counter_h1
        Vx_inter_5 =  np.append(Vx_inter_5, list22)
        k += Vx_inter
    
    print('--Vx')

    """Таблица"""

    df_inter_5 = pd.DataFrame(columns = constants.COLUMNS_AFTER_TRANSITION)
    df_inter_5['Тв1 [Н]'] = T1_inter_Vx_string
    df_inter_5['Тв2 [Н]'] = T2_inter_Vx_string
    df_inter_5['Rк1 [Н]'] = Rring1_inter_Vx_string
    df_inter_5['Rк2 [Н]'] = Rring2_inter_Vx_string
    df_inter_5['R ВМГ [Н]'] = Rwmg_inter_Vx_string
    df_inter_5['R тела [Н]'] = Rbody_inter_Vx_string
    df_inter_5['R сум [Н]'] = Rsum_inter_Vx_string

    df_inter_5['Mвx1 [Н*м]'] = Mx1_inter_Vx_string
    df_inter_5['Mвx2 [Н*м]'] = Mx2_inter_Vx_string
    df_inter_5['Mx ВМГ [Н*м]'] = MxWMG_inter_Vx_string
    df_inter_5['Mx сум [Н*м]'] = MxSum_inter_Vx_string

    df_inter_5['n2 [об/мин]'] = - n2_inter_5
    df_inter_5['h2 [град]'] = - h2_inter_5
    df_inter_5['n1 [об/мин]'] = n1_inter_5
    df_inter_5['h1 [град]'] = h1_inter_5
    df_inter_5['Vн [км/ч]'] = Vx_inter_5

    print('Таблица создана.')

    return df_inter_5