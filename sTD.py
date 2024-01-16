import tkinter as tk

def calculate_result():
    try:
        distance = float(entry_distance.get())
        time = float(entry_time.get())
        speed = distance / time
        result_label.config(text=f"Speed: {speed} km/h")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


STD = tk.Tk()

STD.title("Speed Calculator")


instrlabel = tk.Label(STD, text="กรุณา ใส่ ระยะทาง(Km) และ เวลา")
instrlabel.pack()


distance_label = tk.Label(STD, text="ระยะทาง (กิโลเมตร):")
distance_label.pack()
entry_distance = tk.Entry(STD)
entry_distance.pack()

time_label = tk.Label(STD, text="เวลา (ชั่วโมง):")
time_label.pack()
entry_time = tk.Entry(STD)
entry_time.pack()


calculate_button = tk.Button(STD, text="Calculate", command=calculate_result)
calculate_button.pack()


result_label = tk.Label(STD, text="")
result_label.pack()

STD.mainloop()
