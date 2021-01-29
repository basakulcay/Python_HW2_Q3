#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:56:59 2021

@author: basakulcay
"""

Newyork=['Mozarella','Pepperoni','Basil','Green Pepper']
Veggie=['Mozarella', 'Mushroom', 'Green Pepper', 'Onion']
Margarita=['Spicy Tomato Sauce', 'Mozarella']
BBQ=['Mozarella', 'BBQ Sauce','Grilled Chicken', 'Onion' ]
Extra=['Olive','Salami','Sausage','Corn']
extselect=[]

Price_newyork= 10
Price_veggie= 12
Price_margarita= 8
Price_BBQ= 15

print("Welcome to Pizza MIS")
print("---------------------------Menu--------------------------")
print("Newyork:", Newyork)
print("Veggie:", Veggie)
print("Margarita:", Margarita)
print("BBQ:", BBQ)
print("Extra's:", Extra)
#again='Yes'

def main():

    selection=input("Which pizza do you prefer?: ")
    extra= input('Would you like to add extra ingredients? Yes or No: ')
    
    while extra== 'Yes' or extra=='yes':
        extselect=input("Enter the extra ingredient you want to add your pizza: ")
        try: 
            extselect_index=Extra.index(extselect)
            print("Here is your extra list")
            print(extselect)
            if selection=='Newyork' or selection=='newyork':
                Newyork.insert(0,extselect)
                print ("Here is your selection:", Newyork)
                
            if selection=='Veggie' or selection=='veggie':
                Veggie.insert(0,extselect)
                print ("Here is your selection:", Veggie)
                
            if selection=='Margarita' or selection=='margarita':
                Margarita.insert(0,extselect)
                print ("Here is your selection:", Margarita)
            if selection=='BBQ' or selection=='bbq':
                BBQ.insert(0,extselect)
                print ("Here is your selection: ", BBQ)
                
        except ValueError:
            print("That item was not found in the Extra list")
        
        
    try: 
        if selection== 'Newyork' or selection=='newyork':
            print("Here is your selection: ")
            print(Newyork)
            price(selection)
        if selection=='Veggie' or selection=='veggie':
            print("Here is your selection: ")
            print(Veggie)
        if selection== 'Margarita' or selection=='margarita':
            print("Here is your selection: ")
            print(Margarita)
        if selection== 'BBQ' or selection=='bbq':
            print("Here is your selection: ")
            print(BBQ)
            print('Do you want to order anything else? (Yes or No)')
            again=input('')
            #selection=input("Which pizza do you prefer?: ")
            #extra= input('Would you like to add extra ingredients? Yes or No: ')
        
    except ValueError:
           print("That item was not found in the list ")
           
def price(selection):
    if selection== 'Newyork' or selection=='newyork':
        print('It will cost USD',Price_newyork)
    elif selection== 'Veggie' or selection=='veggie':
        print('It will cost USD',Price_veggie)
    elif selection== 'Margarita' or selection=='margarita':
        print(Price_margarita)
    elif selection== 'BBQ' or selection=='bbq':
        print('It will cost USD',Price_BBQ)
    else:
        print('Enter again')
        
main()
