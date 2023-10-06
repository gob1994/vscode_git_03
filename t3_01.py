import numpy as np
print(np.random.randint(1,100,size=(3,4)))
#引入pandas,并创建一个5行4列的dataframe
import pandas as pd
df = pd.DataFrame(np.random.randint(1,100,size=(5,4)),columns=list('ABCD'))
print(df)