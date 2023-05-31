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
KIND = [
    "linear",
    "nearest",
    "zero",
    "slinear",
    "quadratic",
    "cubic",
    "previous",
    "next",
]

N_STEP_INTER = 125
H_STEP_INTER = 1.25
VX_STEP_INTER = 1.25

INTERPOLATED_CHARACTERISTICS = COLUMNS_AFTER_TRANSITION[5:]
