def calculate_fine(book_title, days_overdue, daily_rates = 5.0):
    fine = days_overdue*daily_rates
    return f"Book: {book_title} Days overdue: {days_overdue} Fine: Rs. {fine}"

book_title = input()
days_overdue = int(input())
fine = calculate_fine(book_title, days_overdue)
print(fine)