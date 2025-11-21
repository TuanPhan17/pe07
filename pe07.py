class Restaurant: # Defining a class called restaurant
    def __init__(self, restaurant_name, cuisine_type): # __init__ method stores restaurent and cuisine type 
        self.restaurant_name = restaurant_name # Store name in objective
        self.cuisine_type = cuisine_type # Store cuisine in objective

    def describe_restaurant(self): # Method to print restaurant details 
        print(f"Restaurant Name: {self.restaurant_name}") # Print restaurant name
        print(f"Cuisine Type: {self.cuisine_type}") # Print cuisine tpye 

    def open_restaurant(self): # Method to show restaurant is open 
        print(f"{self.restaurant_name} is now open!") # Print restaurnt (name) is open 

restaurant1 = Restaurant("Pho_Tuan", "Vietnamese") # made a viet restaurant and cuisine 
restaurant2 = Restaurant("Sushi_House", "Japanese") # made a japanese restaurant and cuisine
restaurant3 = Restaurant("Pizza_Palace", "Italian") # made a italian restaurant and cuisine

restaurant1.describe_restaurant() # Print details for pho_tuan
restaurant2.describe_restaurant() # Print details for sushi_house
restaurant3.describe_restaurant() # Print details for pizza_palace 
