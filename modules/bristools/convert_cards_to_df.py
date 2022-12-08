import os
import numpy as np
import pandas as pd

def convert_cards_to_df(prm,cards,nwrk,npp):

    # Convert list of dictionaries to dataframe
    features = pd.DataFrame(cards)

    # Identify dataframe columns that are lists
    list_cols = []
    for col_name in features.columns:
        if(isinstance(features[col_name][0],list)):
            list_cols.append(col_name)

    # Identify pp versus wrk column of lists
    pp_col_names = []
    wrk_col_names = []
    for col_name in list_cols:
        pcs = col_name.split('_')
        if(pcs[0]=='pp'):
            pp_col_names.append(col_name)
        else:
            wrk_col_names.append(col_name)

    # Split WRK dataframe list elements into columns
    for col_name in wrk_col_names:
        new_col_names = []
        for i in range(0,nwrk):
            new_col_names.append(col_name + '_' + str(i))
        features[new_col_names]  =  pd.DataFrame(features[col_name].tolist())
        features = features.drop(columns=[col_name])

    # Split PP dataframe list elements into columns
    for col_name in pp_col_names:
        new_col_names = []
        for i in range(0,npp):
            new_col_names.append(col_name + '_' + str(i))
        features[new_col_names]  =  pd.DataFrame(features[col_name].tolist())
        features = features.drop(columns=[col_name])

    return(features)
