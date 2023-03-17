# Define a function to calculate loan payments
def calculate_loan_payment(principal, interest_rate, num_years):
    monthly_rate = interest_rate / 12
    num_payments = num_years * 12
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-num_payments))
    return payment

# Define a function to calculate interest rates
def calculate_interest_rate(principal, payment, num_years):
    num_payments = num_years * 12
    monthly_rate = 0.01
    while True:
        new_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** (-num_payments))
        if abs(new_payment - payment) < 0.001:
            break
        monthly_rate += 0.0001
    return monthly_rate * 12 * 100

# Get user input for loan amount, interest rate, and number of years
principal = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
num_years = float(input("Enter the number of years: "))

# Calculate the monthly payment and total interest paid
payment = calculate_loan_payment(principal, interest_rate / 100, num_years)
total_interest = payment * 12 * num_years - principal

# Print the results
print(f"Monthly payment: ${payment:.2f}")
print(f"Total interest paid: ${total_interest:.2f}")

# Get user input for loan amount, payment amount, and number of years
principal = float(input("Enter the loan amount: "))
payment = float(input("Enter the monthly payment amount: "))
num_years = float(input("Enter the number of years: "))

# Calculate the interest rate
interest_rate = calculate_interest_rate(principal, payment, num_years)

# Print the result
print(f"Interest rate: {interest_rate:.2f}%")
