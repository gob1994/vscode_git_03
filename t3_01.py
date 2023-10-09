import numpy as np
print(np.random.randint(1,100,size=(3,4)))
import pandas as pd
df = pd.DataFrame(np.random.randint(1,100,size=(5,4)),columns=list('ABCD'))
print(df)