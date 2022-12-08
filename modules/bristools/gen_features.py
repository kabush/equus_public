import logging
import pandas as pd

from bristools.scan_cards import *
from bristools.load_single_card import *
from bristools.convert_cards_to_df import *
from bristools.load_result import *

def gen_features(prm,vrsn_name):

    # ----------------------------------------
    # Loading entry, past performance, and workout data

    # Survey available cards
    pp_cards = scan_cards(prm,prm.path_pp)

    # Initialize log section
    logging.info('Loading PPs for all cards')

    features = pd.DataFrame()
    
    for card in pp_cards:

        print(card)
        
        # ----------------------------------------
        # Load card
        path_card  = prm.path_pp + card['year'] + '/' + card['card'] + '.DRF'
        pp_raw = load_single_card(prm,path_card,prm.max_nwrk,prm.max_npp)

        # Convert card to a data frame
        pp = convert_cards_to_df(prm,pp_raw,prm.max_nwrk,prm.max_npp)

        # ----------------------------------------
        # Load corresponding result
        path_result = prm.path_res + card['year'] + '/'
        res_dict,keys = load_result(prm,path_result,card['card'],card['year'])

        # Construct result dataframe from dict()
        result = pd.DataFrame(res_dict,columns = keys)
        
        # Adjust result column names to not clash with PP column names
        col_names = []
        for key in keys:
            col_names.append('res_' + key)
        result.columns = col_names
        
        # Clean result names to exactly match PP format
        names = []
        for index,row in result.iterrows():
            name = row['res_name']
            name = re.sub('\((.+)\)', '', name) # Remove international symbol
            name = name.rstrip()
            names.append(name)
        result['cln_name'] = names
        
        # ----------------------------------------
        # Order the results to exactly match the PPs (including missing data)
        pp_reorder = pd.DataFrame()
        result_reorder = pd.DataFrame()
        for index,row in pp.iterrows():
            
            search_track = row['ent_track']
            search_date = row['ent_date']
            search_race_num = int(row['ent_race_num']) # Tmp. cast to achieve this step
            search_post = row['ent_post']
            search_name = row['ent_name']
            
            found_row = result[(result['res_track']==search_track) & (result['res_date']==search_date) &
                                 (result['res_race_num']==search_race_num) & (result['cln_name']==search_name)]

            # Occasionally the result contains duplicate result entries (remove these duplicates - seems to
            # happen to specific horses - may be database problem)
            if(found_row.shape[0]>1):
                found_row = found_row.iloc[0].to_frame().T
            
            # This check handles cards for which races were cancelled (usually due to weather)
            if(not found_row.empty):
                result_reorder = pd.concat([result_reorder,found_row],axis=0)
                pp_reorder = pd.concat([pp_reorder,row.to_frame().T],axis=0)
            else:
                if(found_row.empty):
                    logging.info('WARNING: Result does not match a PP')
                    logging.info('   -' + str(search_track))
                    logging.info('   -' + str(search_date))
                    logging.info('   -' + str(search_race_num))
                    logging.info('   -' + str(search_post))
                    logging.info('   -' + str(search_name))

        # Format the assembled pps/results
        result_reorder.reset_index(inplace=True,drop=True)
        pp_reorder.reset_index(inplace=True,drop=True)
        
        # Combine PPs and Results into a single dataset
        data = pd.concat([pp_reorder,result_reorder],axis=1)

        # Construct dataset card-by-card
        features = pd.concat([features,data],axis=0)

    # Clean-up
    features.reset_index(inplace=True,drop=True)
    print(features)
    
    # Write to file
    features.to_csv(prm.path_features + vrsn_name + '/features.csv',index=False)
