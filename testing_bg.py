# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


def  func_reporte_1():

    df_stock = pd.read_excel('/home/almagro/Escritorio/agusto_Tkinter/Stock Cencosud.xlsx')
    
    filtro_base_pagos = df_stock['BASE / GENERACION'] == 'BASE DE PAGOS'
    filtro_base_pagos = df_stock[filtro_base_pagos]

    cuentas_pagos = filtro_base_pagos['DNI'].count()

    indicadores_base_generacion = pd.DataFrame()
    indicadores_base_generacion[''] = ['BASE DE PAGOS', 'GENERACION', 'Total general']
    indicadores_base_generacion['Q Cuentas'] = ['cuentas_pagos_formato', 'cuentas_generacion_formato', 'total_cuentas_formato']
    indicadores_base_generacion['Deuda'] = ['deuda_pagos', 'deuda_generacion', 'total_deuda']
    indicadores_base_generacion['Prom Deuda'] = ['promedio_deuda_pagos', 'promedio_deuda_generacion', 'total_promedio_deuda']
    indicadores_base_generacion['Base de Pagos'] = ['ultimo_pago_formato', 'ultimo_pago_generacion_formato', 'total_ultimo_pago_formato']

    indicadores_base_generacion.to_excel('/home/cerebro/Documentos/code_python/apps/test2/indicadores_base_generacion.xlsx')

def  func_reporte_2():
    pass

def  func_reporte_3():
    pass

def  func_reporte_4():
    pass

def  func_reporte_5():
    pass

def  func_reporte_6():
    pass
