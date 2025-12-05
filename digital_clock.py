import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock - Nature.Dev")
root.geometry("400x200")
root.configure(bg='black')

# Time label (big, cyan text on black)
time_label = tk.Label(root, 
                     font=('Arial', 40, 'bold'), 
                     fg='cyan', 
                     bg='black')
time_label.pack(pady=20)

# Date label (smaller, white text)
date_label = tk.Label(root, 
                     font=('Arial', 16), 
                     fg='white', 
                     bg='black')
date_label.pack()

def update_time():
    # Update time every second
    current_time = strftime('%H:%M:%S')
    current_date = strftime('%Y-%m-%d %A')
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # Schedule next update in 1000ms (1 second)
    root.after(1000, update_time)

# Start the clock
update_time()

# Run the GUI
root.mainloop()
