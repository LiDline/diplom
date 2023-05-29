from numpy import zeros

def search_points_in_table(df, Vn, n1, n2): 

    R_sum = zeros(len(Vn) * len(n1) * len(n2))
    counter = 0

    for i in range(len(Vn)):
        for j in range(len(n1)):
            for k in range(len(n2)):
                R_sum[counter] = df.loc[(df.loc[:, 'Vн [км/ч]'] == Vn[i]) & (df.loc[:, 'n1 [об/мин]'] == n1[j]) &
                (df.loc[:, 'n2 [об/мин]'] == n2[k]), 'R суммарная [Н]']
                
                counter += 1 
    return R_sum
