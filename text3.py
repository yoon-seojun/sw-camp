import pandas as pd
file_path = "Mars_Base_Inventory_List (1).csv"
df = pd.read_csv(file_path)
data_list = [df.columns.tolist()] + df.values.tolist()
print(data_list)

df_sorted = df.sort_values(by="인화성", ascending=False)
data_list = [df_sorted.columns.tolist()] + df_sorted.values.tolist()
print(data_list)

flammable_df = df[df["인화성"] >= 0.7]
flammable_list = [flammable_df.columns.tolist()] + flammable_df.values.tolist()
print("인화성 0.7 이상 목록:")
print(flammable_list)

flammable_df.to_csv("Mars_Base_Inventory_danger.csv", index=False)