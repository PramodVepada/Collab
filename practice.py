import numpy as np
import pandas as pd
import numpy.random as npr

arr = npr.randint(50,100,16)
arr = arr.reshape(4,4)
df = pd.DataFrame(arr,columns = ['pramod','urvi','vivek','siddhesh'])


