# Используемые константы

COLUMNS_AFTER_CALCULATIONS = [
    "h1 [град]",
    "h2 [град]",
    "Vн [км/ч]",
    "n1 [об/мин]",
    "n2 [об/мин]",
    "Тв1 [Н]",
    "Тв2 [Н]",
    "Rк1 [Н]",
    "Rк2 [Н]",
    "R ВМГ [Н]",
    "R тела [Н]",
    "R сум [Н]",
    "Mвx1 [Н*м]",
    "Mвx2 [Н*м]",
    "Mx ВМГ [Н*м]",
    "Mx сум [Н*м]",
]

COLUMNS_AFTER_TRANSITION = [
    "Vн [км/ч]",
    "h1 [град]",
    "n1 [об/мин]",
    "h2 [град]",
    "n2 [об/мин]",
    "Тв1 [Н]",
    "Тв2 [Н]",
    "Rк1 [Н]",
    "Rк2 [Н]",
    "R ВМГ [Н]",
    "R тела [Н]",
    "R сум [Н]",
    "Mвx1 [Н*м]",
    "Mвx2 [Н*м]",
    "Mx ВМГ [Н*м]",
    "Mx сум [Н*м]",
]

VX_STEP_ANSYS = 2.5
H_STEP_ANSYS = 2.5
N_STEP_ANSYS = 250

# Тип интерполяции
KIND_LIST = [
    "linear",
    "nearest",
    "zero",
    "slinear",
    "quadratic",
    "cubic",
    "previous",
    "next",
]
KIND = KIND_LIST[5]

N_STEP_INTER = 50
H_STEP_INTER = 0.5
VX_STEP_INTER = 0.5

INTERPOLATED_CHARACTERISTICS = COLUMNS_AFTER_TRANSITION[5:]

NEW_CHARACTERISTICS = [
    "Wв1 [Вт]",
    "Wв2 [Вт]",
    "W сум [Вт]",
    'Mкx [Н*м]'
]

NAME_LEGEND = [f'n1 [0:{N_STEP_INTER}:1500]', f'n2 [0:{N_STEP_INTER}:1500]',f'h1 [20:{H_STEP_INTER}:35]',f'h2 [20:{H_STEP_INTER}:35]',
               'Wв', '-Mвx1','Mвx2','Тв1','Тв2','Tк1','Tк2','Wв1', 'Wв2','MКx', '-R', 'T', 'Fx']

MX_MAX = 0.2
R_MAX = 4