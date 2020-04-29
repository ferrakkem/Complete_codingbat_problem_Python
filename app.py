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

#print(make_abba('Yo', 'Alice'))


'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
'''

def make_tags(tag, string):
    making_tag = "<{tag}>".format(tag)
    print(making_tag)

#make_tags('i','yay')

'''
Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]
'''

def make_out_word (str1, str2):
    frist = str1[:2]
    second = str1[2:]
    return frist+str2+second


#print(make_out_word('[[]]', 'Yay'))

'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
'''

def extra_end(string):
    last_two_chars = string[-2:]
    return last_two_chars*3

#print(extra_end('Hello'))

'''
Given a string, return the string made of its first two chars, 
so the String "Hello" yields "He". If the string is shorter than length 2, 
return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
'''

def first_two(string):

    if len(string)>2:
        first_two_chars = string[:2]
        return first_two_chars
    else:
        return string

#print(first_two('ab'))

'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc
'''
def first_half(string):
    get_string_length = int(len(string)/2)
    return string[:get_string_length]

#print(first_half('HelloThere'))

'''
Given a string, return a version without the first and last char,
so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
'''
def without_end(string):

    return string[1:len(string)-1]

#print(without_end('coding'))

'''
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava
'''

def non_start(str1, str2):
    return str1[1:]+str2[1:]

#print(non_start('Hello', 'There'))

######################################----List_1------############################

'''
Given an array of ints, return True if 6 appears as either the first or last element in the array.
The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''

def first_last6(number):
    if number[0] == 9 or number[-1] == 6:
        return True
    else:
        return False

#print(first_last6([13, 6, 1, 2, 3]))

'''
Given an array of ints, return True if the array is length 1 or more, 
and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
'''

def same_first_last(num):
    if num[0] == num[-1]:
        return True
    else:
        return False

#print(same_first_last([1, 2, 1]))

'''
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
Both arrays will be length 1 or more.

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
'''
def common_end(num1, num2):
    if (num1[0]== num2[0]) or(num1[-1] == num2[-1]):
        return True
    else:
        return False

#print(common_end([1, 2, 3], [1, 3]))

'''
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
'''

def reverse3(number):
    return number[::-1]

#print(reverse3([1, 2, 3]))
####------------------------------------------------logic-1---------------------------------------------------------

'''
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

'''

def cigar_party(cigars,is_weekend):

    if (cigars >= 40) and (cigars <=60) or(cigars >= 40) and is_weekend:
        return True
    else:
        return False

#print(cigar_party(30,False))

'''
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, 
and "date" is the stylishness of your date's clothes. 
The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. 
If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, then the result is 0 (no).
Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
'''

def date_fashion(you, my_date):

    if (you >= 8) or my_date >= 8:
        return '2'
    elif (you <= 2 or my_date<= 2):
        return '0'
    else:
        return '1'

#print(date_fashion(5, 10))


'''
The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, 
return True if the squirrels play and False otherwise.

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
'''

def squirrel_play(temperature, is_summer):

    if (is_summer):
        if (temperature >= 60) and (temperature <= 100):
            return True
    else:
        if (temperature >= 60) and (temperature <= 90):
            return True
        else:
            return False

#print(squirrel_play(95, True))

'''
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an 
int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
'''

def caught_speeding(speed, is_birthday):

    if(is_birthday):
        if speed <= 65:
            return 0
        elif (speed >= 65) and (speed <= 85):
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif (speed >= 60) and (speed <= 80):
            return 1
        else:
            return 2

#print(caught_speeding(60, False))


'''
Given 2 ints, a and b, return their sum. 
However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
'''

def sorta_sum(a, b):
    sum = a+b
    if sum in range(10, 19):
        return '20'
    else:
        return sum

#print(sorta_sum(19, 4))

'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating 
if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. 
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
'''

def alarm_clock(day, is_vacation):

    if (is_vacation):
        if (day >= 1) and (day <= 5):
            return "10.00"
        else:
            return 'Off'

    else:
        if (day >= 1) and (day <= 5):
            return "7.00"
        else:
            return '10.00'

#print(alarm_clock(5, True))

'''
The number 6 is a truly great number. 
Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
'''

def love6(a, b):

    if (a == 6) or (b == 6):
        return True
    elif abs(a+b) == 6:
        return True
    elif abs(a-b) == 6:
        return True
    else:
        return False

#print(love6(13, 7))

'''
Given a non-negative number "num", return True 
if num is within 2 of a multiple of 10. 
Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. 

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
'''

def near_ten(num):
    mod_num = num % 10
    if mod_num <= 2:
        return True
    else:
        return False

#print(near_ten(17))

##--------------------------------logic-2-----------------------------------##

'''
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
def make_bricks():
    pass


'''
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, 
it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
'''

def lone_sum(a, b, c):

    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c

#print(lone_sum(1, 2, 3))

'''
Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''
def lucky_sum(a, b, c):

    if a == 13:
        return b+c
    elif b == 13:
        return a
    elif c == 13:
        return a+b
    else:
        return a+b+c

#print(lucky_sum(1, 13, 3))

'''
Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive 
-- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
'''

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) +fix_teen(c)


def fix_teen(n):
    #checking in the range 13..19 inclusive then that value counts as 0, except 15 and 16 do not count as a teens
    if  n >=13 and n <= 19 and n !=15 and n!= 16:
        return 0
    return n

#print(no_teen_sum(2, 1, 16))

'''
For this problem, we'll round an int value up to the next multiple of 10 
if its rightmost digit is 5 or more, so 15 rounds up to 20. 
Alternately, round down to the previous multiple of 10 
if its rightmost digit is less than 5, so 12 rounds down to 10. 
Given 3 ints, a b c, return the sum of their rounded values. 
To avoid code repetition, write a separate helper "def round10(num):" 
and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
'''
def round_sum(a, b, c):
    return round10(a)+round10(b)+round10(c)

def round10(num):
    if num%10 <5:
        return num - (num%10)
    else:
        return num + (10 - num%10)

#print(round_sum(16, 17, 18))

'''
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
while the other is "far", differing from both other values by 2 or more. 
Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
'''
def close_far():
    pass


'''
We want make a package of goal kilos of chocolate. 
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''

#--------------------------------string-2-----------------------------------------------

'''
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
'''
def double_char(string):
    new_string = ""

    for i in string:
        new_char = i*2
        new_string = new_string + new_char
    return new_string
#print(double_char('Hi-There'))

'''
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
'''

def count_hi(string):
    cout = 0

    for i in range(len(string)-1):
        if string[i] =='h' and string[i+1] == 'i':
            cout = cout+1
    return cout
#print(count_hi('hihi'))

'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''

def cat_dog(string):
    cat_count = 0
    dog_count = 0

    cat_count = string.count('cat')
    dog_count = string.count('dog')

    if cat_count == dog_count:
        return True
    else:
        return False

#print(cat_dog('catcat'))

'''
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''

def count_code(string):
    count = 0

    for i in range(len(string)-1):
        if string[i] == 'c' and string[i+1] =='o' and string[i+3] == 'e':
            count = count+1
    return count

#print(count_code('cozexxcope'))


'''
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
'''
def end_other(str1, str2):
    str1_last_chat = str1[-1]
    str2_last_chat = str2[-1]
    #print(str1_last_chat)
    #print(str2_last_chat)
    if str1_last_chat.lower() == str2_last_chat.lower():
        return True
    else:
        return False

#print(end_other('Abd', 'HiaBc'))

'''
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''
def xyz_there(string):
    check_xyz = string.count('xyz')
    dot_count = string.count('.xyz')
    #print(f'{check_xyz} and {dot_count}')

    if check_xyz==dot_count:
        return False
    else:
        return True

#print(xyz_there('.xyzabc'))

#--------------------------list-2---------------------------------------------------------
'''
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

def count_evens(numbers):
    count = 0
    for i in numbers:
        if i%2==0:
            count = count +1
    return count

#print(count_evens([1, 3, 5]))

'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
'''

def big_diff(numbers):
    lg_num = max(numbers)
    sm_num = min(numbers)

    difference = lg_num - sm_num
    return difference


print(big_diff([7, 2, 10, 9]))

'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
'''
def centered_average():
    pass


'''
Return the sum of the numbers in the array, returning 0 for an empty array. 
Except the number 14 is very unlucky, so it does not count and numbers that come immediately after a 14 also do not count.

sum14([1, 2, 2, 1]) → 6
sum14([1, 1]) → 2
sum14([1, 2, 2, 1, 14]) → 6

'''
def sum14(numbers):
    sum = 0
    #i = 0

    for i in range(len(numbers)-1):
        if numbers[i] == 14:
            numbers.pop(i)
        sum = sum + numbers[i]

    return sum

#print(sum14([1, 2,1,1,2,14,1,1]))

'''
Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''

def sum67(numbers):
    result = 0
    flag = True

    for num in numbers:
        if num == 6:
            flag = False
        if flag:
            result += num
        if num == 7:
            flag = True
    return result


print(sum67([1, 2, 2, 6, 99, 99, 7]))

'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''

def has22(nums):

    for i in nums:
        if nums[i] == 2 and nums[i+1] == 2:
            return True
        else:
            return False

#print(has22([1, 2, 1, 2]))