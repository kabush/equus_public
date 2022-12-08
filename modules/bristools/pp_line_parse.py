import re

def pp_line_parse(prm,line):

    record = dict()
    
    # Race details
    record['ent_track'] = line[0].strip().upper()
    record['ent_date'] = line[1].strip()
    record['ent_race_num'] = line[2].strip()
    record['ent_post'] = line[3].strip()
    record['ent_entry'] = line[4].strip().upper()
    record['ent_dist'] = line[5].strip()
    record['ent_surf'] = line[6].strip()  # No upper, case matters
    record['ent_type'] = line[8].strip().upper()
    record['ent_restrictions'] = line[9].strip().upper() #Age/sex restrictions
    record['ent_detail'] = line[10].strip().upper()
    record['ent_purse'] = line[11].strip().upper()
    record['ent_claiming_price'] = line[12].strip().upper()
    record['ent_claiming_price_horse'] = line[13].strip().upper()
    record['ent_race_conditions'] = line[14].strip().upper()
    record['ent_breed'] = line[22].strip().upper()
    record['ent_allweather'] = line[24].strip().upper()

    # Horse details
    record['ent_trnr'] = line[27].strip().upper()
    record['ent_trnr_curr_meet_starts'] = line[28].strip()
    record['ent_trnr_curr_meet_wins'] = line[29].strip()
    record['ent_trnr_curr_meet_plcs'] = line[30].strip()
    record['ent_trnr_curr_meet_shws'] = line[31].strip()

    record['ent_jock'] = line[32].strip().upper()
    record['ent_jock_wt_allow'] = line[33].strip()
    record['ent_jock_curr_meet_starts'] = line[34].strip()
    record['ent_jock_curr_meet_wins'] = line[35].strip()
    record['ent_jock_curr_meet_plcs'] = line[26].strip()
    record['ent_jock_curr_meet_shws'] = line[37].strip()

    record['ent_owner'] = line[38].strip().upper()
    
    record['ent_mto/ae_flag'] = line[40].strip().upper() #M=MTO, A=AE
    record['ent_program_num'] = line[42].strip().upper() # (if available)
    record['ent_mline'] = line[43].strip().upper()
    record['ent_name'] = line[44].strip().upper()
    record['ent_birth_year'] = line[45].strip()
    record['ent_birth_month'] = line[46].strip()
    record['ent_sex'] = line[48].strip().upper() # Map sex to F,M,G,C,H
    record['ent_weight'] = line[50].strip()
    record['ent_sire'] = line[51].strip().upper()
    record['ent_siresire'] = line[52].strip().upper()
    record['ent_dam'] = line[53].strip().upper()
    record['ent_damsire'] = line[54].strip().upper()
    record['ent_breeder'] = line[55].strip().upper()
    record['ent_state/country_abrv'] = line[56].strip().upper()
    record['ent_program_post'] = line[57].strip()

    record['ent_rx'] = line[61].strip().upper()  # includes 1st time lasix
    record['ent_eqp_chng'] = line[63].strip().upper()
    record['ent_starts'] = line[96].strip()
    record['ent_wins'] = line[97].strip()
    record['ent_plcs'] = line[98].strip()
    record['ent_shws'] = line[99].strip()
    record['ent_earnings'] = line[100].strip()
    
    record['ent_bris_run_style'] = line[209].strip().upper() # (E,E/P,P,S,N)
    record['ent_bris_quirin'] = line[210].strip() # (Quirin spd pts)
    record['ent_bris_pace_par_2f'] = line[213].strip()
    record['ent_bris_pace_par_4f'] = line[214].strip()
    record['ent_bris_pace_par_6f'] = line[215].strip()
    record['ent_bris_spd_par'] = line[216].strip()
    record['ent_bris_pace_par_late'] = line[217].strip()

    record['ent_trnr_jock_cmb_starts'] = line[218]
    record['ent_trnr_jock_cmb_wins'] = line[219]
    record['ent_trnr_jock_cmb_$2roi'] = line[222]

    record['ent_days_since_last_race'] = line[223] # DEBUG AGAINST CALC'D
    
    record['ent_state_bred_flag'] = line[238].strip().upper()
    
    record['ent_bris_pwr'] = line[250].strip()

    record['ent_trnr_curr_yr_starts'] = line[1146].strip()
    record['ent_trnr_curr_yr_wins'] = line[1147].strip()
    record['ent_trnr_curr_yr_plcs'] = line[1148].strip()
    record['ent_trnr_curr_yr_shws'] = line[1149].strip()
    record['ent_trnr_curr_yr_roi'] = line[1150].strip()
    record['ent_trnr_prev_yr_starts'] = line[1151].strip()
    record['ent_trnr_prev_yr_wins'] = line[1152].strip()
    record['ent_trnr_prev_yr_plcs'] = line[1153].strip()
    record['ent_trnr_prev_yr_shws'] = line[1154].strip()
    record['ent_trnr_prev_yr_roi'] = line[1155].strip()

    record['ent_jock_curr_yr_starts'] = line[1156].strip()
    record['ent_jock_curr_yr_wins'] = line[1157].strip()
    record['ent_jock_curr_yr_plcs'] = line[1158].strip()
    record['ent_jock_curr_yr_shws'] = line[1159].strip()
    record['ent_jock_curr_yr_roi'] = line[1160].strip()
    record['ent_jock_prev_yr_starts'] = line[1161].strip()
    record['ent_jock_prev_yr_wins'] = line[1162].strip()
    record['ent_jock_prev_yr_plcs'] = line[1163].strip()
    record['ent_jock_prev_yr_shws'] = line[1164].strip()
    record['ent_jock_prev_yr_roi'] = line[1165].strip()
    
    record['ent_$auction'] = line[1221].strip()
    record['ent_dped'] = re.sub("[^0-9]", "",line[1263].strip())
    record['ent_mped'] = re.sub("[^0-9]", "",line[1264].strip())
    record['ent_tped'] = re.sub("[^0-9]", "",line[1265].strip())
    record['ent_dstped']= re.sub("[^0-9]", "",line[1266].strip())
    
    record['ent_bris_spd_life'] = line[1327].strip()
    record['ent_bris_spd_year'] = line[1328].strip()
    record['ent_bris_spd_track'] = line[1330].strip()

    # Past performances
    record['npp'] = 0
    record['pp'] = []

    for i in range(0,prm.max_npp):

        pp = dict()
        
        pp['date'] = line[255+i].strip()

        # Check for valid PPs (must have a date)
        if(pp['date'] != ''):
            record['npp'] = record['npp'] + 1
        
        pp['track'] = line[275+i].strip().upper()
        pp['surfcnd'] = line[305+i].strip().upper()

        pp['dist'] = line[315+i].strip()
        pp['surf'] = line[325+i].strip()
        pp['nhrs'] = line[345+i].strip()
        pp['post'] = line[355+i].strip()
        pp['equip'] = line[365+i].strip().upper()
        pp['rx'] = line[385+i].strip().upper()
        pp['weight'] = line[505+i].strip().upper()
        pp['odds'] = line[515+i].strip()
        pp['rdetail'] = line[535+i].strip().upper()
        pp['claim_price'] = line[545+i].strip()
        pp['purse'] = line[545+i].strip()
        pp['fin_position'] = line[615+i].strip()
        pp['fin_beat_len'] = line[745+i].strip()
        
        pp['bris_pace_2f'] = line[765+i].strip()
        pp['bris_pace_4f'] = line[775+i].strip()
        pp['bris_pace_6f'] = line[785+i].strip()

        pp['bris_pace_late'] = line[815+i].strip()
        pp['bris_spd']  = line[845+i].strip()
        pp['bris_spd_par'] = line[1166+i].strip()
        pp['final_time'] = line[1035+i].strip()
        pp['clmcode'] = line[1045+i].strip().upper() # claimed
        pp['trnr'] = line[1055+i].strip().upper()
        pp['jock'] = line[1065+i].strip().upper()
        pp['rtype'] = line[1085+i].strip().upper()
        pp['code'] = line[1253+i].strip().upper() # x is off the turf
        pp['synth'] = line[1402+i].strip()

        record['pp'].append(pp)
        
    # Workouts
    record['nwrk'] = 0
    record['wrk'] = []
    
    for i in range(0,prm.max_nwrk):
    
        wrk = dict()
    
        wrk['date'] = line[101+i].strip()
    
        # Check for valid PPs (must have a date)
        if(wrk['date'] != ''):
            record['nwrk'] = record['nwrk'] + 1
    
        wrk['time'] = line[113+i].strip()  # may be negative if "bullit" workout
        wrk['track'] = line[125+i].strip().upper()
        wrk['dist'] = line[137+i].strip()  # may be negative if "approx" distance
        wrk['surfcnd'] = line[149+i].strip().upper()
        wrk['desc'] = line[161+i].strip()
        wrk['surf'] = line[173+i].strip().upper() # includes surface type (main/trn)
        wrk['nwrks'] = line[185+i].strip()
        wrk['rank'] = line[197+i].strip()
        
        record['wrk'].append(wrk)

    return(record)
