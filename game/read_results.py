def AI_results():

    f = open("agent_results.txt", "r")
    data = f.read()
    words = data.split()
    print("RNG") 
    spy_win_count = 0
    spy_loss_count = 0
    for k in words:
        if k == 'SPY-WIN':
            spy_win_count += 1
        if k == 'SPY-LOSS':
            spy_loss_count += 1
    print('SPY WINS: ', spy_win_count)
    print('SPY LOSSES: ', spy_loss_count)

    res_win_count = 0
    res_loss_count = 0
    for k in words:
        if k == 'RES-WIN':
            res_win_count += 1
        if k == 'RES-LOSS':
            res_loss_count += 1
    print('RES WINS: ', res_win_count*3)
    print('RES LOSSES: ', res_loss_count*3)

    print('WINS: ', (res_win_count + spy_win_count))
    print('LOSSES: ', (res_loss_count + spy_loss_count))
    f.close()



    f = open("agent_results1.txt", "r")
    data = f.read()
    words = data.split()
    print("AI 1") 
    spy_win_count = 0
    spy_loss_count = 0
    for k in words:
        if k == 'SPY-WIN':
            spy_win_count += 1
        if k == 'SPY-LOSS':
            spy_loss_count += 1
    print('SPY WINS: ', spy_win_count)
    print('SPY LOSSES: ', spy_loss_count)

    res_win_count = 0
    res_loss_count = 0
    for k in words:
        if k == 'RES-WIN':
            res_win_count += 1
        if k == 'RES-LOSS':
            res_loss_count += 1
    print('RES WINS: ', res_win_count)
    print('RES LOSSES: ', res_loss_count)

    print('WINS: ', res_win_count + spy_win_count)
    print('LOSSES: ', res_loss_count + spy_loss_count)
    f.close()


    f = open("agent_results2.txt", "r")
    data = f.read()
    words = data.split()
    print("AI 2") 
    spy_win_count = 0
    spy_loss_count = 0
    for k in words:
        if k == 'SPY-WIN':
            spy_win_count += 1
        if k == 'SPY-LOSS':
            spy_loss_count += 1
    print('SPY WINS: ', spy_win_count)
    print('SPY LOSSES: ', spy_loss_count)

    res_win_count = 0
    res_loss_count = 0
    for k in words:
        if k == 'RES-WIN':
            res_win_count += 1
        if k == 'RES-LOSS':
            res_loss_count += 1
    print('RES WINS: ', res_win_count)
    print('RES LOSSES: ', res_loss_count)

    print('WINS: ', res_win_count + spy_win_count)
    print('LOSSES: ', res_loss_count + spy_loss_count)
    f.close()



AI_results()