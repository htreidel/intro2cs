# hadart_787, Hadar Treidel, 20325554


def create_list():
    """recieves input from user, str only,
       and creates list of words seperated by ' '"""
    strings_from_user_list = []
    user_string = input()
    while user_string != '':
        strings_from_user_list.append(user_string)
        user_string = input()
    return strings_from_user_list


#print(create_list())
    

def concat_list(str_lst):
    """performs concatenation on list of strings and
       returns single string"""
    concatenation = str()
    for i in str_lst:
        concatenation += i
    return concatenation


#print(concat_list(['Hello world', 'What', ' ', 'a nice day', '3']))


def average(num_list):
    """recieves a list of int or float,
       returns average"""
    sum_of_list = 0
    number_count = 0
    if num_list == []:
        return None
    for i in num_list:
        sum_of_list += i
        number_count += 1
    return sum_of_list / number_count


#print(average([2.7, 5, 2, 0.0, 6.3]))
#print(average([]))

        
def cyclic(lst1, lst2):
    """recieves two list and compares if one is
       cyclic trasformation of the other, returns
       true or false"""
    if len(lst1) != len(lst2):
        return False
    lister = lst1[:]
    for i in range(len(lst1)):
        if lst2 == lister:
            return True
        rotation = lister[0]
        lister.remove(rotation)
        lister.append(rotation)
    else:
        return False
        
#print(cyclic('abcd','bcda'))


def histogram(n, num_list):
    """recieves a positive integer and a list of numbers in
       range of 0 to n-1, returns relevant histogram"""
    L = []
    L_counter = 0
    histogram = []
    histogram_counter = 0
    for i in range(n):
        L.append(L_counter)
        L_counter += 1
    for i in L:
        histogram_counter = 0
        for j in num_list:
            if i == j:
                histogram_counter += 1
        histogram.append(histogram_counter)
    return histogram

#print(histogram(3,[1,2,3,4]))


def prime_factors(n):
    """recieves an integer bigger than 1
       returns a list of the prime factors"""
    devider = 2
    prime_factors = []
    if n <= 1:
        return prime_factors
    while devider <= n:
        if n % devider == 0:
            prime_factors.append(devider)
            n = n / devider
        else:
            devider += 1
    if prime_factors != []:
        return prime_factors
    else:
        prime_factors.append(n)
        return prime_factors

#print(prime_factors(0))


def cartesian(lst1, lst2):
    """recieves two lists and returns a list
       consisting of all possible pairs of objects
       from the who lists"""
    list_of_lists = []
    for i in lst1:
        for j in lst2:
            lister = (i, j)
            list_of_lists.append(lister)
    return list_of_lists


#print(cartesian([1, 1], [2]))
            
            
def pairs(n, num_list):
    """ recieves an integer and a list of integers
        which must all be different, returns pairs of
        numbers that add up to the integer"""
    pairs = []
    for i in num_list:
        for j in num_list:
            if i != j:
                if i + j == n and i < j:
                    pairs.append([i,j])
    return pairs


print( pairs(2,[0,0,1,1,2,2]))
                
            
        
            
        
        
