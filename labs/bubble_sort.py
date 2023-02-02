unbubbled = [4,8,7,5,7,6,420,7,45,14]

def bubble(unbubbled_list):
    for i in range(0, len(unbubbled_list)):
        for j in range(0, len(unbubbled_list) - i - 1):
            if unbubbled_list[j] > unbubbled_list[j + 1]:
                unbubbled_list[j], unbubbled_list[j + 1] = unbubbled_list[j + 1], unbubbled_list[j]
                print(unbubbled_list)
    return unbubbled_list
    
print(bubble(unbubbled))  