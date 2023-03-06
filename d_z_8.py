#задача 1

import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array( [401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

M_X = zp.mean()
M_Y = ks.mean()
M_XY = (zp * ks).mean()


cov_ks = M_XY - M_X * M_Y
cov_ks

"9157.839999999997"

np.cov(zp, ks, ddof=0)

"array([[ 3494.64,  9157.84],"
"       [ 9157.84, 30468.89]])"

cov_ks2 = ((zp - zp.mean()) * (ks - ks.mean())).mean()
cov_ks2

"9157.84"

std_X = zp.std()
std_Y = ks.std()
corr_ks = cov_ks / (std_X * std_Y)
corr_ks

"0.8874900920739158"

np.corrcoef(zp, ks)

"array([[1.        , 0.88749009],"
"       [0.88749009, 1.        ]])"

# задача 2

X = np.array([131.0, 125.0, 115.0, 122.0, 131.0, 115.0, 107.0, 99.0, 125.0, 111.0])
mean_X = X.mean()
std_X = X.std(ddof=1)
mean_std_X = std_X / (np.sqrt(len(X)))
t_stat(mean_X, mean_std_X,len(X) - 1, 0.05, 'two-sided')

"Ответ: доверительный интервал (110.55608365158724, 125.64391634841274)"

#задача 3

mean_X = 174.2
std_X = np.sqrt(25)
mean_std_X = std_X / np.sqrt(27)
t_stat(mean_X, mean_std_X,27 - 1, 0.05, 'two-sided')


"Ответ доверительный интервал (172.2220658754539, 176.17793412454608)"