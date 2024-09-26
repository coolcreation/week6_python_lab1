#  Jeff Bohn
#  9/25/2024
#  Working with Dates & Times

############ Chapter 11 Exercise 1 - Invoice Due Date ############

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ") 
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
            if invoice_date < datetime.now():
               #print(type(invoice_date))
                return invoice_date
            else:
                print("Date must be today or earler try again")
        except ValueError:
            print("Invalid date format! Try again.")
            continue


def main():
    print("\nThe Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        due_date = due_date.date()                     # get only the date from the datetime object
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()



