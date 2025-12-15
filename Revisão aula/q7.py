def acurancia(vv: list, vp: list) -> float:
    if len(vv) != len(vp):
        print('ERRO')
    l = len(vv)
    num_previsoes_corr = 0
    num_total_prev = 0
    for i in range(l):
        ref = vv[i]
        prev = prev[i]
        if prev == ref:
            num_previsoes_corr += 1
        num_total_prev += 1
    return num_previsoes_corr / num_total_prev

def acurancia_2(vv: list, vp: list) -> float:
    if len(vv) != len(vp):
        print('ERRO')
    l = len(vv)
    num_previsoes_corr = 0
    num_total_prev = 0
    for ref, prev in zip(vv, vp):
        if prev == ref:
            num_previsoes_corr += 1
        num_total_prev += 1
    return num_previsoes_corr / num_total_prev


        
