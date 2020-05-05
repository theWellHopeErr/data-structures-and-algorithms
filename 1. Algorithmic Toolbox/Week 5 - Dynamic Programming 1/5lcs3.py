import sys
def longest_common_subsequence(string1,string2):
    cols = len(string1)+1
    rows = len(string2)+1
    memory = [[0 for _ in range(cols)] for x in range(rows)]
    max_length=0
    
    for i in range(1,rows):
        for j in range(1,cols):
            if string1[j-1] == string2[i-1]:
                memory[i][j] = 1+memory[i-1][j-1]
            else:
                memory[i][j] = max(memory[i-1][j],memory[i][j-1])
            max_length = max(max_length,memory[i][j])
    
    return max_length

def longest_common_subsequence_three(string1,string2,string3):
    Z = len(string3)+1
    Y = len(string1)+1
    X = len(string2)+1

    memory = [[[0 for z in range(Z)] for y in range(Y)] for x in range(X)]
    max_length=0
    
    for i in range(1,X):
        for j in range(1,Y):
            for k in range(1,Z):
                if (string1[j-1] == string2[i-1]) and (string1[j-1]==string3[k-1]):
                    memory[i][j][k] = 1+memory[i-1][j-1][k-1]
                else:
                    memory[i][j][k] = max(memory[i-1][j][k],memory[i][j-1][k],memory[i][j][k-1])

                max_length = max(max_length,memory[i][j][k])
    return max_length


def lcs3(a, b, c):
    return longest_common_subsequence_three(a, b, c)

if __name__ == '__main__':
    n1 = int(input())
    a = input()
    n1 = int(input())
    b = input()
    n1 = int(input())
    c = input()
    print(lcs3(a,b,c))