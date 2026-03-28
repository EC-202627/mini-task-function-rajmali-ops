def calculate_fine(book_title, days_overdue, daily_rates = 5.0):
    fine = days_overdue*daily_rates
    return fine

book_title = input()
days_overdue = int(input())
daily_rates = int(input())
fine = calculate_fine(book_title, days_overdue,daily_rates)
print("Book:", book_title)
print("Days overdue:", days_overdue)
print("Fine: Rs.", fine)
