import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Sleep Duration and Quality of Sleep by Occupation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

data1 = pd.DataFrame({'Occupation': df['Occupation'], 'Sleep Duration': df['Sleep Duration']})
sns.barplot(x='Occupation', y='Sleep Duration', data=data1, ax=ax1)
ax1.set_title('Sleep Duration by Occupation')
ax1.tick_params(axis='x', rotation=90)

data2 = pd.DataFrame({'Occupation': df['Occupation'], 'Quality of Sleep': df['Quality of Sleep']})
sns.barplot(x='Occupation', y='Quality of Sleep', data=data2, ax=ax2)
ax2.set_title('Quality of Sleep by Occupation')
ax2.tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()


# Sleep Disorders by BMI Category
sleep_disorders = df.groupby('BMI Category')['Sleep Disorder'].value_counts().unstack().fillna(0)

bmi_categories = ['Normal', 'Overweight', 'Obese']

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for i, bmi in enumerate(bmi_categories):
    disorder_counts = sleep_disorders.loc[bmi]
    axes[i].pie(disorder_counts, labels=disorder_counts.index, autopct='%1.1f%%', 
                 colors=['salmon', 'lightgreen', 'skyblue'])
    axes[i].set_title(f'Sleep Disorders for {bmi} BMI Category')

plt.tight_layout()
plt.show()


# Stress Level vs. Quality of Sleep
heatmap_data = df.pivot_table(values='Quality of Sleep', 
                               index='Stress Level', 
                               aggfunc='mean')

plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap='Blues', fmt=".1f")
plt.title('Stress Level vs. Sleep Quality')
plt.show()


# Sleep Duration and Quality of Sleep by Gender and BMI Category
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

data1 = pd.DataFrame({'Gender': df['Gender'], 'Sleep Duration': df['Sleep Duration']})
sns.barplot(x='Gender', y='Sleep Duration', data=data1, ax=ax1)
ax1.set_title('Sleep Duration by Gender')
ax1.tick_params(axis='x', rotation=90)

data2 = pd.DataFrame({'Gender': df['Gender'], 'Quality of Sleep': df['Quality of Sleep']})
sns.barplot(x='Gender', y='Quality of Sleep', data=data2, ax=ax2)
ax2.set_title('Quality of Sleep by Gender')
ax2.tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()
