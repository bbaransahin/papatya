import numpy as np
import pandas as pd

def nanstat_ndarray(nd, print_output=True):
    '''
    This function analyzes the ndarray (or list) and prints results (if print_output parameter left as True).
    1-D and 2-D arrays implemented
    1-D return:
        A numpy array as [total_nan_vals, total_vals]
    2-D return:
        A numpy array as [total_nan_vals, total_vals, column[0]_nan_vals, column[1]_nan_vals, ...]
    '''
    nan_array = pd.isnull(nd)
    return_val = []
    if(len(nd.shape) == 1):
        c = 0
        for i in nan_array:
            if(i):
                c+=1
        print("Nan values:", str(c)+"/"+str(len(nd)), "%"+str(c/float(len(nd))*100), "is nan values.")
        return_val.append(c)
        return_val.append(len(nd))
    elif(len(nd.shape) == 2):
        total_c = 0
        c_columns = []
        for i in range(nd.shape[1]):
            c_columns.append(0)
        for i in nan_array:
            for j in range(nd.shape[1]):
                if(i[j]):
                    total_c+=1
                    c_columns[j]+=1
        print("Total nan values:", str(total_c)+"/"+str(nd.shape[0]*nd.shape[1]), "%"+str(total_c/float(nd.shape[0]*nd.shape[1])*100), "is nan values.")
        return_val.append(total_c)
        return_val.append(nd.shape[0]*nd.shape[1])
        for i in range(nd.shape[1]):
            print("Column["+str(i)+"] nan values:", str(c_columns[i])+"/"+str(nd.shape[0]), "%"+str(c_columns[i]/float(nd.shape[0])*100), "is nan values.")
            return_val.append(c_columns[i])
    else:
        print("Unknown shape", nd.shape,"returning None.")
        return None

    return np.asarray(return_val)
