def convert_to_seconds(minutes, seconds):
    return minutes * 60 + seconds

def convert_to_hours(seconds):
    return seconds / 3600

def main():
    total_seconds = 0

    while True:
        user_input = input("Enter time (minutes:seconds) or type 'done' to finish: ").strip()
        if user_input.lower() == 'done':
            break

        try:
            minutes, seconds = map(int, user_input.split(':'))
            total_seconds += convert_to_seconds(minutes, seconds)
        except ValueError:
            print("Invalid format. Please enter time in the format minutes:seconds.")
    
    total_hours = convert_to_hours(total_seconds)
    print(f"Total time in hours: {total_hours:.2f} hours")

if __name__ == "__main__":
    main()
