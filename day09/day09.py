#has_good_credit = True
#home_price = 1_000_000

#if has_good_credit:
    #down_payment = home_price * 0.1
#else:
   # down_payment = home_price * 0.2

#print(f"Peşinat tutarı: ${down_payment:,.0f}")

weight = float(input("Weight? "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print(f"{converted:.1f} pounds")
else:
    converted = weight * 0.45
    print(f"{converted:.1f} kg")