import pandas as pd;
import plotly.express as px

def read_egresos(year: int, boxplotedad: bool, boxplotpeso: bool, boxplottalla: bool) -> pd.DataFrame:
    columns = ['LOC', 'MUNIC', 'DIAG_INI', 'EDAD', 'SEXO', 'PESO', 'TALLA']
    '''
    En está función requiere de tres parametos:
    - year (int) : año de registro de egresos (2010, 2011, 2012, 2013, 2014, 2015, 2016, 2018).
    - boxplotedad (bool) : Su valor indica si se desea generar un boxplot por edad del registro.
    - boxplotpeso (bool) : Su valor indica si se desea generar un boxplot por peso del registro.
    - boxplottalla (bool) : Su valor indica si se desea generar un boxplot por talla del registro.
    '''
    # leer todos los registros del año especificado, 2017 es una excepción debido a que no está separado por comas.
    if (year == 2017):
        df = pd.read_csv(
            f'data/EGRESO_{year}.csv',
            sep='|',
            usecols=columns,
            dtype={'LOC' : pd.Int64Dtype(),
            'MUNIC' : pd.Int64Dtype(),
            'DIAG_INI' : str,
            'EDAD' : pd.Int64Dtype(),
            'SEXO' : pd.Int64Dtype(),
            'PESO' : float,
            'TALLA' : float}
        ).dropna()
    else:
        df = pd.read_csv(
            f'data/EGRESO_{year}.csv',
            usecols=columns,
            dtype={'LOC' : pd.Int64Dtype(),
            'MUNIC' : pd.Int64Dtype(),
            'DIAG_INI' : str,
            'EDAD' : pd.Int64Dtype(),
            'SEXO' : pd.Int64Dtype(),
            'PESO' : float,
            'TALLA' : float}
        ).dropna()
    # reemplazar todos los valores asociados a N/A. y dropearlos.
    df2 = df.replace([999,999.0,999.00], pd.NA).dropna()
    # filtrado por localidad y municipios del área metropolitana de Monterrey.
    municipios = [6, 18, 26, 31, 39, 46, 19, 48, 21]
    df_nl = df2[df2.LOC == 19]
    df_am = df_nl[df_nl.MUNIC.isin(municipios)]

    if (boxplotedad):
        # bloxplot por edad
        box_edad = df_am.boxplot(column= 'EDAD', by = 'DIAG_INI', fontsize=10, rot=90, grid = False, figsize=(30,14))
        box_edad.figure.savefig('images/boxplot_edad')
        #box_edad.figure.show()

    if (boxplotpeso):
        # bloxplot por peso
        box_peso = df_am.boxplot(column= 'PESO', by = 'DIAG_INI', fontsize=10, rot=90, grid = False, figsize=(30,14))
        box_peso.figure.savefig('images/boxplot_peso')
        #box_peso.figure.show()

    if (boxplottalla):
        # bloxplot por talla
        box_talla = df_am.boxplot(column= 'TALLA', by = 'DIAG_INI', fontsize=10, rot=90, grid = False, figsize=(30,14))
        box_talla.figure.savefig('images/boxplot_talla')
        #box_talla.figure.show()

    return df_am.head()
