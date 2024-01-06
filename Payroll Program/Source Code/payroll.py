# Afraz Akram
# March 19, 2023
# Verison 1.0
# ICS4U
# Mr. Manyanga
# This program will create a payslip designed for the one week pay period.
# It will prompt the user to enter the employee name and number, total hours
# worked, and hourly rate. The input will be processed in order to calculate
# overtime calculations, pre-tax cuts and income tax cuts. Finally, the net
# pay will be calculated. The output will be a text file showing all calculations.

# Open the file location.

f = open("C:\\Users\\Afraz\\Documents\\Programming\\ICS4U\\payroll\\payroll.txt", "w")

# Greet the user and tell them the function of this program.

print("Welcome to the payslip creator, which is designed for the one week pay period.")

# Input the name of the employee.

employeeName = input("Enter Employee Name: ")

# Input the code of the employee.

employeeCode = input("Enter Employee Code: ")

# Create a variable for the hourly rate.

hourlyRate = 0

# Loop so that the user enters a valid value, or a rate not less than minimum wage.

while True:

    hourlyRate = input("Enter Hourly Rate: ")
    
    try:
        hourlyRate = float(hourlyRate)
        
    except ValueError:
        print("Please enter a valid value.")
        continue
    
    if hourlyRate < 15.50:
        print("The minimum wage is $15.50.")
        continue
    
    else:
        break

# Calculate overtime rate.

overtimeRate = hourlyRate * 1.5

# Varaible for total hours.

totalHours = 0

# Loop so that the user enters a valid value.

while True:
    
    totalHours = input("Enter TOTAL Hours Worked in Week (Pay Period and Overtime): ")
    
    try:
        totalHours = int(totalHours)
        
    except ValueError:
        print("Please enter a valid value.")
        continue
    
    if totalHours < 0 or totalHours > 168:
        print("Please enter a valid value.")
        continue
    
    else:
        break

# Variables for overtime hours, regular hours, and federal income tax. 

overtimeHours = 0

regularHours = 0

fedIncTax = 0

# Calculate regular hours and overtime hours.

if totalHours > 40:
    overtimeHours = totalHours - 40
    regularHours = 40

else:
    regularHours = totalHours

# Calculate pays.

overtimePay = overtimeRate * overtimeHours

regularPay = hourlyRate * regularHours

grossPay = regularPay + overtimePay

# Calculate cuts.

cutPension = round(grossPay * 0.01065, 2)

cutEI = round(grossPay * 0.01, 2)

unionDues = 7.38

# Calculate salary. 

salaryYear = grossPay * 52

# Tax brackets.

if salaryYear <= 53359:
    fedIncTax = 0.15

elif salaryYear > 53359 and salaryYear <= 106717:
    fedIncTax = 0.205

elif salaryYear > 106717 and salaryYear <= 165430:
    fedIncTax = 0.26

elif salaryYear > 165430 and salaryYear <= 235675:
    fedIncTax = 0.29

else:
    fedIncTax = 0.33

# Calculate tax cut and net pay.

remainingPay = round((grossPay - cutPension - cutEI - unionDues), 2)

cutTax = round((remainingPay * fedIncTax), 2)

netPay = round((remainingPay - cutTax), 2)

# Write all payslip contents. 

f.write(f"Employee Name: {employeeName}\n")
f.write(f"Employee Code: {employeeCode}\n\n")
f.write(f"Total Hours Worked: {totalHours}\n")
f.write(f"Hours Worked in Pay Period: {regularHours}\n")
f.write(f"Pay in Pay Period: ${regularPay}\n")
f.write(f"Hours Worked in Overtime: {overtimeHours}\n")
f.write(f"Pay in Overtime: ${overtimePay}\n")
f.write(f"Gross Pay: ${grossPay}\n\n")
f.write(f"Pension Cut: -${cutPension}\n")
f.write(f"EI Cut: -${cutEI}\n")
f.write(f"Union Dues: -${unionDues}\n")
f.write(f"Remaining Pay (Pre-Tax): ${remainingPay}\n\n")
f.write(f"Federal Income Tax Cut: -${cutTax}\n")
f.write(f"Net Pay!: ${netPay}\n")

print("Payslip created!")

f.close()