def knows(a, b):  
    relationships = [  
        [False, True, True, True],  # Person 0  
        [False, False, True, True],  # Person 1  
        [False, False, False, True],  # Person 2  
        [False, False, False, False]  # Person 3  
    ]  
    return relationships[a][b]  

def find_celebrity(n):
    candidates = 0
    for i in range(1, n):
        if knows(candidates,i):
            candidates = i

    for j in range(n):
        if j != candidates and knows(candidates, j) and not knows(j,candidates):
            return -1
    return candidates
    

if __name__ == '__main__':
    n = 4
    ans = find_celebrity(n)
    print(ans)