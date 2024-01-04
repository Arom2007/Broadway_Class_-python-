# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours
# worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string, float() to convert the string to number.

hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter the rate per hour: "))
gross_pay = 1.0
if hours - 40.0 <= 0:
    gross_pay *= hours * rate_per_hour
elif hours-40.0 > 0:
    gross_pay *= (40 * rate_per_hour) + ((hours - 40) * (rate_per_hour * 1.5))

print(f"The gross pay for the individual is Rs.{gross_pay} for working {hours} hours.")