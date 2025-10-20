import pandas as pd

filename='EIOPA_RFR_20241231_Term_Structures.xlsx'
sheetname='RFR_spot_no_VA'

df = pd.read_excel(filename, sheet_name=sheetname, skiprows=9, usecols=(1,2), names=['t','Euro'])

df.head(10)