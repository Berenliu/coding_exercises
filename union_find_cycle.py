def union_find_cycle(edges):
    parent = {}
    for e in edges:
        if e[0] in parent:
            if e[1] in parent:
                s0 = get_index(e[0], parent)
                s1 = get_index(e[1], parent)
                if s0==s1:
                    return True
            else:
                parent[e[1]] = e[0]
        else:
            if e[1] in parent:
                parent[e[0]] = e[1]
            else:
                parent[e[1]] = e[0]
                parent[e[0]] = -1
    return False

def get_index(e, parent):
    while parent[e]!=-1:
        e = parent[e]
    return e

def main():
    edges = [[0,1], [1,2], [4,5], [5,1]]
    if union_find_cycle(edges):
        print("there is a cycle")
    else:
        print("there is no cycle")

if __name__ == "__main__":
    main()


