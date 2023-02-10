from guizero import *
from  random import * 
root = App()
welcome_message = Text(root, text="Terrain Generator By @SmashedFrenzy16")
size = 17
waffle = Waffle(root ,height=size, width=size, pad=0, color="green") 
down = randint(4, 8) 
left = randint(2, 5) 
# Coast 
for x in range(size):     
  y = size - 1     
  depth = randint(2, 6)     
  for i in range(depth):         
    waffle.set_pixel(x, y, "blue")         
    y = y - 1         
    sand = randint(1, 2)         
    for j in range(0, sand):             
      waffle.set_pixel(x, y, "yellow") 
# Mountains 
for x in range(size):     
  y = size - 1     
  grass = randint(7, 10)     
  for y in range(0, grass):         
    waffle.set_pixel(x, y, "light green")         
    y = y - 1         
    greymount = randint(3, 7)         
    for y in range(greymount):             
      waffle.set_pixel(x, y, "grey")             
      y = y - 1             
      whitemount = randint(2, 3)             
      for y in range(0, whitemount):                 
        waffle.set_pixel(x, y, "white")  
# River
x = size // 2  
y = 0         
waffle.set_pixel(x, y, "blue") 
for i in range(0, down):     
  waffle.set_pixel(x, y, "blue")     
  y = y + 1 
for i in range(0, left):     
  waffle.set_pixel(x, y, "blue")     
  x = x - 1 
for i in range(0, down):     
  waffle.set_pixel(x, y, "blue")     
  y = y + 1 
for i in range(0, (left * 2)):     
  waffle.set_pixel(x, y, "blue")     
  x = x + 1 
while y < size:     
  waffle.set_pixel(x, y, "blue")     
  y = y + 1  
root.display()
