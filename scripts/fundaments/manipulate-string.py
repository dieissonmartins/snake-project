cpf = '289.306.350-08'
print(cpf)

# size cpf
size_cpf = len(cpf)
print(size_cpf)

# type cpf
type_cpf = type(cpf)
print(type_cpf)

# concat
print(cpf + ' concatenated')

# replace
replace_cpf = cpf.replace('.', '')
replace_cpf = replace_cpf.replace('-', '')
print(replace_cpf)

type_replace_cpf = type(replace_cpf)
print(type_replace_cpf)

# convert string by int
int_cpf = int(replace_cpf)
print(int_cpf)

# type var cpf integer
type_int_cpf = type(int_cpf)
print(type_int_cpf)

# check initial value string
check_init = cpf.startswith('289')
print(check_init)

check_init = cpf.startswith('000')
print(check_init)

# check end value string
check_end = cpf.endswith('-08')
print(check_end)

check_end = cpf.endswith('777')
print(check_end)

# counter words
string_word = 'in publishing and graphic design, 12 Lorem ipsum is placeholder text commonly 17 to demonstrate ipsum. '
print(string_word)

count_words_ipsum = string_word.count('ipsum')
print(count_words_ipsum)

# transform texts

# first capital letter
first_letter_up = string_word.capitalize()
print(first_letter_up)

# check exits numbers by string
check_exists_number = string_word.isdigit()
print(check_exists_number)

# all capitals
string_word_upper = string_word.upper()
print(string_word_upper)

# all little
string_word_lower = string_word.lower()
print(string_word_lower)

# get value by position string
find_value_string = string_word.find('design')
print(find_value_string)

# remove spaces by one string
string_removed_spaces = string_word.strip()
print(string_removed_spaces)

# desmenbrer string to array
string_word_by_array = string_word.split(' ')
print(string_word_by_array)

