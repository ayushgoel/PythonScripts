# https://www.hackerrank.com/challenges/bfsshortreach

q = int(raw_input())

for t1 in xrange(q):
    n, m = [int(i) for i in raw_input().split()]

    al = [set() for i in xrange(n+1)]
    for x in xrange(m):
        u, v = [int(i) for i in raw_input().split()]
        al[u].add(v)
        al[v].add(u)
    s = int(raw_input())

    distances = [-1 for i in xrange(n+1)]
    nodes_to_consider = [(s, 0)]
    # cur_distance = 6
    nodes_considered = set()

    while len(nodes_to_consider) != 0:
        cur_node = nodes_to_consider.pop(0)
        if cur_node[0] in nodes_considered:
            continue
        nodes_considered.add(cur_node[0])
        cur_dis = cur_node[1] + 6
        for e in al[cur_node[0]]:
            if distances[e] == -1 or distances[e] > cur_dis:
                distances[e] = cur_dis
            nodes_to_consider += [(e, cur_dis)]
    del distances[s]
    del distances[0]
    print " ".join([str(i) for i in distances])
