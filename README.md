# Python---Sleep-Analysis
Analyzing lifestyle survey data with Python to discover relationships between different life factors and sleep quality.

## Project Overview
This is an extension of a DataCamp project to analyze anonymized lifestyle survey data to uncover key insights about factors that affect sleep quality, duration, and health with Python.

---

## Dataset Information

The data used in this analysis is stored in the file `sleep_health_data.csv`. It contains information from 374 individuals, capturing various metrics averaged over a six-month period.

### Columns Description

| Column                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Person ID                 | An identifier for each individual                                           |
| Gender                    | The gender of the person (Male/Female)                                      |
| Age                       | The age of the person in years                                              |
| Occupation                | The occupation or profession of the person                                  |
| Sleep Duration (hours)    | The average number of hours the person sleeps per day                       |
| Quality of Sleep (scale: 1-10) | A subjective rating of the quality of sleep, from 1 to 10               |
| Physical Activity Level (minutes/day) | Average daily physical activity in minutes                     |
| Stress Level (scale: 1-10) | A subjective stress rating from 1 to 10                                      |
| BMI Category              | BMI classification (e.g., Underweight, Normal, Overweight)                  |
| Blood Pressure (systolic/diastolic) | Average systolic/diastolic blood pressure                            |
| Heart Rate (bpm)          | Average resting heart rate in beats per minute                               |
| Daily Steps               | Average number of steps per day                                              |
| Sleep Disorder            | Presence/absence of sleep disorders (None, Insomnia, Sleep Apnea)            |

---

## Objectives

1. **Identify Occupation Sleep Patterns:**
   - Determine which occupation has the lowest average sleep duration.
   - Identify the occupation with the lowest average sleep quality.
   - Assess if the same occupation has both the lowest duration and quality.

2. **BMI and Sleep Disorder Insights:**
   - Calculate insomnia ratios by BMI category.
   - Store results in the dictionary `bmi_insomnia_ratios`.

---

## Analysis

### The Code
The following code was used to find the main objectives results:
```python
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
```
### Output:
```bash
The occupation with lowest average sleep is: Sales Representative
The occupation with lowest average sleep quality is: Sales Representative

The occupation with lowest average sleep is the same as the occupation with lowest average sleep quality: True

The insomnia ratio for normal BMI is 0.04
The insomnia ratio for overweight BMI is 0.43
The insomnia ratio for obese BMI is 0.4
```

## Data Visualizations

This project incorporates the following visual elements to enrich the data analysis:

1. **Bar Charts:**
   - Average sleep duration and sleep quality by occupation.

2. **Scatter Plot:**
   - Physical activity vs. sleep duration to explore potential correlations.

3. **Heatmap:**
   - Stress level and sleep quality relationship displayed using a gradient.

4. **Pie Charts:**
   - Distribution of sleep disorders by BMI category, displayed side by side.

---

## Technologies Used
- **Python**
- **Pandas**: Data manipulation
- **Matplotlib**: Visualization
- **Seaborn**: Advanced visualization

---

## Key Findings
- Occupation X (TBD from dataset) had the lowest sleep duration, while Occupation Y (TBD) had the poorest sleep quality.
- Insightful visualizations demonstrated strong relationships between physical activity and sleep, as well as correlations between BMI categories and sleep disorders.

