def calculate_fine(book_title, days_overdue, daily_rates = 5.0):
    fine = days_overdue*daily_rates
    return f"Book: {book_title} \nDays overdue: {days_overdue} \nFine: Rs. {fine}"

print(calculate_fine(input(),int(input())))