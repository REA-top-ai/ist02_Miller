#1
contains_a = lambda word: 'a' in word
print(contains_a('apple'))

#2
long_string = lambda string: len(string) > 12
print(long_string('hello, world!'))

#3
end_in_a = lambda string: string[-1] == 'a'
print(end_in_a('sea'))

#4
even_or_odd = lambda num: 'четное' if num % 2 == 0 else 'нечетное'
print(even_or_odd(3))

#5
multiple_of_three = lambda num: 'кратно трем' if num % 3 == 0 else 'не кратно'
print(multiple_of_three(6))

#6
rate_movie = lambda rating: 'мне понравился этот фильм' if rating > 8.5 else 'этот фильм не очень'
print(rate_movie(7.6))