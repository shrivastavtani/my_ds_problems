#pascal's triangle

def pascal( n):
    triangle= [[]]*n
    # for i in range(0,n):
        

    for i in range(0,n):
        triangle[i]=[0]*(i+1)
        triangle[i][0]=1
        triangle[i][-1]=1
        import pdb; pdb.set_trace()
        for k in range(1,i):
            
            triangle[i][k]=triangle[i-1][k-1]+triangle[i-1][k]

        print(triangle)
        # print(triangle[i][j])
    print(triangle)
    # for i in range(n):
    #     print("i is",i)
    #     for k in range(1,i):
    #         print("k is",k)


if __name__=='__main__':
    pascal(5)