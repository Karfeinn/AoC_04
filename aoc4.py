def get_data():
    with open("test.txt", "r", encoding="utf-8") as file:
        input_data = file.read()
        input_data = input_data.split()
        input_data = [list(char) for char in input_data]
    return input_data

def is_forkliftable(input_data):
    total = []
    for i in range(0, len(input_data)):
        for j in range(0, len(input_data[i])):
            if input_data[i][j]==0:
                continue
            if i == 0 and j == 0 and input_data[i][j] == 1:
                total.append((i,j))
                continue
            if i == len(input_data) -1 and j == 0 and input_data[i][j] == 1:
                total.append((i,j))
                continue
            if i == len(input_data) -1 and j == len(input_data[i])-1 and input_data[i][j] == 1:
                total.append((i,j))
                continue
            if i == 0 and j == len(input_data[i])-1 and input_data[i][j] == 1:
                total.append((i,j))
                continue
            if i == 0:
                somme = input_data[i][j-1] + input_data[i][j+1] + input_data[i+1][j-1] + input_data[i+1][j] + input_data[i+1][j+1]
            elif j == 0 :
                somme = input_data[i-1][j] + input_data[i-1][j+1] + input_data[i][j+1] + input_data[i+1][j] + input_data[i+1][j+1]
            elif i == len(input_data)-1 :
                somme = input_data[i][j-1] + input_data[i-1][j-1] + input_data[i-1][j] + input_data[i-1][j+1] + input_data[i][j+1]
            elif j == len(input_data[i])-1 :
                somme = input_data[i-1][j] + input_data[i-1][j-1] + input_data[i][j-1] + input_data[i+1][j] + input_data[i+1][j-1]
            else :
                somme = input_data[i-1][j] + input_data[i-1][j-1] + input_data[i][j-1] + input_data[i+1][j-1] + input_data[i+1][j] + input_data[i+1][j+1] + input_data[i][j+1] + input_data[i-1][j+1]
            if somme < 4 :
                total.append((i,j))
    
    for couple in total:
        input_data[couple[0]][couple[1]] = 0
    return len(total)

def get_binary_data(input_data):   
    for i in range(0,len(input_data)):
        for j in range(0,len(input_data)) :
            if input_data[i][j] == ".":
                input_data[i][j]  = int(0)
            else: input_data[i][j] = int(1)
    return input_data

def recursive():
    data = get_binary_data(get_data())
    last_mouved = is_forkliftable(data)
    total = last_mouved
    while last_mouved != 0:
        last_mouved = is_forkliftable(data)
        total += last_mouved
    return total

print(recursive())