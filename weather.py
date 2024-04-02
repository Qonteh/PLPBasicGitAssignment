from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
 
 
def get_weather():
   try:
       city = textfield.get()
       geolocator = Nominatim(user_agent="weather_app")
       location = geolocator.geocode(city)
 
 
       if not location:
           raise ValueError("City Not Found")
 
 
       timezone_finder = TimezoneFinder()
       result = timezone_finder.timezone_at(lng=location.longitude, lat=location.latitude)
 
 
       home_timezone = pytz.timezone(result)
       local_time = datetime.now(home_timezone)
       current_time = local_time.strftime("%I:%M %p")
       clock.config(text=current_time)
       name.config(text=f"CURRENT WEATHER in {city}, {location.address.split(',')[-1].strip()}")
 
 
       # Weather API
       api_key = "1adf7b7b41514913765b9130ba236b96"
       api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
 
 
       json_data = requests.get(api).json()
       weather_info = json_data.get('weather', [{}])[0]
       main_info = json_data.get('main', {})
       wind_info = json_data.get('wind', {})
       sys_info = json_data.get('sys', {})
 
 
       condition = weather_info.get('main', '')
       description = weather_info.get('description', '')
       temp = int(main_info.get('temp', 0) - 273.15)
       pressure = main_info.get('pressure', 0)
       humidity = main_info.get('humidity', 0)
       wind_speed = wind_info.get('speed', 0)
       country = sys_info.get('country', '')
       sunrise_time = datetime.utcfromtimestamp(sys_info.get('sunrise', 0)).strftime('%H:%M:%S')
       sunset_time = datetime.utcfromtimestamp(sys_info.get('sunset', 0)).strftime('%H:%M:%S')
 
 
       temperature_label.config(text=f"{temp} °C")
       condition_label.config(text=f"{condition} | Temperature is {temp} °C")
 
 
       wind_label.config(text=f"Wind: {wind_speed} m/s")
       humidity_label.config(text=f"Humidity: {humidity}%")
       description_label.config(text=f"{description.capitalize()}")
       pressure_label.config(text=f"Pressure: {pressure} hPa")
       country_label.config(text=f"Country: {country}")
       sunrise_label.config(text=f"Sunrise: {sunrise_time}")
       sunset_label.config(text=f"Sunset: {sunset_time}")
 
 
   except Exception as e:
       messagebox.showerror("Weather App", str(e))
 
 
 
 
# Creating the main window
root = Tk()
root.title("Weather App - The Pycodes")
root.geometry("900x600")
root.resizable(False, False)
 
 
# Creating search box
textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()
 
 
search_button = Button(text="Search", font=("Arial", 12, 'bold'), command=get_weather)
search_button.place(x=400, y=34)
 
 
# Creating labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)
 
 
label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)
 
 
label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)
 
 
label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)
 
 
label5 = Label(root, text="COUNTRY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label5.place(x=120, y=500)
 
 
label6 = Label(root, text="SUNRISE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label6.place(x=250, y=500)
 
 
label7 = Label(root, text="SUNSET", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label7.place(x=430, y=500)
 
 
temperature_label = Label(font=("arial", 70, "bold"), fg="#ee666d")
temperature_label.place(x=400, y=150)
condition_label = Label(font=("arial", 15, 'bold'))
condition_label.place(x=400, y=250)
 
 
wind_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
wind_label.place(x=120, y=430)
 
 
humidity_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
humidity_label.place(x=280, y=430)
 
 
description_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
description_label.place(x=450, y=430)
 
 
pressure_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
pressure_label.place(x=650, y=430)
 
 
country_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
country_label.place(x=120, y=530)
 
 
sunrise_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
sunrise_label.place(x=250, y=530)
 
 
sunset_label = Label(text="...", font=("arial", 15, 'bold'), bg="#1ab5ef")
sunset_label.place(x=430, y=530)
 
 
# Time
name = Label(root, font=("arial", 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20,))
clock.place(x=30, y=130)
 
 
root.mainloop()