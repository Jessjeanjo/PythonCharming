# Created by Jessica Joseph on 02/21/18

## variables
a = 9
b = 10

my_variable = 26
any_variable_name = 10 # number cannot be at the start of your variable name

string_variable = "jessica" # python only knows this is 7 chars and the first char is a 'j'
single_quotes = 'strings can have single quotes' 

print(my_variable)
print(string_variable) # just the content gets printed out



## methods
def my_print_method(my_argument):
	print(my_argument)

my_print_method('hello world')


def my_multiply_method(number_one, number_two):
	return number_one * number_two

my_print_method(my_multiply_method(3,7))
