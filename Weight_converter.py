weight = int(input('Weight: '))
unit = input('(K)g or (L)bs: ')

if unit.upper() == 'K': 
    converted = (weight * 2.205) 
    print ('Weight is: ' + str(converted) +' '+ 'Lbs')
else: 
    converted = (weight / 2.205)
    print ('Weight is: ' + str(converted) +' '+'Kg')
