import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3


# 4
def draw_cat_plot():
    # 5
    df_cat = sns.catplot(df, x='variable', y='value', hue='cardio', col='variable', kind='count', height=5, aspect=1)


    # 6
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    

    # 7



    # 8
    fig = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count', height=5, aspect=1).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig