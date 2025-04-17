def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0]-1, command[1], command[2]-1
        if j == len(array):
            arr = sorted(array[i:])
        arr = sorted(array[i:j])
        print(arr)
        answer.append(arr[k])
        
    return answer