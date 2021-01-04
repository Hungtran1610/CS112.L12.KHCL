s = input()
list_a = list(s)
int_s = int(s)
list_a.sort()

# TH1: Nếu dãy chia hết cho 3 thì sắp xếp dãy giảm gần, in dãy -> thoát
if int_s % 3 == 0:
    list_a.reverse()
    print(''.join(list_a))
    exit()

x = int(int_s % 3)

# tìm i trong a sao cho a[i] % 3 = x, nếu không trả về -1
def senario_one(input_string, x):
    ind_result = -1
    if str(x) in input_string:
        ind_result = input_string.index(str(x))
        return ind_result
    
    if str(x + 3) in input_string:
        ind_result = input_string.index(str(x + 3))
        return ind_result
    
    if str(x + 6) in input_string:
        ind_result = input_string.index(str(x + 6))
        return ind_result

    return ind_result

# tìm vị trí i, j trong a sao cho a[i] % 3 = x, a[j] % 3 = x, nếu không trả về -1, -1
def senario_two(input_string, x):
    first_index = senario_one(input_string, x)
    second_index = senario_one(input_string[first_index + 1: ], x) + first_index + 1
    return first_index, second_index

# Tìm và xóa vị trí không thỏa mãn điều kiện, sắp xếp lại dãy giảm dần, in dãy
ind = senario_one(list_a, x)
if ind == -1:
    ind_1, ind_2 = senario_two(list_a, (x*2)%3)
    if ind_1 != -1 and ind_2 != -1:
        list_a.remove(list_a[ind_1])
        list_a.remove(list_a[ind_2 - 1])

        list_a.reverse()

        if len(list_a) == 1:
            print(str(list_a[0]))
            exit()
        else:
            print(''.join(list_a))
            exit()

list_a.remove(list_a[ind])
list_a.reverse()
if list_a != []:
    print(''.join(list_a))
    exit()