def CompletePack_恰好装满方案总数( V, weight):
    F = [0] * (V + 1)
    F[0] = 1
    for i in range(0, len(weight)):
        for v in range(weight[i], V + 1):

                F[v] = F[v] + F[v - weight[i]]
    return F[V]
V = 12553
weight = [1,2,3]
print(CompletePack_恰好装满方案总数(V, weight))