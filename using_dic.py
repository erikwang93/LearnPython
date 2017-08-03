act = {
    'Masami':30,
    'Gakki':29,
    'Alison':35
}

print('Masami\'s age is %d' % act['Masami'])


act['Nina'] = 28

del act['Alison']

print('There is %d actor in this book' % len(act))
for name,age in act.items():
    print('Name: %s,Age: %d' % (name,age))

if act['Nina'] in act:
    print('Yes,her age is %d' % act['Nina'])