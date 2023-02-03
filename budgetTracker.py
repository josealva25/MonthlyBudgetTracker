import csv
import datetime
import smtplib
 
expenses = []
#Replace the 'bank.csv' with your own csv file from your bank
with open('bank.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    next(reader)

    for row in reader:
        amount  = row[2].replace('$', '')
        if amount == '':
            amount = 0.0
        date = datetime.datetime.strptime(row[0], '%m/%d/%Y').date()
        if date.month == 1:
            expenses.append({
            'date': row[0],
            'description': row[1],
            'amount': float(amount)
        })
            

total_expenses = sum(expense['amount'] for expense in expenses)

limit = 500.0

if total_expenses > limit * 0.9:
    remaining_budget = limit - total_expenses

print('Total Expense: ', total_expenses)