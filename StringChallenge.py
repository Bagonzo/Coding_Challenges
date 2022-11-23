# String Challenge
# Have the function
# String Challenge (str) take the
# str parameter being passed and
# determine if it is an acceptable
# sequence by either returning the
# string true or false. The str
# parameter will be composed of + and
# = symbols with several characters
# between them (ie. ++d+===+c++==a)
# and for the string to be true each
# letter must be surrounded by a +
# symbol. So the string to the left would
# be false. The string will not be empty
# and will have at least one letter.
# Examples
# Input: "+d+=3=+S+"

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