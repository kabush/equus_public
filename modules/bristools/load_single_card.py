import csv

from bristools.pp_line_parse import *

def load_single_card(prm,pp_path,nwrk,npp):

    # Each line is a horse
    with open(pp_path,'r') as fh:

        reader = csv.reader(fh)

        # Each line of the card is a horse in a race
        all_pp_list = []
        for line in reader:

            # Parse the horse's data
            pp = pp_line_parse(prm,line) 

            if(nwrk>0):
                
                # Convert list of wrk dictionaries to lists of keys
                wrk_keys = pp['wrk'][0].keys()
                for key in wrk_keys:
                    key_name = 'wrk_' + key
                    pp[key_name] = []
                    for i in range(pp['nwrk']):
                        tmp_dict = pp['wrk'][i]
                        pp[key_name].append(tmp_dict[key])
                pp.pop('wrk')

            if(npp>0):
                
                # Convert list of pp dictionaries to lists of keys
                pp_keys = pp['pp'][0].keys()
                for key in pp_keys:
                    key_name = 'pp_' + key
                    pp[key_name] = []
                    for i in range(pp['npp']):
                        tmp_dict = pp['pp'][i]
                        pp[key_name].append(tmp_dict[key])
                pp.pop('pp')

            # Add to list of processed PPs
            all_pp_list.append(pp)
    
    return(all_pp_list)
