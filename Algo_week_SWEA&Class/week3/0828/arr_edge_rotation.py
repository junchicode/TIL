def edge_turn(x1,y1,x2,y2):
    for x1,y1,x2,y2 in queries:
        tmp = arr[x1-1][y1-1]

        for k in range(x1-1,x2-1): #왼쪽 세로
            test = arr[k+1][y1-1]
            arr[k][y1-1] = test

        for k in range(y1-1,y2-1): # 하단 가로
            test = arr[x2-1][k+1]
            arr[x2-1][k] = test
            

        for k in range(x2-1,x1-1,-1): # 왼쪽 세로
            test = arr[k-1][y2-1]
            arr[k][y2-1] = test
            

        for k in range(y2-1,y1-1,-1): # 상단 가로
            test = arr[x1-1][k-1]
            arr[x1-1][k] = test

        arr[x1-1][y1] = tmp

queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

arr =[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]