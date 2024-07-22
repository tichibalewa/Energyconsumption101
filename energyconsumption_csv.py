import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x = pd.read_csv(r"C:\Users\hopeb\OneDrive\Desktop\Data science\Energy_consumption.csv")
df = pd.read_csv(r"C:\Users\hopeb\OneDrive\Desktop\Data science\Energy_consumption.csv")
#print(df.head(1000))


# Descriptive statistics for numerical columns
#print(df[['Temperature', 'Humidity', 'SquareFootage', 'Occupancy', 'RenewableEnergy', 'EnergyConsumption']].describe())

# Compute correlation matrix
correlations = df[['Temperature', 'Humidity', 'SquareFootage', 'Occupancy', 'RenewableEnergy', 'EnergyConsumption']].corr()
# Print correlations with EnergyConsumption
#print(correlations['EnergyConsumption'].sort_values(ascending=False))

# Average energy consumption by HVACUsage
hvac_energy = df.groupby('HVACUsage')['EnergyConsumption'].mean()
#print(hvac_energy)

# Average energy consumption by LightingUsage
lighting_energy = df.groupby('LightingUsage')['EnergyConsumption'].mean()
#print(lighting_energy)

# Average energy consumption by DayOfWeek
day_energy = df.groupby('DayOfWeek')['EnergyConsumption'].mean()
#print(day_energy)

# Average energy consumption by Holiday
holiday_energy = df.groupby('Holiday')['EnergyConsumption'].mean()
#print(holiday_energy)



# HVAC Usage vs Energy Consumption
plt.scatter(df['HVACUsage'], df['EnergyConsumption'], marker='o', linestyle='-')
plt.xlabel('HVACUsage')
plt.ylabel('EnergyConsumption')


plt.title('Energy Consumption by HVAC Usage')
plt.show()


# Lighting Usage vs Energy Consumption
plt.hist(df['LightingUsage'],df['EnergyConsumption'],marker='o', linestyle='-')
plt.xlabel('LightingUsage')
plt.ylabel('EnergyConsumption')


plt.title('Energy Consumption by Lighting Usage')
plt.show()

# Day of Week vs Energy Consumption
plt.plot(df['DayOfWeek'],df['EnergyConsumption'],marker='o', linestyle='-')
plt.xlabel('DayOfWeek')
plt.ylabel('EnergyConsumption')


plt.title('Energy Consumption by Day of Week')
plt.show()

# Holiday vs Energy Consumption
plt.plot(df['Holiday'],df['EnergyConsumption'], marker='o', linestyle='-')
plt.xlabel('Holiday')
plt.ylabel('EnergyConsumption')


plt.title('Energy Consumption by Holiday')
plt.show()
