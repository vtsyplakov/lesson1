def get_summ (one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    one_delimiter_two = one+delimiter+two
    upper_string = f'{one_delimiter_two}'.upper()
    print(upper_string)

get_summ ('Learn', 'python')

def format_price (price):
    price = int(price)
    string_price = f'Цена: {price} руб.'
    print (string_price)

format_price (56.24)