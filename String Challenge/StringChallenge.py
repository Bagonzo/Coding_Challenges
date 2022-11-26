def StringChallenge(arr):
    if len(arr) <= 3:
        return False
    elif (arr[0] >= 'a' and arr[0] <= 'z') or (arr[0] >= 'A' and arr[0] <= 'Z'):
        return False
    elif (arr[-1] >= 'a' and arr[-1] <= 'z') or (arr[-1] >= 'A' and arr[-1] <= 'Z'):
        return False
    else:
        for i in range(1, len(arr)-1):
            if (arr[i] >= 'a' and arr[i] <= 'z') or (arr[i] >= 'A' and arr[i] <= 'Z'):
                if arr[i-1] != "+" or arr[i+1] != "+":
                    return False
            else:
                return True

s = input("Enter the string: ")
print(StringChallenge(s))