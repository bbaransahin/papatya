import numpy as np
import pandas as pd

from papatya import errors

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
        raise errors.InvalidShape("Given ndarray's shape must be 1-D or 2-D but found "+str(len(nd.shape))+"-D.")

    return np.asarray(return_val)

def get_max_min(s, print_output=True):
    '''
    This function takes an iterable array like object and returns min and max values of it.
    It works with 1-D and 2-D arrays.
    implemented 2-D's:
        pandas.core.frame.DataFrame
        numpy.ndarray
    Note:
        Using builtin functions as max() and min() is valid for 1-D iterables but won't work
    with 2-D iterables, so this function provides a more generalised functionality.
    '''
    if (
            (type(s) == np.ndarray and len(s.shape) == 1)
            or type(s) == pd.core.series.Series
            ):
        max_val = max(s)
        min_val = min(s)
    elif (type(s) == np.ndarray and len(s.shape) == 2):
        max_val = s[0][0]
        min_val = s[0][0]
        for i in s:
            for j in i:
                if (j > max_val):
                    max_val = j
                if (j < min_val):
                    min_val = j
    elif (type(s) == pd.core.frame.DataFrame):
        max_val = s[0][0]
        min_val = s[0][0]
        for i in s:
            for j in s[i]:
                if (j > max_val):
                    max_val = j
                if (j < min_val):
                    min_val = j
    else:
        raise errors.UnknownTypeError("Given data type is unknown. Found data type "+str(type(s))+".")

    if (print_output):
        print('max, min = ('+str(min_val)+',',str(max_val)+')')

    return min_val, max_val
