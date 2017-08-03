shoplist = ['apple','banana','mango','carrot']

print('I have',len(shoplist),'items to purchase.')

print('these item are:')
for item in shoplist:
    print(item)

print('\nI also have to by rice.')
shoplist.append('rice')

print('my shoplist is now,',shoplist)

print('sort my list')
shoplist.sort()
print('sorted list',shoplist)

print('first item is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('bought',olditem)
print('shoplist is now ',shoplist)
