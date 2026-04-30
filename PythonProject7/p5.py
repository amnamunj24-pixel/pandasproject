# price_adjuster.py
import pandas as pd

class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        discount_amount = self.price * (percent_off / 100)
        self.price = round(self.price - discount_amount, 2)

df = pd.read_csv("p5.csv")

# filter for electronics only
electronics = df[df['Category'] == 'Electronics'].copy() # copy to avoid warnings

for idx, row in electronics.iterrows():
    p = Product(row['Product_ID'], row['Price'])
    p.apply_discount(20) # 20% holiday sale
    electronics.at[idx, 'Price'] = p.price # update the df

electronics['Promo_Active'] = "Yes"
electronics.to_excel("holiday_promos.xlsx", index=False)
print("Holiday promos exported to holiday_promos.xlsx")