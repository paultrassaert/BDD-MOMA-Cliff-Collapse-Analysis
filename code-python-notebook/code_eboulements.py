import pandas as pd

# Chargement du fichier
df = pd.read_excel(r"C:\Users\kweez\Documents\IMT\Projet command entreprise\eboulements_propre.xlsx")

# Conversion en numérique
df["annee_dig"] = pd.to_numeric(df["annee_dig"], errors="coerce")

# Définition des périodes
bins = [1994, 2000, 2008, 2012, 2015, 2019, 2022]
labels = ["1995–2000", "2001–2008", "2009–2012", "2013–2015", "2016–2019", "2020–2022"]

# Attribution des périodes
df["periode"] = pd.cut(df["annee_dig"], bins=bins, labels=labels, right=True)

# Comptage des éboulements par période et par cellule 
compte = df.groupby(["cell_6", "periode"]).size().unstack(fill_value=0)

print(compte)




