#  Jeff Bohn
#  9/25/2024
#  Working with Dates & Times

############ Chapter 11 Exercise 2 - Timer Program ############

from datetime import datetime, time, date


def printTime(seconds, microseconds):
    return print(f"Seconds: {seconds}.{microseconds}")


def main():
    print("\nThe Timer program\n")

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print(f"Start time: {start_time}\n")
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print(f"Stop time: {stop_time}\n")

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60 
    minutes = minutes % 60

    # display results
    try:
        print("ELAPSED TIME")
        if hours > 0:
            if minutes < 10:
                print(f"Hours/minutes: {hours}:0{minutes}")
            else:
                print(f"Hours/minutes: {hours}:{minutes}")
            printTime(seconds, microseconds)
        elif minutes > 0:
            print(f"Minutes: {minutes}")
            printTime(seconds, microseconds)
        else:
            printTime(seconds, microseconds)
        print()
    except Exception as e:
        print(Exception, e)

if __name__ == "__main__":

    main()
