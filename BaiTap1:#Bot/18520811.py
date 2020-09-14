import re

def read_data():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    data_list = re.split('\s', lines[1])
    filtered_list = list(filter(lambda y: y is not '', data_list))
    res = list(map(lambda y: int(y), filtered_list))

    return res

def main():
    from_var = 0
    data = read_data()
    res_data = {
        'from': 1,
        'to': len(data),
        'sum': sum(data)
    }

    while len(data) > from_var:
        for i in range(from_var, len(data)):
            range_sum = sum(data[from_var: i])
            if range_sum > res_data['sum']:
                res_data['from'] = from_var + 1
                res_data['to'] = i
                res_data['sum'] = range_sum
        from_var += 1

    print(res_data)


if __name__ == "__main__":
    main()