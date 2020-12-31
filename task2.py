time_in_seconds = int(input("Enter time in seconds: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = (time_in_seconds % 3600) % 60
print(f"Time in hh:mm:ss format: {hours:>02}:{minutes:>02}:{seconds:>02}")
