def left_bs(arr, st, end, n):
    """find the left most index the n could insert into arr"""
    if arr[st]>=n:
        return st-1
    if arr[end]<n:
        return end+1 
    mid = st + (end-st)//2
    while st <= end:
        if arr[mid] < n and arr[mid+1] >= n:
            return mid + 1
        if arr[mid] < n:
            st = mid
        else:
            end = mid-1
        mid = st + (end-st)//2

def right_bs(arr, st, end, n):
    """find the right most index the n could insert into arr"""
    if arr[st]>n:
        return st-1
    if arr[end]<n:
        return end+1 
    mid = st + (end-st)//2
    while st <= end:
        if arr[mid] <= n and arr[mid+1] > n:
            return mid + 1
        if arr[mid] <= n:
            st = mid + 1
        else:
            end = mid
        mid = st + (end-st)//2

def normal_bs(arr, n):
    """find the index of n in arr, if n is not in arr, return -1"""
    st = 0
    end = len(arr)-1
    found = False
    while not found and st <= end:
        mid = st + (end-st)//2
        if arr[mid] == n:
            found = True
            break
        elif arr[mid] < n:
            st = mid + 1
        else:
            end = mid -1
    if found:
        return mid
    else:
        return -1
