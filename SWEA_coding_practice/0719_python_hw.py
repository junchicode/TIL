orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orderlist = []
orderlist = orders.split(",") #스플릿 쓰면 리스트로 반환되는듯, 굳이 제거까지 해서 처리했다,,,

q_1 = len(orderlist)
q_2 = sorted(set(orderlist), reverse=True)
# 1번 답
print(q_1)
# 2번 답
print(q_2)

reslist = []
for i in q_2:
    if '아이스' in i:
        new = i.replace("아이스", "")
        reslist.append(new)
    else:
        reslist.append(i)
# 2번 아이스 제거 답
print(sorted(set(reslist), reverse = True))
        


        

    
