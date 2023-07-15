import numpy as np
from random import random as random
from pandas import DataFrame
from pandas import read_csv
from warnings import filterwarnings as message
from matplotlib import pyplot 
from sklearn.model_selection import train_test_split

from PICK_UP import pick_processors
from manic import df_load
from one_try import NeuralNetwork
from os import system
message('ignore')
system('clear')



example=DataFrame(read_csv('data/learning_data.csv'
                ).drop(columns=['Unnamed: 0', 'y'], axis=1).T[19]).T

example['love']=np.ones(1)

columns=example.columns
example.columns=range(len(example.columns))
example


df=df_load()

print('\n'*1)



df=df.astype('float16')
df.columns=range(len(df.columns))

_weights_=read_csv('weights/_weights_.csv').drop(columns=['Unnamed: 0'], axis=1)
__weights__=read_csv('weights/__weights__.csv').drop(columns=['Unnamed: 0'], axis=1)
___weights___=read_csv('weights/___weights___.csv').drop(columns=['Unnamed: 0'], axis=1)



all_proc_data=example.T.join(df.T)
all_proc_data.columns=range(len(all_proc_data.columns))

df_errors=DataFrame(all_proc_data[1]-all_proc_data[0]).T
df_errors.columns=columns

errors_config=['UP ERRORS' if error>0 else 'DOWN ERRORS' for error in df_errors.T[0]]
df_errors=df_errors.T

df_errors[1]=errors_config
df_errors.columns=['Your loss','CONFIG TO GOOD']

NN=NeuralNetwork

print('Your score in all processing-> ',NN.step_all(in_values=df, _weights_=_weights_,
           __weights__=__weights__,___weights___=___weights___), '\n')

df_errors.index=columns
print(df_errors)
