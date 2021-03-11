import math
'''
1° = (π * rad)/180   
1 rad = 180°/π   
'''
degree = 360
radian = degree*math.pi/180
print('%d degree is %f radians' %(degree, radian))


degree = 45
radian = degree*math.pi/180
print('%d degree is %f radians' %(degree, radian))


print('%d degree is %f radiana'%(360, math.radians(360)))
print('%d degree is %f radiana'%(45, math.radians(45)))
print('')



small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22

small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2

print('small','\t',small_pizza_r,'\t',small_pizza_price,'\t',small_area)
print('big','\t', big_pizza_r,'\t',big_pizza_price,'\t',big_area)
print('family','\t',family_pizza_r,'\t',family_pizza_price,'\t',family_area)
print('\n')
print('small',small_pizza_price/small_area)
print('big',big_pizza_price/big_area)
print('family',family_pizza_price/family_area)
print('')

math_ls = dir(math) 
print(math_ls)
