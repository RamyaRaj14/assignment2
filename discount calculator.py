#discount calculator
purchase_amt=int(input("Enter the purchased amount"))
if purchase_amt>=100 and purchase_amt<=1000:
    print("Discount is 0%")
    discount=purchase_amt*0//100
    total_bill=purchase_amt-discount
elif purchase_amt>=1001 and purchase_amt<2000:
    print("Discount is 15%")
    discount=purchase_amt*15//100
    total_bill=purchase_amt-discount
elif purchase_amt>=2001 and purchase_amt<3000:
    print("Discount is 20%")
    discount=purchase_amt*20//100
    total_bill=purchase_amt-discount
else:
    print("Discount is 25%")
    discount=purchase_amt*25//100
    total_bill=purchase_amt-discount

print("Purchased amount:",purchase_amt)
print("Discount:",discount)
print("Total Bill:",total_bill)
