def result_line_parse(prm,line):

    res = dict()
    res['track'] = line[0].strip().upper()
    res['date'] = line[1].strip()
    res['race_num'] = int(line[2].strip())
    res['name'] = line[4].strip().upper()
    res['post'] = int(line[7].strip())
    res['ptodds'] = float(line[30].strip())
    res['finish'] = int(line[59].strip())
    res['btn_lengths'] = float(line[72].strip()) # Winner = 0.0

    tmp = line[50]
    if(tmp != ''):
        res['win_pay'] = float(tmp.strip())
    else:
        res['win_pay'] = 0.0

    tmp = line[51]
    if(tmp != ''):
        res['plc_pay'] = float(tmp.strip())
    else:
        res['plc_pay'] = 0.0

    tmp = line[52]
    if(tmp != ''):
        res['shw_pay'] = float(tmp.strip())
    else:
        res['shw_pay'] = 0.0

    return(res)
