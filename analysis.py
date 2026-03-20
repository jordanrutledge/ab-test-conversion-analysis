import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
import numpy as np

df = pd.read_csv('ab_data.csv')
countries = pd.read_csv('countries.csv')

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nSample:\n", df.head())
print("\nConversion rate by group:\n", df.groupby('group')['converted'].mean())

df = df[((df['group'] == 'control') & (df['landing_page'] == 'old_page')) |
        ((df['group'] == 'treatment') & (df['landing_page'] == 'new_page'))]

df = df.drop_duplicates(subset='user_id')

control = df[df['group'] == 'control']['converted']
treatment = df[df['group'] == 'treatment']['converted']

control_rate = control.mean()
treatment_rate = treatment.mean()
lift = treatment_rate - control_rate

n_control = len(control)
n_treatment = len(treatment)

count = np.array([treatment.sum(), control.sum()])
nobs = np.array([n_treatment, n_control])

z_stat, p_value = proportions_ztest(count, nobs)

print("\n── A/B Test Results ──────────────────────────────")
print(f"Control conversion rate:   {control_rate:.4f} ({control_rate*100:.2f}%)")
print(f"Treatment conversion rate: {treatment_rate:.4f} ({treatment_rate*100:.2f}%)")
print(f"Lift:                      {lift*100:.4f}%")
print(f"Z-statistic:               {z_stat:.4f}")
print(f"P-value:                   {p_value:.4f}")
print(f"Significant (p < 0.05):    {p_value < 0.05}")

results = pd.DataFrame({
    'group': ['control', 'treatment'],
    'users': [n_control, n_treatment],
    'conversions': [control.sum(), treatment.sum()],
    'conversion_rate': [control_rate, treatment_rate]
})
results.to_csv('ab_results.csv', index=False)
print("\nExported ab_results.csv")

df_geo = df.merge(countries, on='user_id', how='left')
geo_summary = df_geo.groupby('country')['converted'].agg(['sum','count','mean']).reset_index()
geo_summary.columns = ['country', 'conversions', 'users', 'conversion_rate']
geo_summary.to_csv('ab_results_by_country.csv', index=False)
print("Exported ab_results_by_country.csv")