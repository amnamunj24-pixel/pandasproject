import pandas as pd

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        self.quantity -= amount
        # might want to add a check here so it doesn't go negative
        if self.quantity < 0:
            self.quantity = 0

# load morning stock
stock_df = pd.read_csv("p2.csv")
stock_df = stock_df.rename(columns={'Qty_kg': 'Current_Quantity'})

# get coffee beans row
coffee_row = stock_df[stock_df['Ingredient'] == 'Coffee Beans']
if coffee_row.empty:
    print("No coffee beans found in stock file")
else:
    name = coffee_row.iloc[0]['Ingredient']
    qty = coffee_row.iloc[0]['Current_Quantity']

    coffee = Ingredient(name, qty)
    coffee.use_item(2.5) # busy day

    # update the dataframe
    stock_df.loc[stock_df['Ingredient'] == 'Coffee Beans', 'Current_Quantity'] = coffee.quantity
    stock_df.to_csv("p2.csv", index=False)
    print(f"Updated coffee beans. New qty: {coffee.quantity} kg")