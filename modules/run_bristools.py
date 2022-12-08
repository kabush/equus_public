import os
import argparse
import logging
from time import gmtime, strftime

import params as prm
from bristools.gen_features import *

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='The program constructs a *.csv file from all available data in /equus_public/inputs/<version>/')
    parser.add_argument('-v','--version',help='Dataset version name.', default='vrsn-NONE')
    args = parser.parse_args()

    # Create output directory (if necessary)
    out_path = prm.path_outputs
    if(not os.path.isdir(out_path)):
        print('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
    
    # Create log directory (if necessary)
    out_path = prm.path_log
    if(not os.path.isdir(out_path)):
        print('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
    
    # Create tmp directory (if necessary)
    out_path = prm.path_tmp
    if(not os.path.isdir(out_path)):
        print('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
        
    # Set-up logging (now that output and log is available)
    time_str = strftime('%Y_%b_%d_%H:%M:%S', gmtime())
    log_file = prm.path_log + 'run_bristools_' + time_str + '_log.txt'
    logging.basicConfig(filename=log_file, level=logging.INFO)
        
    # Create features directory (if necessary)
    out_path = prm.path_features
    if(not os.path.isdir(out_path)):
        logging.info('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
    
    # Create new dataset version directory (delete previous if necessary)
    out_path = prm.path_features + args.version + '/'
    if(os.path.isdir(out_path)):
        logging.info('Path ' + out_path + ' found!')
        logging.info('Removing ' + out_path)
        os.system('! rm -rf ' + out_path)
        logging.info('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
    else:
        logging.info('Path ' + out_path + ' not found')
        logging.info('Creating ' + out_path)
        os.system('! mkdir ' + out_path)
    
    # Generate features
    gen_features(prm,args.version)

if __name__ == '__main__':
    main()
