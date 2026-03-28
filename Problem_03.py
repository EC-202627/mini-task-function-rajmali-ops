def calculate_fine(book_title, days_overdue, daily_rates = 5.0, max_fine = 150.0):
    fine = days_overdue*daily_rates
    if fine > max_fine:
        fine = max_fine
        str = f"{fine}\nYou have accumulated the maximum fine of INR: 150.0"
        return str
    else:
        return fine

book_title = input()
days_overdue = int(input())
fine = calculate_fine(book_title, days_overdue)
print("Book:", book_title)
print("Days overdue:", days_overdue)
print("Fine: Rs.", fine)