import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("graphing.csv")

df = df[df['Class']== 4]
print(len(df))
std_dev_lamda = (df['Lambda']).std()
std_dev_lamda_t = (df['Lambda_t']).std()
std_dev_H = (df['H']).std()
std_dev_H_t = (df['H_t']).std()
std_dev_lz = (df['Lempel-Ziv Complexity']).std()

print(f'stdev lam    : {std_dev_lamda}')
print(f'stdev lam_t  : {std_dev_lamda_t}')
print(f'stdev h      : {std_dev_H}')
print(f'stdev h_t    : {std_dev_H_t}')
print(f'stdev l_z    : {std_dev_lz}')

avg_dev_lamda = (df['Lambda']).mean()
avg_dev_lamda_t = (df['Lambda_t']).mean()
avg_dev_H = (df['H']).mean()
avg_dev_H_t = (df['H_t']).mean()
avg_dev_lz = (df['Lempel-Ziv Complexity']).mean()

print('\n')
print(f'mean lam    : {avg_dev_lamda}')
print(f'mean lam_t  : {avg_dev_lamda_t}')
print(f'mean h      : {avg_dev_H}')
print(f'mean h_t    : {avg_dev_H_t}')
print(f'mean l_z    : {avg_dev_lz}')
print('\n')
print(f'spread lam  : {std_dev_lamda/avg_dev_lamda}')
print(f'spread lam_t: {std_dev_lamda_t/avg_dev_lamda_t}')
print(f'spread h    : {std_dev_H/avg_dev_H}')
print(f'spread h_t  : {std_dev_H_t/avg_dev_H_t}')
print(f'spread l_z  : {std_dev_lz/avg_dev_lz}')
