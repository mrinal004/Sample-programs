def missing(arr,n):
    x1=arr[0]
    x2=1
    for i in range(1,n):
        x1=x1^arr[i]
    for i in range(2,n+2):
        x2=x2^i
    return x1^x2
if __name__=='__main__':
    arr=[1,2,4,6,3,7,8]
    n=len(arr)
    miss=missing(arr,n)
    print(miss)