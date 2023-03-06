# 8___________________________________
from scipy import stats
import numpy as np
rest_sono = [24, 20, 28, 32, 36, 40, 44, 48]
reac_sono = [2, 3, 7, 8, 9, 12, 13, 16]
rest_sono = np.array(rest_sono, dtype=int)

slope, intercept, r_value, p_value, std_err = stats.linregress(rest_sono, reac_sono)
print(f' {slope}x {intercept}')

import matplotlib.pyplot as plt
plt.scatter(rest_sono, reac_sono)
plt.plot(rest_sono, intercept + slope*rest_sono, 'r', label='Linha ajustada')
plt.title('Diagrama de Dispersão')
plt.xlabel('Restrição')
plt.ylabel('Reação')
plt.legend()
plt.show()

y_pred = intercept + slope * rest_sono
SQregressao = sum((y_pred - reac_sono)**2)
print(f'sqregre = {SQregressao}')

SQtotal = sum((reac_sono - np.mean(reac_sono))**2)
print(f'sqtotal = {SQtotal}')

R_squared = 1 - (SQregressao / SQtotal)
print(f'R^2 = {R_squared}')
import math 
r = math.sqrt(R_squared)

t = r/math.sqrt((1-(r)**2)/8)
print(f' t= {t}')
