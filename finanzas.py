import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

import boa
from boa.utils.date import duration_ratio, periods_in_year


Data = pd.read_excel("Calculo_de_resultados.xls")

close = Data['close']

porc_rend_diario = close.returns()

rend_diario = [0]
for i in range(1, len(close)):
    rend_diario.append(porc_rend_diario[i]*close[i])

porc_perf_acum = close.returns().cum_returns()
perform_acum = porc_perf_acum*close[0]

rolling_perf_261 = close.rolling_equity()
dd_acum = close.drawdown()
rollind_dd_261 = close.rolling_drawdown()

run_up_acum = close.runup()
rolling_runup_acum = close.rolling_runup()

print(porc_rend_diario.volatility())
print(close.returns(None, 'W-Fri').volatility() * 100)


tabla = pd.DataFrame({'date': Data['date'],
                      'close': Data['close'],
                      'Rendimientos diaros': rend_diario,
                      '% Rendimiento diarios' : porc_rend_diario,
                      'Performance acumulado': perform_acum,
                      '% Performance acumulado': porc_perf_acum,
                      '%Rolling performance (ventana 261)' : rolling_perf_261,
                      '%Drawdown acumulado' : dd_acum,
                      '%Run Up acumulado' : run_up_acum,
                      '%Rolling drawdown acumulado (ventana 261)' : rollind_dd_261,
                      '%Rolling runup acumulado (ventana 261)' : rolling_runup_acum
                      })
#                      '%Rolling volatilidad (ventana 22)' : []
#                      '%Rolling volatilidad (ventana 261)' : []
#                      })

print(tabla)
