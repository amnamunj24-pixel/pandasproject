import pandas as pd

class RescuePet:

    def __init__(self, name, species, age):

        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True

df1 = pd.read_csv("p3.csv")

df2 = pd.read_csv("p3.csv")

# Combine

df = pd.concat([df1, df2], ignore_index=True)

# Clean

df = df.dropna()

# Filter dogs

dogs = df[df["Animal_Type"] == "Dog"]

# Pick one dog

dog_row = dogs.iloc[0]

pet = RescuePet(dog_row["Pet_Name"], dog_row["Animal_Type"], dog_row["Age_Years"])

pet.process_adoption()

# Save adopted pet

adopted_data = pd.DataFrame([{

    "Pet_Name": pet.name,

    "Animal_Type": pet.species,

    "Age_Years": pet.age,

    "Adopted": pet.is_adopted

}])

try:

    old = pd.read_csv("successful_adoptions.csv")

    final = pd.concat([old, adopted_data], ignore_index=True)

except FileNotFoundError:

    final = adopted_data

final.to_csv("successful_adoptions.csv", index=False)