# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data (replace with your actual data)
data = {
    'City': ['Munich', 'Stuttgart', 'Frankfurt', 'Hamburg', 'Berlin', 'Leipzig'],
    'CurrentYield': [5.0, 4.5, 4.8, 5.2, 5.1, 4.7],
    'TargetYield': [5.5, 4.9, 5.3, 5.5, 5.4, 5.0],
    'Priority': [1, 2, 1, 2, 3, 3],
    'PriceAdvantage': [50000, -20000, 10000, -5000, 20000, -10000],
    'StrategicScore': [29, 26, 24, 22, 22, 17]
}
df = pd.DataFrame(data)

# Streamlit Layout
st.title("Real Estate Investment Dashboard")

# --- Yield Comparison ---
st.subheader("Current Yield vs Target Yield Comparison")
fig1, ax1 = plt.subplots()
scatter = ax1.scatter(df["CurrentYield"], df["TargetYield"], s=(100 / df["Priority"])*10, alpha=0.7, color="green", edgecolor='black')
ax1.axline((0, 0), slope=1, color='red', linestyle='--')
ax1.set_xlabel("Current Yield (%)")
ax1.set_ylabel("Target Yield (%)")
st.pyplot(fig1)

# --- Price Advantage Analysis ---
st.subheader("Price Advantage / Discrepancy Analysis")
fig2, ax2 = plt.subplots()
bars = ax2.bar(df["City"], df["PriceAdvantage"], color='skyblue', edgecolor='black')
ax2.axhline(0, color='red', linestyle='--')
ax2.set_xlabel("City")
ax2.set_ylabel("Price Advantage (€)")
st.pyplot(fig2)

# --- Strategic City Scoring ---
st.subheader("Strategic City Scoring (Total Score)")
fig3, ax3 = plt.subplots()
sns.barplot(x=df["City"], y=df["StrategicScore"], palette='viridis', ax=ax3)
ax3.set_xlabel("City")
ax3.set_ylabel("Total Score")
st.pyplot(fig3)

# --- Geographical Map Placeholder ---
st.subheader("Geographical Distribution of Key Cities")
st.map(df[['City', 'Priority']])  # This is a placeholder. Replace with actual coordinates for cities.
st.write("Map is a placeholder. Please replace with actual latitude/longitude data.")
