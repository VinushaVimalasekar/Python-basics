weight = int(input('Weight: '))
unit = input('(K)g or (L)bs: ')

if unit.upper() == 'K': 
    converted = (weight * 0.45) 
    print ('Weight is: ' + str(converted) +' '+ 'Lbs')
else: 
    converted = (weight / 0.45)
    print ('Weight is: ' + str(converted) +' '+'Kg')
