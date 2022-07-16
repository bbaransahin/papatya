import numpy as np
from tqdm import tqdm

def to_onehot(s, verbose=True):
    '''
    This function transforms a data (ndarray, pandas.Series, etc.) to onehot format and returns.
    '''
    vals = []
    onehot = []

    #These blocks are both same, only difference is the tqdm.
    if (verbose):
        for v in tqdm(s):
            if (not v in vals):
                vals.append(v)
                for i in onehot:
                    i.append(0)
            onehot_item = []
            ind = vals.index(v)
            for i in range(len(vals)):
                if (i == ind):
                    onehot_item.append(1)
                else:
                    onehot_item.append(0)
            onehot.append(onehot_item)
    else:
        for v in s:
            if (not v in vals):
                vals.append(v)
                for i in onehot:
                    i.append(0)
            onehot_item = []
            ind = vals.index(v)
            for i in range(len(vals)):
                if (i == ind):
                    onehot_item.append(1)
                else:
                    onehot_item.append(0)
            onehot.append(onehot_item)

    onehot = np.asarray(onehot)
    return onehot

def normalize(s, verbose=True):
    '''
    This function normalizes a data between 0 and 1.
    '''
    normalized = []
    max_val = s[0]
    min_val = s[0]
    for v in s:
        if (v > max_val):
            max_val = v
        if (v < min_val):
            min_val = v
    if (verbose):
        for v in tqdm(s):
            normalized.append((v-min_val)/float(max_val-min_val))
    else:
        for v in s:
            normalized.append((v-min_val)/float(max_val-min_val))

    normalized = np.asarray(normalized)
    return normalized
