import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Sea Level')

# Linear regression for all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot line of best fit for all data
plt.plot(df['Year'], intercept + slope * df['Year'], color='red', label='Best Fit Line (1880-2014)')

# Linear regression for data since 2000
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Plot line of best fit for recent data
plt.plot(recent_data['Year'], intercept_recent + slope_recent * recent_data['Year'], color='green', label='Best Fit Line (2000-Present)')

# Predict sea level rise in 2050
plt.plot([1880, 2050], [intercept + slope * 1880, intercept + slope * 2050], linestyle='--', color='gray', label='Projection to 2050')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Save and show plot
plt.tight_layout()
plt.savefig('sea_level_prediction.png')
plt.show()
