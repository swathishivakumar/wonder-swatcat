def activity01(num1):
    '''determine if an input number is even or odd'''
    if (num1 % 2 == 0):
		return 'Even'
    else:
		return 'Odd'

def activity02(iv_one, iv_two):
        '''return the sum of two input numbers'''
        sum_one_two= iv_one + iv_two
        return sum_one_two
        
def activity03(num_list):
	'''given a list of integers, count how many are even'''
        even_count = 0
        odd_count = 0
        for number in num_list:
                if (number % 2 == 0):
                        even_count += 1
                else:
                        odd_count += 1
        return even_count 
        
def activity04(stringi):
        '''return the input string, backwards'''
        return stringi[::-1]
