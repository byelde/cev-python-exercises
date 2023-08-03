def notas(*num, sit=False):
    dic = {}
    dic["total"] = len(num)
    dic["maior"] = max(num)
    dic["menor"] = min(num)
    dic["média"] = sum(num)/len(num)

    if sit:
        if dic["média"] < 6:
            situacao = "RUIM"
        elif 6 <= dic["média"] <= 8:
            situacao = "BOA"
        else:
            situacao = "ÓTIMA"
        dic["situação"] = situacao
    return dic


resp = notas(5, 5, 5, sit = True)
print(resp)