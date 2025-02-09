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

### Approach
1. **Data Analysis Using GroupBy:**  
   - I used `groupby()` to compute the mean values for sleep duration and sleep quality by occupation.  
   - Then I sorted these averages and selected the occupation with the lowest sleep duration (`lowest_sleep_occ`) and lowest sleep quality (`lowest_sleep_quality_occ`).  

2. **Comparing Occupations:**  
   - I defined a simple `compare_occupation()` function that checks whether the same occupation has the lowest sleep duration and sleep quality, returning a boolean (`same_occ`).  

3. **BMI and Insomnia Ratios:**  
   - I defined a function `calculate_insomnia_ratios()` that iterates over BMI categories (`Normal`, `Overweight`, `Obese`). For each category, it calculates the ratio of individuals diagnosed with insomnia, rounding it to two decimal places.  

### Output:
```bash
The occupation with lowest average sleep is: Sales Representative
The occupation with lowest average sleep quality is: Sales Representative

The occupation with lowest average sleep is the same as the occupation with lowest average sleep quality: True

The insomnia ratio for normal BMI is 0.04
The insomnia ratio for overweight BMI is 0.43
The insomnia ratio for obese BMI is 0.4
```

## Data Visualization
Though the primary objectives results can be obtained without visualization, I decided to go a little bit further and see what a few graphs could tell.
*Please note*: The code for each graph is in the file *'data_visualizations.py'*.

### Sleep Duration and Quality of Sleep by Occupation
![image](https://github.com/user-attachments/assets/215df963-d5b8-4ac0-a83e-c66ad0714fad)
Here we can see that indeed, for the occupations included in this survey, the Sales Representative is the one that has the worst sleep. On the other hand, Engineers seem to be sleeping better. The cause of this remains a mistery, but I would assume this might be related either to economic factors, work-life balance, work circumstances, private circumstances, and a combination of all those.


### Sleep Disorders by BMI Category
![image](https://github.com/user-attachments/assets/0d440737-c405-473a-ac55-c9558f303e70)
Here we can see that subjects with overweight and obesity tend to have some sleep disorder (either insomnia or sleep apnea), with only 5.4% of subjects in the Normal BMI group having a sleep disorder, 87.1% of subjects in the Overweight BMI group, and 100% in the Obese group. This comes as no surprise, since it is widely known that overweight and obesity may change metabolism and/or sleep-wake cycles in such a way that causes sleep quality to deteriorate.


### Stress Level vs. Quality of Sleep
![image](https://github.com/user-attachments/assets/f00d524a-11cb-4f08-94b5-929a24b880bf)
This one is a no-brainer, right? 
It may be even silly to mention this, but if this does not show that the more stress we have, the poorer our quality of sleep (and life) will be, I don't know what will. 


### Sleep Duration and Quality of Sleep by Gender
![image](https://github.com/user-attachments/assets/37271f01-740b-4479-bff6-37ec02dbc825)
For this one is important to show the distribution of males and females in the survey:
```python
count_by_gender = df.groupby('Gender')['Gender'].count()
count_by_gender_bmi = df.groupby(['Gender', 'BMI Category'])['Gender'].count()
```
```bash
Gender
Female    185
Male      189
Name: Gender, dtype: int64

Gender  BMI Category
Female  Normal           78
        Obese             1
        Overweight      106
Male    Normal          138
        Obese             9
        Overweight       42
Name: Gender, dtype: int64
```
We can see that the gender distribution is practically 50/50. For some reason, the proportion of overweight females is 250% higher than the proportion of overweight males.
However, if we look at the graphs, we can see that despite the BMI Category, females tend to sleep a bit more and have a better quality of sleep. 

This is a very interesting observation.. The reasons might vary, and of course the data is limited and small, but this might be related to stress-management, and metabolic and hormonal factors: females generally report longer sleep and better sleep quality, potentially linked to differences in stress management or health awareness, and also females often require more sleep due to hormone regulation, as estrogen and progesterone production depend on sufficient rest, unlike testosterone, which isn't as sleep-dependent.

---

## Conclusion
Though the data is limited and small, this analysis provided valuable insights into how various lifestyle factors affect sleep duration and quality. 

Key findings include:  
- **Occupation Impact:** Sales Representatives had the lowest average sleep duration and quality, suggesting potential work-life balance or stress issues affecting sleep.  
- **BMI and Sleep Disorders:** Overweight and obese individuals exhibited significantly higher rates of sleep disorders, aligning with established research on the metabolic and hormonal effects of excess body weight on sleep.  
- **Stress and Sleep Quality:** A clear negative correlation between stress levels and sleep quality confirmed the well-known impact of stress on overall sleep health.  
- **Gender Differences:** Despite a higher proportion of overweight females, women generally reported better and longer sleep than men. This may be linked to hormonal regulation, where estrogen and progesterone require adequate rest, unlike testosterone, and also to stress management or health-awareness.  

These results emphasize the complex interactions between health, stress, lifestyle, and sleep, underscoring the importance of tailored interventions to promote better sleep and overall well-being.

---

## Technologies Used
- **Python**
- **Pandas**: Data manipulation
- **Matplotlib**: Visualization
- **Seaborn**: Advanced visualization

