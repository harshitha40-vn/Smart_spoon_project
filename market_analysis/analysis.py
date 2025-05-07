import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv('market_analysis/data.csv')

def plot_preferences(df):
    df['Eat_At_Restaurants'].value_counts().plot(kind='bar', title='Dining Frequency')
    plt.tight_layout()
    plt.savefig('market_analysis/pref_chart.png')

def sodium_impact(df):
    return df[df['Low_Sodium_Diet'] == 'Yes']['Satisfied_With_LowSodium'].value_counts()

def analyze_awareness_interest(df):
    awareness = df['Aware_Of_Tech'].value_counts(normalize=True) * 100
    interest = df['Interested_In_Device'].value_counts(normalize=True) * 100
    return awareness, interest

def summarize_salt_opinion(df):
    return df['Salt_Opinion'].value_counts()
