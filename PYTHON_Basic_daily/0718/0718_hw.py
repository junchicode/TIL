score = {
'algorithm' : 90,
'python': 85,
'django': 89,
'web': 83
}
count = 0
sc = 0
for i in score:
    sc += score.get(i)
    count += 1
    
res =  sc/count

print(res)