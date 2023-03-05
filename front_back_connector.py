import pandas as pd


SHEET_ID = '1PSCh90qzY_J5tPNp5khMniMs9y-y5I-1th_OFkBlcI0'
SHEET_NAME = 'SAINS_DATA'

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

df = pd.read_csv(url)

print(df.head())
print (df.values[1])
print(df.columns[1])
print(df.at[4, 'customer_name'])

def sheet_deconstructor(user_ident):
    print(df.at[user_ident, 'customer_name'])
    user_name = df.at[user_ident, 'customer_name']
    user_user = df.at[user_ident, 'user_user']
    user_pass = df.at[user_ident, 'user_pass']
    has_debit = df.at[user_ident, 'has_debit']
    has_credit = df.at[user_ident, 'has_credit']
    has_savings = df.at[user_ident, 'has_savings']
    savings_val = df.at[user_ident, 'savings_val']
    total_points = df.at[user_ident, 'total_points']

    return user_name, user_user, user_pass, has_debit, has_credit, has_savings, savings_val, total_points

def table_height():
    print(len(df.index))
    to_return = len(df.index)
    return to_return

def table_to_list():

    return df.values.tolist()


def num_of_rows():
    return table_to_list().len()




