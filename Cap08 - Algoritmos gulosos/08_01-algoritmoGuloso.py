#Criação de um conjunto com os estados (foi utilizado conjunto pois ele não aceita elementos duplicados)
estadosParaAbranger = set(["al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", 
                           "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md", 
                           "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", 
                           "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc", 
                           "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"])

#Criação da tabela hash de estações junto com o conjunto de estados que cada uma abrange
estacoes = {}
estacoes["k01"] = set(["id", "nv", "ut"])
estacoes["k02"] = set(["wa", "id", "mt"])
estacoes["k03"] = set(["or", "nv", "ca"])
estacoes["k04"] = set(["nv", "ut"])
estacoes["k05"] = set(["ca", "az"])
estacoes["k06"] = set(["tx", "ok", "nm"])
estacoes["k07"] = set(["fl", "ga", "al", "sc"])
estacoes["k08"] = set(["ny", "nj", "ct"])
estacoes["k09"] = set(["pa", "oh", "wv"])
estacoes["k10"] = set(["il", "in", "mi", "wi"])
estacoes["k11"] = set(["co", "wy", "mt"])
estacoes["k12"] = set(["nd", "sd", "ne"])
estacoes["k13"] = set(["mn", "ia", "mo"])
estacoes["k14"] = set(["la", "ms", "ar"])
estacoes["k15"] = set(["tn", "ky", "va"])
estacoes["k16"] = set(["nc", "sc", "ga"])
estacoes["k17"] = set(["me", "nh", "vt"])
estacoes["k18"] = set(["ma", "ri", "ct"])
estacoes["k19"] = set(["de", "md", "va"])
estacoes["k20"] = set(["az", "nm", "tx"])
estacoes["k21"] = set(["ca", "nv", "az"])
estacoes["k22"] = set(["wa", "or", "ca"])
estacoes["k23"] = set(["id", "mt", "wy"])
estacoes["k24"] = set(["ut", "co", "nm"])
estacoes["k25"] = set(["ks", "ok", "tx"])
estacoes["k26"] = set(["mi", "oh", "pa"])
estacoes["k27"] = set(["wi", "mn", "ia"])
estacoes["k28"] = set(["il", "mo", "ky"])
estacoes["k29"] = set(["tn", "al", "ms"])
estacoes["k30"] = set(["la", "tx"])
estacoes["k31"] = set(["fl", "ga"])
estacoes["k32"] = set(["sc", "nc"])
estacoes["k33"] = set(["va", "wv"])
estacoes["k34"] = set(["ny", "pa"])
estacoes["k35"] = set(["nj", "de"])
estacoes["k36"] = set(["ct", "ma"])
estacoes["k37"] = set(["vt", "nh"])
estacoes["k38"] = set(["me"])
estacoes["k39"] = set(["ak", "hi"])
estacoes["k40"] = set(["ak"])
estacoes["k41"] = set(["hi"])
estacoes["k42"] = set(["nd", "mn"])
estacoes["k43"] = set(["sd", "ne"])
estacoes["k44"] = set(["co", "ks"])
estacoes["k45"] = set(["wy", "ut"])
estacoes["k46"] = set(["id", "wa"])
estacoes["k47"] = set(["or", "ca"])
estacoes["k48"] = set(["nv", "az"])
estacoes["k49"] = set(["nm", "tx"])
estacoes["k50"] = set(["ok", "ks"])

#conjunto onde sera armazenado as estacoes escolhidas
estacoesFinal = set()

#Variavel para armazenar a melhor estação (a que cobre mais estados)
while estadosParaAbranger:
    melhorEstacao = None
    estadosCobertos = set()
    for estacao, estadosDaEstacao in estacoes.items():
        cobertos = estadosParaAbranger & estadosDaEstacao
        if len(cobertos) > len(estadosCobertos):
            melhorEstacao = estacao
            estadosCobertos = cobertos
    print(melhorEstacao + " foi escolhida nesta iteração")
    estacoesFinal.add(melhorEstacao)
    estadosParaAbranger -= estadosCobertos

print(estacoesFinal)

#Verifica se todos os estados foram cobertos
interseccao = set()
for estacao in estacoesFinal:
    interseccao = interseccao | estacoes[estacao]

print(len(interseccao))