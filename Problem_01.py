def calculate_fine(book_title, days_overdue, daily_rates = 5):
    fine = days_overdue*daily_rates
    return f"{book_title} Days overdue: {days_overdue} Fine: Rs.{fine}"

print(calculate_fine(input(),int(input())))