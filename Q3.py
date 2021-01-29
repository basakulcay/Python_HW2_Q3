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
selected=[]
total=0

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
    selected.append(selection)
    #total+=Price_newyork
    extra= input('Would you like to add extra ingredients? Yes or No: ')
    
    while extra== 'Yes' or extra=='yes':
        extselect=input("Enter the extra ingredient you want to add your pizza: ")
        try: 
            extselect_index=Extra.index(extselect)
            
            if selection.lower()=='newyork':
                Newyork.insert(0,extselect)
                print ("Here is your new selection:", Newyork)
                extra=input('Do you want to add another ingredient? (Yes or No): ')
                
            if selection.lower()=='veggie':
                Veggie.insert(0,extselect)
                print ("Here is your new selection:", Veggie)
                extra=input('Do you want to add another ingredient? (Yes or No): ')
                
            if selection.lower()=='margarita':
                Margarita.insert(0,extselect)
                print ("Here is your new selection:", Margarita)
                extra=input('Do you want to add another ingredient? (Yes or No): ')
                
            if selection.lower()=='bbq':
                BBQ.insert(0,extselect)
                print ("Here is your new selection: ", BBQ)
                extra=input('Do you want to add another ingredient? (Yes or No): ')
                
        except ValueError:
            print("That item was not found in the Extra list")
            extra=input('Do you want to add an extra ingredient? (Yes or No): ')
        
    try: 
        if selection.lower()== 'newyork':
            print("Here is your selection: ")
            print(Newyork)
            price(selection)
        if selection.lower()=='veggie':
            print("Here is your selection: ")
            print(Veggie)
        if selection.lower()== 'margarita':
            print("Here is your selection: ")
            print(Margarita)
        if selection.lower()== 'bbq':
            print("Here is your selection: ")
            print(BBQ)
           
        again=input('Do you want to order another pizza? (Yes or No) ')
        if again=='Yes' or again=='yes':
            main()
        else:
            print('The pizzas you ordered are: ',selected)
            #print(total)
            
    except ValueError:
           print("That item was not found in the list ")
           
def price(selection):
    if selection.lower()== 'newyork':
        print('It will cost USD',Price_newyork)
       
    elif selection.lower()== 'veggie':
        print('It will cost USD',Price_veggie)
    elif selection.lower()== 'margarita':
        print(Price_margarita)
    elif selection.lower()== 'bbq':
        print('It will cost USD',Price_BBQ)
    else:
        print('Enter again')
        
main()
