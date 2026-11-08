import pandas as pd 
import numpy as np

drugs = {
    "Name" : ["Compound_A","Compound_B","Compound_C","Compound_D","Compound_E","Compound_F"],
    "Molecular_weight" : [342, 180, 520, 289, 410, 156],
    "Solubility" : [0.8, 0.9, 0.3, 0.7, 0.5, 0.95],
    "Toxicity" : [0.1, 0.05, 0.8, 0.2, 0.4, 0.02],
    "Activity" : [0.9, 0.5, 0.95, 0.75, 0.5, 0.4]
}

df = pd.DataFrame(drugs)
df["MW_pass"] = df["Molecular_weight"] < 500
df["Sol_pass"] = df["Solubility"] > 0.4
df["Tox_pass"] = df["Toxicity"] < 0.3
df["Act_pass"] = df["Activity"]  > 0.6

df["Rule_pass"] = (df["MW_pass"].astype(int) +
                df["Sol_pass"].astype(int) +
                df["Tox_pass"].astype(int) +
                df["Act_pass"].astype(int))

conditions = [df["Rule_pass"] == 4,
             df["Rule_pass"] == 3,
             df["Rule_pass"] == 2]

choices = ["Excellent candidate", "Good candidate", "Weak candidate"]
df["Classification"] = np.select(conditions,choices,default="Rejected")
print(df[["Name", "Rule_pass", "Classification"]])
print("\nBest Candidate:\n")
Best_candidate = df[df["Classification"] == "Excellent candidate"][["Name", "Toxicity", "Activity"]]
print(Best_candidate)