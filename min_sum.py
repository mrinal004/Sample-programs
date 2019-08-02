def minSum(arr,size):
    if size<2:
        return -1
    low=0
    high=1
    min_sum=arr[0]+arr[1]
    for i in range(0,size-1):
        for j in range(i+1,size):
            sum=arr[i]+arr[j]
            if abs(min_sum)>abs(sum):
                min_sum=sum
                low=i
                high=j
    print(arr[low],arr[high])

arr=[1,60,-10,70,-80,85]
minSum(arr,len(arr))
