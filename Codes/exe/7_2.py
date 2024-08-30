# Write a code that read two strings and to generate the third with characters that be in both strings.

string_0 = 'AAACTBF'
string_1 = 'CBT'

set_str0 = set(string_0)
set_str1 = set(string_1)

intersection = (set_str0.intersection(set_str1))

string_2 = ''.join(intersection)

print(f'The third string:   {string_2}')
