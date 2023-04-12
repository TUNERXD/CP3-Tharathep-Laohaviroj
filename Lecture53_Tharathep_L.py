def VatCalculate(Totalprice):
    result = Totalprice + (Totalprice * 7/100)
    return result
print(VatCalculate(float(input("Totalprice: "))))
