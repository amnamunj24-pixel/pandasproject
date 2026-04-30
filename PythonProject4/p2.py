import pandas as pd
class Ingredients:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        self.quantity -= amount
        if self.quantity <= 0:
            self.quantity = 0

stock_df = pd.read_csv("p2.csv")
stock_df = stock_df.rename(columns={'Qty_kg' : 'Current_Quantity'})

coffe_row = stock_df[stock_df['Ingredient'] == 'Coffee Beans']
if coffe_row.empty:
    print("No coffee beans")
else:
    coffee_row = coffe_row.iloc[0]
    qty = coffee_row['Current_Quantity']

    coffee = Ingredients(coffee_row['Ingredient'], qty)
    coffee.use_item(2.5)

    stock_df.loc[stock_df['Ingredient'] == 'Coffee Beans', 'Current_Quantity'] = coffee.quantity
    stock_df.to_csv("p2.csv", index=False)
    print("Coffee beans has been saved,New qty: {coffee.quantity} kg")