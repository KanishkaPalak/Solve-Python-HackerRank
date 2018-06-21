if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    for i in range(0, n):
        for j in range(i+1, n):
            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    m=arr[n-1]
    while m==max(arr):
        arr.remove(max(arr))
    print(max(arr))
            
     
    
