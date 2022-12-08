import csv

from bristools.result_line_parse import *

def load_result(prm,path,card,year):

    input_path = path + card + str(year) + '.1'
    surf_dict = dict()
    surfcnd_dict = dict()
    weather_dict = dict()
    temp_dict = dict()
    wps_pool_dict = dict()
    runup_dict = dict()

    with open(input_path,'r') as fh:

        reader = csv.reader(fh)

        for line in reader:

            race_num = int(line[2].strip())
            surf = line[8].strip()   # includes new (A) for all-weather indicator
            surf_cnd = line[37].strip()
            weather = line[62].strip()
            temp = line[63].strip()
            wps_pool = line[64].strip()
            runup = line[65].strip() # no units specified (feet?)

            surf_dict[race_num] = surf
            surfcnd_dict[race_num] = surf_cnd
            weather_dict[race_num] = weather
            temp_dict[race_num] = temp
            wps_pool_dict[race_num] = wps_pool
            runup_dict[race_num] = runup

            
    results_path = path + card + str(year) + '.2'
    all_results = []
    with open(results_path,'r') as fh:

        reader = csv.reader(fh)
        
        ## Each line of the results is a horse in a race
        for line in reader:

            ## Parse the horse's data (this function grabs all the data available)
            result = result_line_parse(prm,line)

            ## Add in race-level data from prior result read
            result['surf'] =  surf_dict[result['race_num']]
            result['surfcnd'] = surfcnd_dict[result['race_num']]
            result['weather'] = weather_dict[result['race_num']]
            result['temp'] = temp_dict[result['race_num']]
            result['wps_pool'] = wps_pool_dict[result['race_num']]
            result['runup'] = runup_dict[result['race_num']]
            
            all_results.append(result)

    return(all_results,result.keys())
