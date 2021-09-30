def bottleneck_diagram_dist(diag1, diag2, order):
    dg1 = [y for (x, y) in diag1 if x == order]
    dg2 = [y for (x, y) in diag2 if x == order]

    return gd.bottleneck_distance(dg1, dg2)


def diagram_threshold (diag,threshold ):
    return [(x,y) for (x,y) in diag if abs(y[1] - y[0])> threshold]
# scoring


def ps_scoring(diag):
    try:
        return max([x[1][1] - x[1][0] if x[0] == 1 else 0 for x in diag])
    except:
        return 0

def qps_scoring(diag):
    try:
        Q2_max = max([x[1][1] - x[1][0] if x[0] == 2 else 0 for x in diag])
        Ps_max = max([x[1][1] - x[1][0] if x[0] == 1 else 0 for x in diag])
        Ps_second_max = max([x[1][1] - x[1][0] if x[0] == 1 and x[1][1] - x[1][0] != Ps_max else 0 for x in diag])
        return math.sqrt(Q2_max * Ps_second_max / 3)
    except:
        return 0
    
def two_2ndHomology_score(diag):
    Q2_max = max([x[1][1] - x[1][0] if x[0] == 2 else 0 for x in diag])
    Q2_second_max = max([x[1][1] - x[1][0] if x[0] == 2 and x[1][1] - x[1][0] != Q2_max else 0 for x in diag])
    return Q2_second_max * Q2_max


def get_features(diag):
    features_array = []


    first_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 1]
    second_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 2]
    third_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 3]
    forth_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 4]
    
    first_lifespan = [c-b for (a,(b,c)) in first_list]+[0]
    second_lifespan = [c-b for (a,(b,c)) in second_list]+[0]
    third_lifespan = [c-b for (a,(b,c)) in third_list]+[0]
    forth_lifespan = [c-b for (a,(b,c)) in forth_list]+[0]
    first_lifespan_sorted = sorted(first_lifespan)
    second_lifespan_sorted = sorted(second_lifespan)
    third_lifespan_sorted = sorted(third_lifespan)
    forth_lifespan_sorted = sorted(forth_lifespan)
    borntime_first_sorted = sorted([(b,c-b) for (a,(b,c)) in first_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    borntime_second_sorted = sorted([(b,c-b) for (a,(b,c)) in second_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    borntime_third_sorted = sorted([(b,c-b) for (a,(b,c)) in third_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    borntime_forth_sorted = sorted([(b,c-b) for (a,(b,c)) in forth_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_first_sorted = sorted([(c,c-b) for (a,(b,c)) in first_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_second_sorted = sorted([(c,c-b) for (a,(b,c)) in second_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_third_sorted = sorted([(c,c-b) for (a,(b,c)) in third_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_forth_sorted = sorted([(c,c-b) for (a,(b,c)) in forth_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]


    # --------------------------------- now features ---------------------------------------------
    number_of_first_above_0_0005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.0005])
    features_array.append(number_of_first_above_0_0005)
    number_of_second_above_0_0005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.0005])
    features_array.append(number_of_second_above_0_0005)
    number_of_first_above_0_001 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.001])
    features_array.append(number_of_first_above_0_001)
    number_of_second_above_0_001 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.001])
    features_array.append(number_of_second_above_0_001)
    number_of_first_above_0_003 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.003])
    features_array.append(number_of_first_above_0_003)
    number_of_second_above_0_003 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.003])
    features_array.append(number_of_second_above_0_003)
    number_of_first_above_0_005 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.005])
    features_array.append(number_of_first_above_0_005)
    number_of_second_above_0_005 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.005])
    features_array.append(number_of_second_above_0_005)
    number_of_first_above_0_007 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.007])
    features_array.append(number_of_first_above_0_007)
    number_of_second_above_0_007 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.007])
    features_array.append(number_of_second_above_0_007)
    ratio_second_first_above_0_0005 = number_of_first_above_0_0005/(1+number_of_second_above_0_0005)
    features_array.append(ratio_second_first_above_0_0005)
    ratio_second_first_above_0_001 = number_of_first_above_0_001/(1+number_of_second_above_0_001)
    features_array.append(ratio_second_first_above_0_001)
    ratio_second_first_above_0_003 = number_of_first_above_0_003/(1+number_of_second_above_0_003)
    features_array.append(ratio_second_first_above_0_003)
    ratio_second_first_above_0_005 = number_of_first_above_0_005/(1+number_of_second_above_0_005)
    features_array.append(ratio_second_first_above_0_005)
    ratio_second_first_above_0_007 = number_of_first_above_0_007/(1+number_of_second_above_0_007)
    features_array.append(ratio_second_first_above_0_007)

    if len(first_lifespan) < 1:
        max_1_first = sum(first_lifespan_sorted)
    else:
        max_1_first = first_lifespan_sorted[-1]

    if len(first_lifespan) < 2:
        max_2_first = sum(first_lifespan_sorted)
    else:
        max_2_first = max_1_first + first_lifespan_sorted[-2]

    if len(first_lifespan) < 4:
        max_3_first = sum(first_lifespan_sorted)
    else:
        max_3_first = max_2_first + first_lifespan_sorted[-3]

    if len(first_lifespan) < 4:
        max_4_first = sum(first_lifespan_sorted)
    else:
        max_4_first = max_3_first + first_lifespan_sorted[-4]

    if len(first_lifespan) < 5:
        max_5_first = sum(first_lifespan_sorted)
    else:
        max_5_first = max_4_first + first_lifespan_sorted[-5]

    if len(first_lifespan) < 6:
        max_6_first = sum(first_lifespan_sorted)
    else:
        max_6_first = max_5_first + first_lifespan_sorted[-6]

    features_array.append(max_1_first)
    features_array.append(max_2_first)
    features_array.append(max_3_first)
    features_array.append(max_4_first)
    features_array.append(max_5_first)
    features_array.append(max_6_first)

    #21

    if len(second_lifespan) < 1:
        max_1_second = sum(second_lifespan_sorted)
    else:
        max_1_second = second_lifespan_sorted[-1]

    if len(second_lifespan) < 2:
        max_2_second = sum(second_lifespan_sorted)
    else:
        max_2_second = max_1_second + second_lifespan_sorted[-2]

    if len(second_lifespan) < 4:
        max_3_second = sum(second_lifespan_sorted)
    else:
        max_3_second = max_2_second + second_lifespan_sorted[-3]

    if len(second_lifespan) < 4:
        max_4_second = sum(second_lifespan_sorted)
    else:
        max_4_second = max_3_second + second_lifespan_sorted[-4]

    if len(second_lifespan) < 5:
        max_5_second = sum(second_lifespan_sorted)
    else:
        max_5_second = max_4_second + second_lifespan_sorted[-5]

    if len(second_lifespan) < 6:
        max_6_second = sum(second_lifespan_sorted)
    else:
        max_6_second = max_5_second + second_lifespan_sorted[-6]

    features_array.append(max_1_second)
    features_array.append(max_2_second)
    features_array.append(max_3_second)
    features_array.append(max_4_second)
    features_array.append(max_5_second)
    features_array.append(max_6_second)

    mult_max_two_first = max_1_first * (max_2_first-max_1_first)
    features_array.append(mult_max_two_first)
    mult_max_two_second = max_1_second * (max_2_second-max_1_second)
    features_array.append(mult_max_two_second)
    mult_max_three_first = mult_max_two_first*(max_3_first - max_2_first)
    features_array.append(mult_max_three_first)
    mult_max_three_second = mult_max_two_second*(max_3_second-max_2_second)
    features_array.append(mult_max_three_second)
    mult_max_four_first =  mult_max_three_first* (max_4_first-max_3_first)
    features_array.append(mult_max_four_first)
    mult_max_four_second = mult_max_three_second* (max_4_second-max_3_second)
    features_array.append(mult_max_four_second)
    qps = qps_scoring(diag)
    features_array.append(qps)
    ps = ps_scoring(diag)
    features_array.append(ps)
    #35
    # borntime_first




    borntime_max_second = borntime_second_sorted[0][0]
    borntime_max_first =borntime_first_sorted[0][0]
    borntime_max2_second =borntime_second_sorted[1][0]
    borntime_max2_first =borntime_first_sorted[1][0]
    borntime_max3_second =borntime_second_sorted[2][0]
    borntime_max3_first =borntime_first_sorted[2][0]
    borntime_max4_second =borntime_second_sorted[3][0]
    borntime_max4_first =borntime_first_sorted[3][0]
    borntime_max5_second =borntime_second_sorted[4][0]
    borntime_max5_first =borntime_first_sorted[4][0]
    borntime_max6_second =borntime_second_sorted[5][0]
    borntime_max6_first =borntime_first_sorted[5][0]

    features_array.append(borntime_max_first)
    features_array.append(borntime_max2_first)
    features_array.append(borntime_max3_first)
    features_array.append(borntime_max4_first)
    features_array.append(borntime_max5_first)
    features_array.append(borntime_max6_first)

    features_array.append(borntime_max_second)
    features_array.append(borntime_max2_second)
    features_array.append(borntime_max3_second)
    features_array.append(borntime_max4_second)
    features_array.append(borntime_max5_second)
    features_array.append(borntime_max6_second)

    deathtime_max_second =deathtime_second_sorted[0][0]
    deathtime_max_first =deathtime_first_sorted[0][0]
    deathtime_max2_second =deathtime_second_sorted[1][0]
    deathtime_max2_first =deathtime_first_sorted[1][0]
    deathtime_max3_second =deathtime_second_sorted[2][0]
    deathtime_max3_first =deathtime_first_sorted[2][0]
    deathtime_max4_second =deathtime_second_sorted[3][0]
    deathtime_max4_first =deathtime_first_sorted[3][0]
    deathtime_max5_second =deathtime_second_sorted[4][0]
    deathtime_max5_first =deathtime_first_sorted[4][0]
    deathtime_max6_second =deathtime_second_sorted[5][0]
    deathtime_max6_first =deathtime_first_sorted[4][0]

    features_array.append(deathtime_max_first)
    features_array.append(deathtime_max2_first)
    features_array.append(deathtime_max3_first)
    features_array.append(deathtime_max4_first)
    features_array.append(deathtime_max5_first)
    features_array.append(deathtime_max6_first)

    features_array.append(deathtime_max_second)
    features_array.append(deathtime_max2_second)
    features_array.append(deathtime_max3_second)
    features_array.append(deathtime_max4_second)
    features_array.append(deathtime_max5_second)
    features_array.append(deathtime_max6_second)
    #59
    standard_deviation_2second =np.std(second_lifespan_sorted[-2:])
    standard_deviation_2first = np.std(first_lifespan_sorted[-2:])
    standard_deviation_3second = np.std(second_lifespan_sorted[-3:])
    standard_deviation_3first = np.std(first_lifespan_sorted[-3:])
    standard_deviation_4second =np.std(second_lifespan_sorted[-4:])
    standard_deviation_4first = np.std(first_lifespan_sorted[-4:])
    standard_deviation_5second =np.std(second_lifespan_sorted[-5:])
    standard_deviation_5first = np.std(first_lifespan_sorted[-5:])
    standard_deviation_6second =np.std(second_lifespan_sorted[-6:])
    standard_deviation_6first = np.std(first_lifespan_sorted[-6:])

    features_array.append(standard_deviation_2first)
    features_array.append(standard_deviation_3first)
    features_array.append(standard_deviation_4first)
    features_array.append(standard_deviation_5first)
    features_array.append(standard_deviation_6first)

    features_array.append(standard_deviation_2second)
    features_array.append(standard_deviation_3second)
    features_array.append(standard_deviation_4second)
    features_array.append(standard_deviation_5second)
    features_array.append(standard_deviation_6second)

    max_first_lifespan = first_lifespan_sorted[-1]

    max_second_lifespan = second_lifespan_sorted[-1]
    max_div_median_first = max_first_lifespan/(statistics.median(first_lifespan_sorted)+1)
    features_array.append(max_div_median_first)
    max_div_median_second = max_second_lifespan/(statistics.median(second_lifespan_sorted)+1)

    features_array.append(max_div_median_second)
    max_div_mean_first = max_first_lifespan/(statistics.mean(first_lifespan_sorted)+1)
    features_array.append(max_div_mean_first)

    max_div_mean_second = max_second_lifespan/(statistics.mean(second_lifespan_sorted)+1)
    features_array.append(max_div_mean_second)


    first_standard_dev_lifespan = np.std(first_lifespan_sorted)
    second_standard_dev_lifespan =np.std(second_lifespan_sorted)
    first_standard_dev_borntime = np.std(borntime_first_sorted)
    second_standard_dev_borntime =np.std(borntime_second_sorted)
    first_standard_dev_deathtime =np.std(deathtime_first_sorted)
    second_standard_dev_deathtime =np.std(deathtime_second_sorted)

    features_array.append(first_standard_dev_lifespan)
    features_array.append(second_standard_dev_lifespan)
    features_array.append(first_standard_dev_borntime)
    features_array.append(second_standard_dev_borntime)
    features_array.append(first_standard_dev_deathtime)
    features_array.append(second_standard_dev_deathtime)



    # new features
    try:
        features_array.append(second_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-4])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-5])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-6])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-7])
    except Exception:
        features_array.append(0)


    try:
        features_array.append(first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-4])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-5])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-6])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-7])
    except Exception:
        features_array.append(0)

    # now multiplication
    try:
        features_array.append(second_lifespan_sorted[-3]*second_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-4]*second_lifespan_sorted[-3]*second_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-5]*second_lifespan_sorted[-4]*second_lifespan_sorted[-3]*second_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-6]*second_lifespan_sorted[-5]*second_lifespan_sorted[-4]*second_lifespan_sorted[-3]*second_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(second_lifespan_sorted[-7]*second_lifespan_sorted[-6]*second_lifespan_sorted[-5]*second_lifespan_sorted[-4]*second_lifespan_sorted[-3]*second_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)

    try:
        features_array.append(first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-4]*first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-5]*first_lifespan_sorted[-4]*first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-6]*first_lifespan_sorted[-5]*first_lifespan_sorted[-4]*first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(first_lifespan_sorted[-7]*first_lifespan_sorted[-6]*first_lifespan_sorted[-5]*first_lifespan_sorted[-4]*first_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)


    return features_array
