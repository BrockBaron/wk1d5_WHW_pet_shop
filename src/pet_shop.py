#1
from typing import Collection, Counter


def get_pet_shop_name(pet_shop):
    return pet_shop['name']             #[]refering to a dictionary key, either {} or []
    print([])

#2
def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

#3 & 4
def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount
#    get_total_cash(pet_shop)+= amount doesnt work due to a infinite loop/ retunring a re assignment into a variable

#5
def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

#6
def increase_pets_sold(pet_shop, qty):
    pet_shop['admin']['pets_sold'] += qty

#7
def get_stock_count(pet_shop):
    return len(pet_shop['pets'])  #returning count of keys in dictionary 'pets'
    # total_pets=0
    # for pet in pet_shop:        
    #     total_pets += len(pet_shop['pets'][0]['names'])
    # return total_pets

#8 & 9
def get_pets_by_breed(pet_shop, breed_name):
    breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            breed.append(pet)
    return breed

#10 & 11
def find_pet_by_name(pet_shop, pet_name):
    for name in pet_shop["pets"]:
        if name["name"] == pet_name:
            return name

#12
def remove_pet_by_name(pet_shop, pet_name):
    for pet in range(len(pet_shop['pets'])): 
        if pet_shop['pets'][pet]['name'] == pet_name: 
            del pet_shop['pets'][pet] 
            break
        
    #print (pet_shop['pets'])

#13
def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop['pets'].append(new_pet)

#14
def get_customer_cash(customer):
    return customer['cash']

#15
def remove_customer_cash(customer, money):
    customer['cash'] -= money

#16
def get_customer_pet_count(customer):
    return len(customer['pets'])

#17    
def add_pet_to_customer(customer, new_pet):
    return customer['pets'].append(new_pet)    

#18 & 19 & 20
def customer_can_afford_pet(customer, new_pet):
    if customer['cash']>= new_pet['price']:
        return True
    elif customer['cash']< new_pet['price']:
        return False
    

#21

def sell_pet_to_customer(pet_shop, pet, customer):
    customer['pets']+= pet
    pet_shop['admin']['pets_sold'] += 1
    
    get_customer_pet_count.append() # add or subtract pet cound dependant on if selling or buying from customer
    
    get_pets_sold.append() # inrease pet sold in sale or state 0 in buy
    
    get_customer_cash.append() # subtract in purchase of pet, increase in sale of pet
    
    get_total_cash.apped() # increase in sale of pet, decrease in purchase of pet
    
    
# add pet to customer pets list increase value by 1 - retrun get customer pet count funciton

# increase value 'number' in pets sold - return get pets sold fucntion

# change customers cash after purchase i.e. get customer remaining cash after purchase - return get customer cash

# increase value of total cash in shop in crease value by 900 - return get total cash in shop



# reset values of pets sold and customer owned values

# create loop (for or while) to take customer cash and add it to total cash

# create loop to remove pet from shop and add it to customer pet value count

#create logic or loop to either sell or buy , changing the dirctiong of customer cash and shop cash, and customer pet count and shops pet count.


