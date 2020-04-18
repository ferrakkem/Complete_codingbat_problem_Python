'''
The parameter weekday is True if it is a weekday,
and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
def sleep_in(weekday, vacation):
    if(not weekday or vacation):
        return True
    else:
        False

#print(sleep_in(False, False))

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling. 
Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

def monkey_trouble(a_smile, b_smile):

    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return True

#print(monkey_trouble(False, True))

'''
Given two int values, return their sum. 
Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''
def sum_double(num1, num2):
    sum = 0
    if (num1 == num2):
        sum = (num1 + num2)*2
        return sum
    else:
        sum = num1+num2
        return sum

#print(sum_double(2, 2))

'''
Given an int n, return the absolute difference between n and 21, 
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''

def diff21(n):

    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

#print(diff21(66))

'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''

def parrot_trouble(hour, is_talking):

    if ((is_talking) and (hour<7 or hour>20)):
        return True
    else:
        return False

#print(parrot_trouble(True, 7))

'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
'''

def makes10(a, b):

    if (a == 10) or (b == 10) or (a+b == 10):
        return True
    else:
        return False

#print(makes10(1, 9))

'''
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''

def near_hundred(n):
    diff1 = abs(100 - n)
    diff2 = abs(200 - n)
    if (diff1 <= 10 or diff2 <= 10):
        return True
    else:
        return False

#print(near_hundred(90))

'''
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''

def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))

#print(pos_neg(-1, -1, True))


'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
'''

def not_string(sting):
    checking_value = 'Not'
    if not checking_value.upper() in sting.upper():
        return "Not " + sting
    else:
        return sting

#print(not_string('Not bad'))

'''
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''

def missing_char(string, n):
    front = string[:n]
    back = string[n + 1:]
    return front + back

#print(missing_char('kitten', 1))

'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(str):

    if len(str) <= 1:
        return str

    front_chrac = str[0]
    back_chrac = str[-1]
    rest_chrac = str[1:-1]
    return  back_chrac + rest_chrac + front_chrac

#print(front_back('a'))

'''
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc
'''

def front3(string):
    get_front_three = string[:3]
    return get_front_three*3


#print(front3('Chocolate'))

'''
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi
'''

def string_times(string, number):

    if (number>0):
        return string*number
    else:
        return "You input negative number"

#print(string_times('Hi', -3))

'''
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''

def front_times(string, number):
    front_slice = string[:3]
    if (number <= 3):
        return front_slice*number
    else:
        return front_slice*number

#print(front_times('abc', 3))

'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(string):
    result = ""
    for i in range(len(string)):
        if i%2 == 0:
            result = result + string[i]
    return result

#print(string_bits('Heeololeo'))

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab
'''

def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result

#print(string_splosion('ab'))

'''
Given a string, return the count of the number of times that 
a substring length 2 appears in the string and also as 
the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

def last2(string):
    pass


'''
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''

def array_count9(number):
    count = 0
    for i in number:
        if i == 9:
            count = count + 1
    return count

#print(array_count9([1, 9, 9, 3, 9,9]))

'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

def array_front9(number):
    count = 0
    end = len(number)
    if end > 4:
        end = 4

    for i in range(end):
        if number[i] == 9:
            return True
    return False


#print(array_front9([1, 2, 3, 4, 9]))

'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

def array123(numbers):
    for i in range(len(numbers) - 2):
        if numbers[i] == 1 and numbers[i + 1] == 2 and numbers[i + 2] == 3:
            return True
    return False

#print(array123([1, 1, 2, 3, 1]))

'''
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
'''

def make_abba(a, b):
    return a+b+b+a

print(make_abba('Yo', 'Alice'))
