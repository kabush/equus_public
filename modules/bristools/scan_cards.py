import logging
import os

def scan_cards(prm,path_cards):

    # Initialize log section
    logging.info('Scanning all PP files')
    
    # Construct list of PP cards
    logging.info('Clear /tmp directory') 
    os.system('! rm -rf ' + prm.path_tmp)
    os.system('! mkdir ' + prm.path_tmp)

    # Construct list of PP cards
    os.system('! ls ' + path_cards + ' > ' + prm.path_tmp + 'years.txt')
    pp_list = []
    with open(prm.path_tmp + 'years.txt') as fh:

        for line in fh:

            year = line.rstrip()

            os.system('! ls ' + path_cards + year + ' > ' + prm.path_tmp + 'card_' + str(year) + '.txt')

            with open(prm.path_tmp + 'card_' + str(year) + '.txt') as cfh:

                for cline in cfh:

                    filename = cline.rstrip()
                    pcs = filename.split('.')

                    card = dict()
                    card['card'] = pcs[0]  #Track and date: BRIS format = TTTMMDD
                    card['year'] = year
                    pp_list.append(card)

    # Clean-up
    os.system('! rm ' + prm.path_tmp + '*.txt')

    return(pp_list)    
