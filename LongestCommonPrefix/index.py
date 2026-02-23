def find():
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]

    arr.sort()
    result = ""
    for i in range(len(arr[0])):
        for s in arr:
            if i== len(s) or s[i] != arr[0][i]:
                return result
        result += arr[0][i]

print(find())