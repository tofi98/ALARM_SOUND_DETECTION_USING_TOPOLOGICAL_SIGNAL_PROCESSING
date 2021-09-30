def get_features(diag):

    features_array = []
    blue_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 1]
    green_list = [(a,(b,c)) for (a,(b,c)) in diag if a == 2]
    blue_lifespan = [c-b for (a,(b,c)) in blue_list]+[0]
    green_lifespan = [c-b for (a,(b,c)) in green_list]+[0]
    blue_lifespan_sorted = sorted(blue_lifespan)
    green_lifespan_sorted = sorted(green_lifespan)
    borntime_blue_sorted = sorted([(b,c-b) for (a,(b,c)) in blue_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    borntime_green_sorted = sorted([(b,c-b) for (a,(b,c)) in green_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_blue_sorted = sorted([(c,c-b) for (a,(b,c)) in blue_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    deathtime_green_sorted = sorted([(c,c-b) for (a,(b,c)) in green_list],key=lambda a:a[1])+[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]


    # --------------------------------- now features ---------------------------------------------
    number_of_blue_above_0_0005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.0005])
    features_array.append(number_of_blue_above_0_0005)
    number_of_green_above_0_0005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.0005])
    features_array.append(number_of_green_above_0_0005)
    number_of_blue_above_0_001 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.001])
    features_array.append(number_of_blue_above_0_001)
    number_of_green_above_0_001 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.001])
    features_array.append(number_of_green_above_0_001)
    number_of_blue_above_0_003 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.003])
    features_array.append(number_of_blue_above_0_003)
    number_of_green_above_0_003 =len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.003])
    features_array.append(number_of_green_above_0_003)
    number_of_blue_above_0_005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.005])
    features_array.append(number_of_blue_above_0_005)
    number_of_green_above_0_005 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.005])
    features_array.append(number_of_green_above_0_005)
    number_of_blue_above_0_007 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 1 and c-b>0.007])
    features_array.append(number_of_blue_above_0_007)
    number_of_green_above_0_007 = len([(a,(b,c)) for (a,(b,c)) in diag if a == 2 and c-b>0.007])
    features_array.append(number_of_green_above_0_007)
    ratio_green_blue_above_0_0005 = number_of_blue_above_0_0005/(1+number_of_green_above_0_0005)
    features_array.append(ratio_green_blue_above_0_0005)
    ratio_green_blue_above_0_001 = number_of_blue_above_0_001/(1+number_of_green_above_0_001)
    features_array.append(ratio_green_blue_above_0_001)
    ratio_green_blue_above_0_003 = number_of_blue_above_0_003/(1+number_of_green_above_0_003)
    features_array.append(ratio_green_blue_above_0_003)
    ratio_green_blue_above_0_005 = number_of_blue_above_0_005/(1+number_of_green_above_0_005)
    features_array.append(ratio_green_blue_above_0_005)
    ratio_green_blue_above_0_007 = number_of_blue_above_0_007/(1+number_of_green_above_0_007)
    features_array.append(ratio_green_blue_above_0_007)

    if len(blue_lifespan) < 1:
        max_1_blue = sum(blue_lifespan_sorted)
    else:
        max_1_blue = blue_lifespan_sorted[-1]

    if len(blue_lifespan) < 2:
        max_2_blue = sum(blue_lifespan_sorted)
    else:
        max_2_blue = max_1_blue + blue_lifespan_sorted[-2]

    if len(blue_lifespan) < 4:
        max_3_blue = sum(blue_lifespan_sorted)
    else:
        max_3_blue = max_2_blue + blue_lifespan_sorted[-3]

    if len(blue_lifespan) < 4:
        max_4_blue = sum(blue_lifespan_sorted)
    else:
        max_4_blue = max_3_blue + blue_lifespan_sorted[-4]

    if len(blue_lifespan) < 5:
        max_5_blue = sum(blue_lifespan_sorted)
    else:
        max_5_blue = max_4_blue + blue_lifespan_sorted[-5]

    if len(blue_lifespan) < 6:
        max_6_blue = sum(blue_lifespan_sorted)
    else:
        max_6_blue = max_5_blue + blue_lifespan_sorted[-6]

    features_array.append(max_1_blue)
    features_array.append(max_2_blue)
    features_array.append(max_3_blue)
    features_array.append(max_4_blue)
    features_array.append(max_5_blue)
    features_array.append(max_6_blue)

    #21

    if len(green_lifespan) < 1:
        max_1_green = sum(green_lifespan_sorted)
    else:
        max_1_green = green_lifespan_sorted[-1]

    if len(green_lifespan) < 2:
        max_2_green = sum(green_lifespan_sorted)
    else:
        max_2_green = max_1_green + green_lifespan_sorted[-2]

    if len(green_lifespan) < 4:
        max_3_green = sum(green_lifespan_sorted)
    else:
        max_3_green = max_2_green + green_lifespan_sorted[-3]

    if len(green_lifespan) < 4:
        max_4_green = sum(green_lifespan_sorted)
    else:
        max_4_green = max_3_green + green_lifespan_sorted[-4]

    if len(green_lifespan) < 5:
        max_5_green = sum(green_lifespan_sorted)
    else:
        max_5_green = max_4_green + green_lifespan_sorted[-5]

    if len(green_lifespan) < 6:
        max_6_green = sum(green_lifespan_sorted)
    else:
        max_6_green = max_5_green + green_lifespan_sorted[-6]

    features_array.append(max_1_green)
    features_array.append(max_2_green)
    features_array.append(max_3_green)
    features_array.append(max_4_green)
    features_array.append(max_5_green)
    features_array.append(max_6_green)

    mult_max_two_blue = max_1_blue * (max_2_blue-max_1_blue)
    features_array.append(mult_max_two_blue)
    mult_max_two_green = max_1_green * (max_2_green-max_1_green)
    features_array.append(mult_max_two_green)
    mult_max_three_blue = mult_max_two_blue*(max_3_blue - max_2_blue)
    features_array.append(mult_max_three_blue)
    mult_max_three_green = mult_max_two_green*(max_3_green-max_2_green)
    features_array.append(mult_max_three_green)
    mult_max_four_blue = mult_max_three_blue* (max_4_blue-max_3_blue)
    features_array.append(mult_max_four_blue)
    mult_max_four_green = mult_max_three_green* (max_4_green-max_3_green)
    features_array.append(mult_max_four_green)
    qps = qps_scoring(diag)
    features_array.append(qps)
    ps = ps_scoring(diag)
    features_array.append(ps)
    #35
    # borntime_blue

    borntime_max_green = borntime_green_sorted[0][0]
    borntime_max_blue = borntime_blue_sorted[0][0]
    borntime_max2_green = borntime_green_sorted[1][0]
    borntime_max2_blue = borntime_blue_sorted[1][0]
    borntime_max3_green = borntime_green_sorted[2][0]
    borntime_max3_blue = borntime_blue_sorted[2][0]
    borntime_max4_green = borntime_green_sorted[3][0]
    borntime_max4_blue = borntime_blue_sorted[3][0]
    borntime_max5_green = borntime_green_sorted[4][0]
    borntime_max5_blue = borntime_blue_sorted[4][0]
    borntime_max6_green = borntime_green_sorted[5][0]
    borntime_max6_blue = borntime_blue_sorted[5][0]

    features_array.append(borntime_max_blue)
    features_array.append(borntime_max2_blue)
    features_array.append(borntime_max3_blue)
    features_array.append(borntime_max4_blue)
    features_array.append(borntime_max5_blue)
    features_array.append(borntime_max6_blue)

    features_array.append(borntime_max_green)
    features_array.append(borntime_max2_green)
    features_array.append(borntime_max3_green)
    features_array.append(borntime_max4_green)
    features_array.append(borntime_max5_green)
    features_array.append(borntime_max6_green)

    deathtime_max_green = deathtime_green_sorted[0][0]
    deathtime_max_blue = deathtime_blue_sorted[0][0]
    deathtime_max2_green = deathtime_green_sorted[1][0]
    deathtime_max2_blue = deathtime_blue_sorted[1][0]
    deathtime_max3_green = deathtime_green_sorted[2][0]
    deathtime_max3_blue = deathtime_blue_sorted[2][0]
    deathtime_max4_green = deathtime_green_sorted[3][0]
    deathtime_max4_blue = deathtime_blue_sorted[3][0]
    deathtime_max5_green = deathtime_green_sorted[4][0]
    deathtime_max5_blue = deathtime_blue_sorted[4][0]
    deathtime_max6_green = deathtime_green_sorted[5][0]
    deathtime_max6_blue = deathtime_blue_sorted[4][0]

    features_array.append(deathtime_max_blue)
    features_array.append(deathtime_max2_blue)
    features_array.append(deathtime_max3_blue)
    features_array.append(deathtime_max4_blue)
    features_array.append(deathtime_max5_blue)
    features_array.append(deathtime_max6_blue)

    features_array.append(deathtime_max_green)
    features_array.append(deathtime_max2_green)
    features_array.append(deathtime_max3_green)
    features_array.append(deathtime_max4_green)
    features_array.append(deathtime_max5_green)
    features_array.append(deathtime_max6_green)
    #59
    standard_deviation_2green =np.std(green_lifespan_sorted[-2:])
    standard_deviation_2blue = np.std(blue_lifespan_sorted[-2:])
    standard_deviation_3green = np.std(green_lifespan_sorted[-3:])
    standard_deviation_3blue = np.std(blue_lifespan_sorted[-3:])
    standard_deviation_4green =np.std(green_lifespan_sorted[-4:])
    standard_deviation_4blue = np.std(blue_lifespan_sorted[-4:])
    standard_deviation_5green =np.std(green_lifespan_sorted[-5:])
    standard_deviation_5blue = np.std(blue_lifespan_sorted[-5:])
    standard_deviation_6green =np.std(green_lifespan_sorted[-6:])
    standard_deviation_6blue = np.std(blue_lifespan_sorted[-6:])

    features_array.append(standard_deviation_2blue)
    features_array.append(standard_deviation_3blue)
    features_array.append(standard_deviation_4blue)
    features_array.append(standard_deviation_5blue)
    features_array.append(standard_deviation_6blue)

    features_array.append(standard_deviation_2green)
    features_array.append(standard_deviation_3green)
    features_array.append(standard_deviation_4green)
    features_array.append(standard_deviation_5green)
    features_array.append(standard_deviation_6green)

    max_blue_lifespan = blue_lifespan_sorted[-1]

    max_green_lifespan = green_lifespan_sorted[-1]
    max_div_median_blue = max_blue_lifespan/(statistics.median(blue_lifespan_sorted)+1)
    features_array.append(max_div_median_blue)
    max_div_median_green = max_green_lifespan/(statistics.median(green_lifespan_sorted)+1)

    features_array.append(max_div_median_green)
    max_div_mean_blue = max_blue_lifespan/(statistics.mean(blue_lifespan_sorted)+1)
    features_array.append(max_div_mean_blue)

    max_div_mean_green = max_green_lifespan/(statistics.mean(green_lifespan_sorted)+1)
    features_array.append(max_div_mean_green)


    blue_standard_dev_lifespan = np.std(blue_lifespan_sorted)
    green_standard_dev_lifespan =np.std(green_lifespan_sorted)
    blue_standard_dev_borntime = np.std(borntime_blue_sorted)
    green_standard_dev_borntime =np.std(borntime_green_sorted)
    blue_standard_dev_deathtime =np.std(deathtime_blue_sorted)
    green_standard_dev_deathtime =np.std(deathtime_green_sorted)

    features_array.append(blue_standard_dev_lifespan)
    features_array.append(green_standard_dev_lifespan)
    features_array.append(blue_standard_dev_borntime)
    features_array.append(green_standard_dev_borntime)
    features_array.append(blue_standard_dev_deathtime)
    features_array.append(green_standard_dev_deathtime)



    # new features
    try:
        features_array.append(green_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-4])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-5])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-6])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-7])
    except Exception:
        features_array.append(0)


    try:
        features_array.append(blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-4])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-5])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-6])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-7])
    except Exception:
        features_array.append(0)

    # now multiplication
    try:
        features_array.append(green_lifespan_sorted[-3]*green_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-4]*green_lifespan_sorted[-3]*green_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-5]*green_lifespan_sorted[-4]*green_lifespan_sorted[-3]*green_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-6]*green_lifespan_sorted[-5]*green_lifespan_sorted[-4]*green_lifespan_sorted[-3]*green_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(green_lifespan_sorted[-7]*green_lifespan_sorted[-6]*green_lifespan_sorted[-5]*green_lifespan_sorted[-4]*green_lifespan_sorted[-3]*green_lifespan_sorted[-2])
    except Exception:
        features_array.append(0)

    try:
        features_array.append(blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-4]*blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-5]*blue_lifespan_sorted[-4]*blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-6]*blue_lifespan_sorted[-5]*blue_lifespan_sorted[-4]*blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)
    try:
        features_array.append(blue_lifespan_sorted[-7]*blue_lifespan_sorted[-6]*blue_lifespan_sorted[-5]*blue_lifespan_sorted[-4]*blue_lifespan_sorted[-3])
    except Exception:
        features_array.append(0)


    return features_array
