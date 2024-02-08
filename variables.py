#conversion variables pounds to kilograms

print("POUNDS TO KILOGRAMS CONVERSION")
print("______________________________")
weight = int(input("What is your weight? "))
lb_or_kg = input("(L)lbs or (K)kgs:")


if lb_or_kg.upper() == 'L':
    kg = weight * 0.45
    print(f'You are {kg} kg.')

else:
    kg = weight / 0.45
    print(f'You are {kg} lbs')

    

      
