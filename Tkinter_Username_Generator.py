from tkinter import *
win = Tk()

# Random Username Generator
import random


def username_generator():
    adjectives = ['Excellent', 'Amazing', 'Fantastic', 'Gloomy', 'Contagious', 'Ambient', 'Agitated', 'Raging',
                  'Critical', 'Determined', 'Healthy', 'Inspired', 'Creative', 'Healthy', 'Livid', 'Bitter',
                  'Strengthened', 'Refreshed', 'Vibrant', 'Motivated', 'Frozen', 'Stunned', 'Dynamic']
    nouns = ['Bread', 'Toast', 'Banana', 'Elephant', 'Apple', 'Ad', 'Wasp', 'Meat', 'Guy', 'Girl', 'Berry',
             'Clock', 'File', 'Test', 'Pen', 'Sun', 'Moon', 'Cow', 'Chicken', 'List', 'Button', 'Bar', 'Car',
             'Phone', 'Brand', 'Person', 'Space', 'Ball', 'Air', 'Computer', 'Color']
    numbers = list(range(100))
    label = Label(win, text=f'                        {random.choice(adjectives)}{random.choice(nouns)}{random.choice(numbers)}{random.choice(numbers)}                     ')
    label.grid(row=3, column=1)


myLabel = Label(win, text='Press The Button to Generate a Username')
myButton = Button(win, text='Generate Username', padx=100, pady=100, command=username_generator, bg='purple')
myLabel.grid(row=1, column=1)
myButton.grid(row=2, column=1)
win.geometry("500x500")
win.mainloop()
