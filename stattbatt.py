import psutil
import tkinter as tk

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged
        power_status = "Plugged In" if power_plugged else "On Battery"
        return f"Battery Status: {power_status}\nBattery Percentage: {percent}%"
    else:
        return "Battery information not available."

def update_label():
    battery_info = get_battery_info()
    label.config(text=battery_info)
    root.after(10000, update_label)  # Update every 10 seconds

root = tk.Tk()
root.title("StattBatt")

label = tk.Label(root, text="", font=("Helvetica", 16))
label.pack(padx=20, pady=20)

update_label()  # Initial update
root.mainloop()
