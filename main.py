def findFirstUniqueElement(arr):
    i = 0
    j = 0
    while i < len(arr):
        i = j
        j = i + 1
        while j < len(arr) and arr[j] == arr[i]:
            j += 1
        length = j - i
        
        if length == 1: break
    
    # return current i
    if i == len(arr):
        return None 
    
    return arr[i]


if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3,3,3,3,3,4,4,5,5,5,5,6,6,7,7,7,9,9,9,10]
    arr2 = [1,2,2,2,3,3,3,3,3,3,4,4,5,5,5,5,6,6,7,7,7,9,9,9,10]
    arr3 = [1,1,2,2,2,3,4,4,5,5,5,5,6,6,7,7,7,9,9,9,10]
    arr4 = [1,1,2,2,2,3,3,4,4,5,5,5,5,6,6,7,7,7,9,9,9,10,10]

    print(findFirstUniqueElement(arr))
    print(findFirstUniqueElement(arr2))
    print(findFirstUniqueElement(arr3))
    print(findFirstUniqueElement(arr4))