import tkinter as tk
from tkinter import messagebox

# Conversion functions
def pm25_to_ppm(pm25):
    return pm25 * 0.000001

def ppm_to_pm25(ppm):
    return ppm * 1000000

# Function to classify PM2.5 levels
def classify_pm25(pm25):
    if pm25 <= 12:
        return "Good"
    elif pm25 <= 35:
        return "Moderate"
    elif pm25 <= 55:
        return "Unhealthy for Sensitive Groups"
    elif pm25 <= 150:
        return "Unhealthy"
    elif pm25 <= 250:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Function to handle conversion and display result
def convert():
    value = float(entry_value.get())
    if conversion_type.get() == "µg/m³ to ppm":
        converted_value = pm25_to_ppm(value)
        category = classify_pm25(value)
        result_label.config(text=f"Converted Value: {converted_value:.6f} ppm\nCategory: {category}")
    elif conversion_type.get() == "ppm to µg/m³":
        converted_value = ppm_to_pm25(value)
        category = classify_pm25(converted_value)
        result_label.config(text=f"Converted Value: {converted_value:.2f} µg/m³\nCategory: {category}")
    else:
        messagebox.showerror("Error", "Invalid conversion type selected")

# Function to clear the input and result fields
def clear():
    entry_value.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Air Pollution Level Converter")
root.geometry("400x300")

# Create a frame for the input section
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Label and input field for value
label_value = tk.Label(input_frame, text="Enter Pollution Value:")
label_value.grid(row=0, column=0, padx=10, pady=5)

entry_value = tk.Entry(input_frame)
entry_value.grid(row=0, column=1, padx=10, pady=5)

# Dropdown to select conversion type
conversion_type = tk.StringVar(value="µg/m³ to ppm")
conversion_options = ["µg/m³ to ppm", "ppm to µg/m³"]
dropdown = tk.OptionMenu(input_frame, conversion_type, *conversion_options)
dropdown.grid(row=1, column=0, columnspan=2, pady=10)

# Button to convert
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result label to display the converted value and category
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
result_label.pack(pady=10)

# Button to clear the input and result
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=10)

# Run the main loop
root.mainloop()
