print("Welcome to the tip calculator")
total_bill = float(input("What was your total bill ? Rs."))
tip = int (input("How much tip would you like to give ? 10 , 12 or 15"))
People = int(input (" How many people to split the bill? "))
bill_with_tip = tip / 100 * total_bill + total_bill
bill_per_person = total_bill / People
final_amount = round(bill_per_person, 2)
print(f'Each person should pay: Rs.{final_amount}')