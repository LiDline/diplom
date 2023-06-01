import numpy as np



# Записал новые значения в виде строки для следующего преобразования
def in_matrix_form_for_h2(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, list1, R1, h2_counter_0, h_inter, df):

    k = 0

    T1_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*  #количество диапазонов от 20 до 30
                               len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    T2_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Rring1_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Rring2_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Rwmg_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Rbody_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Rsum_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))

    Mx1_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    Mx2_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    MxWMG_inter_h2_string = np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))
    MxSum_inter_h2_string =  np.zeros((len(list1)*len(R1)//h2_counter_0*
                                   len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))))



    for i in range (0, len(R1)//h2_counter_0 * len(np.arange(df['h2 [град]'].min(), df['h2 [град]'].max()+h_inter, h_inter))):
        for j in range (0, len(list1)):
            T1_inter_h2_string[k] = a1[i,j]
            T2_inter_h2_string[k] = a2[i,j]
            Rring1_inter_h2_string[k]  = a3[i,j]
            Rring2_inter_h2_string[k]  = a4[i,j]
            Rwmg_inter_h2_string[k] = a5[i,j]
            Rbody_inter_h2_string[k] = a6[i,j]
            Rsum_inter_h2_string[k]= a7[i,j]

            Mx1_inter_h2_string[k]  = a8[i,j]
            Mx2_inter_h2_string[k]  = a9[i,j]
            MxWMG_inter_h2_string[k] = a10[i,j]
            MxSum_inter_h2_string[k] = a11[i,j]


            k += 1


    return (
        T1_inter_h2_string,
        T2_inter_h2_string,
        Rring1_inter_h2_string,
        Rring2_inter_h2_string,
        Rwmg_inter_h2_string,
        Rbody_inter_h2_string,
        Rsum_inter_h2_string,
        Mx1_inter_h2_string,
        Mx2_inter_h2_string,
        MxWMG_inter_h2_string,
        MxSum_inter_h2_string,
    )