import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Total AdWords Earnings\\dataset\\google_adwords_earnings.xlsx')
df1=df.groupby('business_type')['adwords_earnings'].sum()
df2=df.pivot_table(
    index=None,
    columns='business_type',
    values='adwords_earnings',
    aggfunc='sum'
)

print(df1.sort_values(ascending=True))
print(df2)