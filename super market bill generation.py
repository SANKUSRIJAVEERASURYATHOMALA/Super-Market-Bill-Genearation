# SUPER MARKET BILL GENERATION PROJECT

print("========== SUPER MARKET ==========")

items = []
units = []
quantities = []
prices = []
totals = []

grand_total = 0

while True:

    item = input("\nEnter Item Name: ")

    print("\nSelect Unit Type")
    print("1. KG")
    print("2. Liters")
    print("3. Pieces")
    print("4. Dozens")

    choice = int(input("Enter Choice (1/2/3/4): "))

    # KG Items
    if choice == 1:
        unit = "KG"
        quantity = float(input("Enter Quantity in KG: "))
        price = float(input("Enter Price per KG: "))

    # Liter Items
    elif choice == 2:
        unit = "Liters"
        quantity = float(input("Enter Quantity in Liters: "))
        price = float(input("Enter Price per Liter: "))

    # Piece Items
    elif choice == 3:
        unit = "Pieces"
        quantity = int(input("Enter Number of Pieces: "))
        price = float(input("Enter Price per Piece: "))

    # Dozens Items
    elif choice == 4:
        unit = "Dozens"
        quantity = int(input("Enter Number of Dozens: "))
        price = float(input("Enter Price per Dozen: "))

    else:
        print("Invalid Choice")
        continue

    total = quantity * price

    items.append(item)
    units.append(unit)
    quantities.append(quantity)
    prices.append(price)
    totals.append(total)

    grand_total += total

    again = input("\nDo You Want To Add Another Item? (yes/no): ")

    if again.lower() != "yes":
        break


# BILL DISPLAY
print("\n")
print("=============== FINAL BILL ===============")

print("{:<15} {:<10} {:<12} {:<12} {:<12}".format(
    "Item", "Unit", "Quantity", "Price", "Total"
))

for i in range(len(items)):
    print("{:<15} {:<10} {:<12} {:<12} {:<12}".format(
        items[i],
        units[i],
        quantities[i],
        prices[i],
        totals[i]
    ))

print("==========================================")
print("Grand Total = Rs.", grand_total)

# DISCOUNT SECTION
if grand_total >= 5000:
    discount = grand_total * 0.20

elif grand_total >= 3000:
    discount = grand_total * 0.10

elif grand_total >= 1000:
    discount = grand_total * 0.05

else:
    discount = 0

final_amount = grand_total - discount

print("Discount = Rs.", discount)
print("Final Amount = Rs.", final_amount)

# GST Calculation
gst = final_amount * 0.18
net_amount = final_amount + gst

print("GST (18%) = Rs.", gst)
print("Net Amount = Rs.", net_amount)

print("\n========= THANK YOU VISIT AGAIN =========")