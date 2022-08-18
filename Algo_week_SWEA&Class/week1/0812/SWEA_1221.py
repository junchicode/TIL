import sys
sys.stdin = open("GNS_test_input.txt", "r")

planet = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
def count (list):
    count = 0
    for i in list:
        count += 1
    return count

def bubblesort (list, N):
    # 정렬의 끝에서부터 하나씩 줄여간다
    for i in range(N-1, 0, -1):
        # 0부터 지정된 i까지 범위를 갖는 리스트에서
        for j in range(0, i):
            # 만약 왼이 오보다 크면
            if list[j] > list[j+1]:
                # 바꿔준다
                list[j], list[j+1] = list[j+1],list[j]
    
    return list
    
T = int(input())
for tc in range(T):
    
    number, N = input().split()
    N = int(N)
    case = list(input().split())
    length_planet = count(planet)

    planet_dict = {}
    for i in range(0, length_planet):
        planet_dict[planet[i]] = i

    for i in range(N):
        case[i] = planet_dict[case[i]]
    sorted_case = bubblesort(case, N)
    swap_plan_dict ={}
    for k,v in planet_dict.items():
        swap_plan_dict[v] = k

    for i in range(N):
        sorted_case[i] = swap_plan_dict[case[i]]

    res = " ".join(sorted_case)
    print(f"{number} \n{res}")
        


    
        