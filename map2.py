str_list = ['1', '100', '33']
str_to_int = list(map(int, str_list))

float_list = (3.14, 3.5, 22.6)
float_to_int = tuple(map(int, float_list))

print(str_to_int, float_to_int)