from func.scipy_interpolation import scipy_interpolation

def perform_scipy_interpolation(args):
    df, matrix1, matrix2, h2_counter_0, h_inter, col_name, h2, list = args
    return scipy_interpolation(df, matrix1, matrix2, h2_counter_0, h_inter, col_name, h2, list)