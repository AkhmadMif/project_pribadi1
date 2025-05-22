#Sumber data kaggle
#link: https://www.kaggle.com/datasets/ihelon/coffee-sales?select=index_1.csv

import pandas as pd


# Ganti nama file CSV dan output Excel sesuai kebutuhan
csv_file = 'index_2.csv'
excel_file = 'index_2.xlsx'

# Baca file CSV
df = pd.read_csv(csv_file)

# Simpan sebagai Excel
df.to_excel(excel_file, index=False)

print("CSV berhasil dikonversi ke Excel!")