import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = 'd4629ea6c9c52b192ad2b95207e2b631'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        weather_data = response.json()
        
        if weather_data['cod'] == 200:
            weather_description = weather_data['weather'][0]['description']
            temparature = weather_data['main']['temp']
            messagebox.showinfo(f'Weather in {city}', f'Temparature: {temparature}°C\nDescription: {weather_description}')
        else:
            messagebox.showerror('Error',f'Cannot find weather data for {city}')  
    except requests.exceptions.RequestException:
        messagebox.showerror('Error','Failed to connect to the weather service. Please check your Internet Connection.') 

# GUI Setup
root = tk.Tk()
root.title('Weather App')

label = tk.Label(root, text ='Enter City: ')
label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(root, text ='Get Weather', command = get_weather)
get_weather_btn.pack(pady=10)

root.mainloop()
