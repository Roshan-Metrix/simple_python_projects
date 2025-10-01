## Inputs we need from the user 
# Total rend, food , electricity_spend, charge_per_unit, no of persons



rent = int(input("Enter your hostel/flat rent :"))
food = int(input("Enter the amount of food order : "))
electricity_spend = int(input("Enter the total of electricity spend : "))
charge_per_unit = int(input("Enter the charge per unit : "))
persons = int(input("Enter the no. of persons living in room/flat : "))


total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)
