from tkinter import Tk, Frame, Button, Label, Entry, Scrollbar,Listbox, StringVar
from PIL import Image, ImageTk
from tkinter import ttk
import requests
root=Tk()
root.geometry("350x350")
root.title("Weather App")
root.config(background="grey")

#background image
background_image=r"C:\Users\TestUser\Desktop\Python\weather_app\images\new2.jpg"
image=Image.open(background_image)
photo=ImageTk.PhotoImage(image)
imageLabel=Label(image=photo)
imageLabel.pack()
cities = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry",
    "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir"
]
#SEARCH BOX
search_box=ttk.Combobox(root, width=27,values=cities,state="normal")
search_box.place(x=80,y=80,height=25)

#labell 3
lable3=Label(root)
lable3.place(x=93,y=150,height=120,width=160)
#GET WEATHER WITH API
def weather():
    city_name=search_box.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=dd1fb1a291dca283d94a0b44f111f3c4&units=metric")
    # lable3.config(text=data[weather])
    final = data.json()
    print(final)
    main=final["weather"][0]["main"]
    temp=final["main"]["temp"]
    humidity=final["main"]["humidity"]
    temp_min=final["main"]["temp_min"]
    temp_max=final["main"]["temp_max"]
    lable3.config(text=f" The temperature is :{temp} \n At {city_name}, it feels like {main} \n The min. temp is {temp_min}° \n The max. temp is {temp_max}° \n The humidity is {humidity} ")
    # if data.status_code==200:

        

#search button
button1 = Button(root, text="search", bg="white", width=4, height=1,command=weather)  # Customize button appearance
button1.place(x=265, y=80)  # Adjust the position as needed




#weather app text

Label2=Label(root,text="Weather App",font="Arial", height=1)
Label2.place(x=130,y=50)




root.mainloop()






# root.mainloop()

# import tkinter as tk

# # Create the main application window
# root = tk.Tk()

# # Set the window title
# root.title("My Tkinter Application")

# # Set the window size
# root.geometry("300x200")

# # Create a label widget
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack(pady=20)

# # Start the Tkinter event loop
# root.mainloop()


# from tkinter import Tk, Label, Button
# from PIL import Image, ImageTk

# # Create the main application window
# root = Tk()

# # Set window properties
# root.geometry("350x350")
# root.title("Weather App")
# root.config(background="grey")

# # Load and resize the background image
# background_image_path = r"C:\Users\TestUser\Desktop\Python\weather_app\images\new2.jpg"
# image = Image.open(background_image_path)
# image = image.resize((350, 350), Image.Resampling.LANCZOS)

# # Convert the image to Tkinter format
# photo = ImageTk.PhotoImage(image)

# # Create a Label to display the background image
# imageLabel = Label(root, image=photo)
# imageLabel.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch to fill the window

# # Create and place a button on top of the image
# button1 = Button(root, text="hello", bg="white")  # Customize button appearance
# button1.place(x=100, y=100)  # Adjust the position as needed

# # Start the Tkinter event loop
