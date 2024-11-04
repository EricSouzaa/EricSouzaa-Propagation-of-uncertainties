import pandas as pd

data_base = {
    "Elements": ["Ca", "K", "Al", "Mg", "Na","C","H2O"],
    "Lines (in Å)": [
        "16136.823, 16150.763, 16157.364",
        "15163.067, 15168.376",
        "16718.957, 16750.564, 16763.360",
        "15740.716, 15748.988, 15765.842",
        "16373.853, 16388.858",
        "15977.7, 16184.9",
        "15256.8, 15258.3, 15258.4, 15259.2, 15259.4, 15270.6, 15315.7, 15317.3, 15317.5, 15353.6, 15360.5, 15447.6, 15455.8, 15461.5, 15503.6"
    ]
}

data_1 = {
    "Elements": ["Ni","Mn","Cr","V","Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15605.68, 15632.654, 16584.439, 16589.295, 16673.711, 16815.471, 16818.76",
        "15159.0, 15217.8, 15262.4",
        "15680.063",
        "15924.9",
        "15334.847, 15543.756, 15602.842, 15698.979, 15715.573, 16635.161",
        "15888.410, 15960.063, 16094.787, 16680.770",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16352.217, "
        "16354.582, 16364.590, 16368.135, 16581.250, 16582.013, 16866.688, 16871.895, 16879.090, 16884.530, 16886.279, "
        "16895.180, 16898.887",
        "15207.5, 15219.5, 15244.8, 15294.6, 15395, 15490.3, 15591.8, 15604, 15621.7, 15632, "
        "15648.5, 15662, 15692.5, 15723.5",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, "
        "16546.8, 16548.8, 16557.2, 16574.8, 16694.4, 16735.4, 16738.3, 16741.7, 16796.4, 16812.7, "
        "16814.1, 16889.6, 16892.9, 16922.7, 16935.1"
    ]
}

data_2 = {
    "Elements": ["Mn","V","Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15159",
        "15924.9",
        "15334.847, 15543.756, 15715.573",
        "15888.410",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16352.217, "
        "16354.582, 16364.590, 16368.135, 16581.250, 16582.013, 16866.688, 16871.895, 16879.090, 16884.530, 16886.279, "
        "16895.180, 16898.887",
        "15207.5, 15219.5, 15294.6, 15621.7, 15632, 15723.5",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, "
        "16546.8, 16548.8, 16557.2, 16574.8, 16889.6, 16892.9, 16935.1"
    ]
}

data_3 = {
    "Elements": ["Mn","V","Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15159",
        "15924.9",
        "15334.847, 15543.756, 15715.573",
        "15888.410",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16352.217, "
        "16354.582, 16364.590, 16368.135, 16581.250, 16582.013, 16866.688, 16871.895, 16879.090, 16884.530, 16886.279, "
        "16895.180, 16898.887",
        "15294.6",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, "
        "16546.8, 16548.8, 16557.2, 16574.8, 16889.6, 16892.9, 16935.1"
    ]
}

data_4 = {
    "Elements": ["Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15334.847, 15543.756, 15715.573",
        "15888.410",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16352.217, "
        "16354.582, 16364.590, 16368.135, 16581.250, 16582.013, 16866.688, 16871.895, 16879.090, 16884.530, 16886.279, "
        "16895.180, 16898.887",
        "15294.6",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, "
        "16546.8, 16548.8, 16557.2, 16574.8, 16889.6, 16892.9, 16935.1"
    ]
}

data_5 = {
    "Elements": ["Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15334.847, 15543.756, 15715.573",
        "15888.410",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16352.217, "
        "16354.582, 16364.590, 16368.135, 16581.250, 16582.013, 16866.688, 16871.895, 16879.090, 16884.530, 16886.279, "
        "16895.180, 16898.887",
        "15294.6",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, 16546.8, 16548.8, "
        "16557.2, 16574.8, 16889.6, 16892.9, 16935.1"
    ]
}

data_6 = {
    "Elements": ["Ti","Si","OH","Fe I","FeH"],
    "Lines (in Å)": [
        "15334.847, 15543.756, 15715.573",
        "15888.410",
        "15391.208, 15407.288, 15409.308, 15505.782, 15558.023, 15560.244, 15565.961, 15568.780, 15572.084, 16052.765, "
        "16055.464, 16061.7, 16065.054, 16069.524, 16074.163, 16190.263, 16192.208, 16204.076, 16207.186, 16866.688, "
        "16871.895, 16879.090, 16884.530, 16886.279",
        "15294.6",
        "15965, 16009.6, 16018.5, 16108.1, 16114, 16245.7, 16271.8, 16284.7, 16299.4, 16377.4, 16546.8, 16548.8, "
        "16557.2, 16574.8, 16889.6, 16892.9, 16935.1"
    ]
}

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#Table_Base
df_base = pd.DataFrame(data_base)

df_table1 = pd.DataFrame(data_1)
df_table2 = pd.DataFrame(data_2)
df_table3 = pd.DataFrame(data_3)
df_table4 = pd.DataFrame(data_4)
df_table5 = pd.DataFrame(data_5)
df_table6 = pd.DataFrame(data_6)

df_combined1 = pd.concat([df_base, df_table1], ignore_index=True) #Combined Base + 2
df_combined2 = pd.concat([df_base, df_table2], ignore_index=True) #Combined Base + 3
df_combined3 = pd.concat([df_base, df_table3], ignore_index=True) #Combined Base + 4
df_combined4 = pd.concat([df_base, df_table4], ignore_index=True) #Combined Base + 5
df_combined5 = pd.concat([df_base, df_table5], ignore_index=True) #Combined Base + 6
df_combined6 = pd.concat([df_base, df_table6], ignore_index=True) #Combined Base + 7


# Mapeamento exato e intervalos de temperatura para as tabelas combinadas
temperature_tables = {
    4000: df_table1,
    3700: df_table1,
    3600: df_table2,
    3500: df_table3,
    3400: df_table4,
    3300: df_table5,
    3200: df_table6
}


def get_spectral_lines(teff):
    """Retorna o DataFrame df_base combinado com o DataFrame exato ou mais próximo da temperatura fornecida."""
    if teff in temperature_tables:
        df = temperature_tables[teff]
    else:
        closest_temp = min(temperature_tables.keys(), key=lambda x: abs(x - teff))
        df = temperature_tables[closest_temp]

    return pd.concat([df_base, df], ignore_index=True)
