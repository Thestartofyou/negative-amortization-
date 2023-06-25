def is_negative_amortization(r, n, P, A):
    """
    Checks if a borrower is at risk of negative amortization.

    r: Annual interest rate as a decimal (e.g., 0.05 for 5%)
    n: Loan term in months
    P: Loan principal amount
    A: Monthly payment amount

    Returns True if the borrower is at risk of negative amortization, False otherwise.
    """
    monthly_interest = r / 12  # Monthly interest rate
    remaining_balance = P  # Initial remaining balance

    for _ in range(n):
        interest_payment = remaining_balance * monthly_interest
        principal_payment = A - interest_payment
        remaining_balance -= principal_payment

        if remaining_balance < 0:
            return True

    return False


# Example usage:
interest_rate = 0.05  # 5% annual interest rate
loan_term = 360  # 30-year loan term (360 months)
loan_amount = 200000  # $200,000 loan amount
monthly_payment = 1000  # $1,000 monthly payment

at_risk = is_negative_amortization(interest_rate, loan_term, loan_amount, monthly_payment)

if at_risk:
    print("Borrower is at risk of negative amortization.")
else:
    print("Borrower is not at risk of negative amortization.")
