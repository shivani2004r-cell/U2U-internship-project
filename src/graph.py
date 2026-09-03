import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\ADMIN\U2UInnovate-Project-15\data\raw\RTA Dataset.csv")

# Check weather conditions
print("Weather Conditions:")
print(df["Weather_conditions"].value_counts())

# Weather vs Accident Severity graph
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Weather_conditions",
    hue="Accident_severity"
)

plt.title("Accident Severity by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")

plt.xticks(rotation=45)

plt.tight_layout()

# Save graph
plt.savefig(
    "../reports/figures/weather_vs_severity.png"
)

# Display graph
plt.show()