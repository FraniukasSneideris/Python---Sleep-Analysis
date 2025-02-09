import pandas as pd

# Reading the data
df = pd.read_csv('sleep_health_data.csv')

# Getting the occupation with lowest average sleep duration
lowest_avg_sleep = df.groupby('Occupation')['Sleep Duration'].mean()
lowest_sleep_occ = lowest_avg_sleep.sort_values().index[0] 

# Getting the occupation with lowest average quality of sleep
lowest_sleep_quality = df.groupby('Occupation')['Quality of Sleep'].mean()
lowest_sleep_quality_occ = lowest_sleep_quality.sort_values().index[0]

print(f'The occupation with lowest average sleep is: {lowest_sleep_occ}')
print(f'The occupation with lowest average sleep quality is: {lowest_sleep_quality_occ}\n')

# Comparing occupation with lowest average sleep duration and lowest quality of sleep
def compare_occupation(occ1, occ2):
    if occ1 == occ2:
        same_occ = True
    else:
        same_occ = False
    
    return same_occ

same_occ = compare_occupation(lowest_sleep_quality_occ, lowest_sleep_occ)

print(f'The occupation with lowest average sleep is the same as the occupation with lowest average sleep quality: {same_occ}\n')

# BMI and insomnia:
def calculate_insomnia_ratios(df, bmi_categories):
    ratios = {}
    for bmi in bmi_categories:
        total = len(df[df['BMI Category'] == bmi])
        insomnia_cases = len(df[(df['BMI Category'] == bmi) & (df['Sleep Disorder'] == 'Insomnia')])
        ratios[bmi] = round(insomnia_cases / total, 2) 
    return ratios

bmi_categories = ['Normal', 'Overweight', 'Obese']
bmi_insomnia_ratios = calculate_insomnia_ratios(df, bmi_categories)

print(f"The insomnia ratio for normal BMI is {bmi_insomnia_ratios['Normal']}")
print(f"The insomnia ratio for overweight BMI is {bmi_insomnia_ratios['Overweight']}")
print(f"The insomnia ratio for obese BMI is {bmi_insomnia_ratios['Obese']}")
