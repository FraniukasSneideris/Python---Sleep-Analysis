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
bmi_categories = ['Normal', 'Overweight', 'Obese']

fig, axes = plt.subplots(3, 2, figsize=(14, 15))
fig.suptitle("Sleep Data by BMI Categories", fontsize=16)

for i, bmi in enumerate(bmi_categories):
    # Data by BMI category
    bmi_data = df[df['BMI Category'] == bmi]
    
    # Plot Sleep Duration by Gender
    sns.barplot(
        x='Gender', y='Sleep Duration', data=bmi_data, ax=axes[i, 0]
    )
    axes[i, 0].set_title(f'Sleep Duration ({bmi} BMI)')
    axes[i, 0].tick_params(axis='x', rotation=90)
    
    # Plot Quality of Sleep by Gender
    sns.barplot(
        x='Gender', y='Quality of Sleep', data=bmi_data, ax=axes[i, 1]
    )
    axes[i, 1].set_title(f'Quality of Sleep ({bmi} BMI)')
    axes[i, 1].tick_params(axis='x', rotation=90)

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust to fit titles
plt.show()
