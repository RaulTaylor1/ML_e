import pandas as pd
def data_report(df):
    '''Esta funcion describe los campos de un dataframe de pandas de forma bastante clara, crack'''
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])
    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])
    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])
    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])
    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)

    return concatenado.T



def info_nans(df):

    nan_info = pd.DataFrame({
        'Filas': len(df),
        'NaNs': df.isna().sum(),
        'Porcentaje': (df.isna().sum() / len(df)) * 100
    })

    return nan_info.round(2)



def min_max_df(df):
    max_min_df = pd.DataFrame(index=['min', 'max'], columns=df.columns)
    max_min_df.loc['min'] = df.min()
    max_min_df.loc['max'] = df.max()
    return max_min_df



def calcular_medias(df):
    medias = df.mean()
    return medias



