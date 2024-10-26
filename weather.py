import tkinter
from tkinter import PhotoImage
from tkinter import ttk
import requests
import json
from pathlib import Path

def func_get_weather():
    city = select_city_dropdown.get()
    api_key = "c2fbea751a183c38f45e79ac1cc8c378"  # Replace with your actual API key
    api_url = (f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c2fbea751a183c38f45e79ac1cc8c378&units'
               f'=metric')
    server_data = requests.get(api_url)
    server_data_json = server_data.json()

    if server_data.status_code == 200:
        temp = server_data_json["main"]["temp"]
        output_label.config(text=f'Temperature: {temp}°C')
    else:
        output_label.config(text="Error fetching data")
    output_label.pack(pady=10)


root = tkinter.Tk()
root.geometry("500x600")
root.title("My Weather App")

# Absolute Path Example
# image_path = r"C:\Users\prana\PranavProjects\pythonProject\weather1.png"
#
# # OR using forward slashes
# image_path = "C:/Users/prana/PranavProjects/pythonProject/weather1.png"

# OR using pathlib for modern and robust path handling
# from pathlib import Path
image_path = Path("C:/Users/prana/PranavProjects/pythonProject/weather1.png")

bg_image = PhotoImage(file=image_path)
set_bg_image = tkinter.Label(root, image=bg_image)
set_bg_image.place(relheight=1, relwidth=1)

app_header = tkinter.Label(root, text="My Weather App", font=('Georgia', 24), bg='White', fg='Blue')
app_header.pack(pady=20)

cities = ['Bengaluru', 'Mumbai', 'Pune', 'Goa', 'Delhi','Akola','Akot','Amravati','Nagpur']
select_city_dropdown = ttk.Combobox(root, values=cities, font=('Georgia', 10))  # Correct parameter name is 'values'
select_city_dropdown.pack(pady=20)

get_weather_button = tkinter.Button(root, text='Get Weather', font=('Georgia', 15), command=func_get_weather)
get_weather_button.pack(pady=10)

output_label = tkinter.Label(root, text="", font=('Georgia', 15))
output_label.pack(pady=10)

root.mainloop()
