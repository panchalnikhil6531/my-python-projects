light_color = input("Enter the traffic light color (green, yellow, red): ").lower()
if light_color == "green":
    print("Car is allowed to go.")
elif light_color == "yellow":
    print("Car has to wait.")
elif light_color == "red":
    print("Car has to stop.")
else:
    print("Unrecognized signal.")
