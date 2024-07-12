import pandas as pd
import matplotlib.pyplot as plt

# Extract the data from the CSV file
data = pd.read_csv("influenza_data.csv")

# Plot the trend of influenza cases
plt.plot(data['Week'], data['Influenza Type A'], label="Influenza Type A", color='blue')
plt.plot(data['Week'], data['Influenza Type B'], label="Influenza Type B", color='red')
plt.xlabel('Week')
plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels by 90 degrees for better readability

# Limit the x-axis to display a maximum of 13 major tick marks for clearer data presentation
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(13))

plt.ylabel('Number of Cases')
plt.title('Influenza Cases Reported in the US Per Week (2023-24)')
plt.legend()
plt.grid(True)
plt.show()


# Calculate rolling mean and standard deviation
rolling_window = 4
data['Rolling Mean A'] = data['Influenza Type A'].rolling(window=rolling_window).mean()
data['Rolling Std A'] = data['Influenza Type A'].rolling(window=rolling_window).std()

data['Rolling Mean B'] = data['Influenza Type B'].rolling(window=rolling_window).mean()
data['Rolling Std B'] = data['Influenza Type B'].rolling(window=rolling_window).std()

# Plot the data with rolling mean and standard deviation
plt.figure(figsize=(14, 7))

# Influenza Type A
plt.subplot(2, 1, 1)
plt.plot(data['Week'], data['Influenza Type A'], label='Influenza Type A', color='blue', alpha=0.5)
plt.plot(data['Week'], data['Rolling Mean A'], label='Rolling Mean A', color='blue')
plt.fill_between(data['Week'], data['Rolling Mean A'] - data['Rolling Std A'], data['Rolling Mean A'] + data['Rolling Std A'], color='blue', alpha=0.2, label='Rolling Std A')
plt.xlabel('Week')
plt.xticks(rotation=90, ha='right')
plt.ylabel('Number of Cases')
plt.title('Influenza Type A Cases with Rolling Mean and Standard Deviation')
plt.legend()
plt.grid(True)

# Influenza Type B
plt.subplot(2, 1, 2)
plt.plot(data['Week'], data['Influenza Type B'], label='Influenza Type B', color='red', alpha=0.5)
plt.plot(data['Week'], data['Rolling Mean B'], label='Rolling Mean B', color='red')
plt.fill_between(data['Week'], data['Rolling Mean B'] - data['Rolling Std B'], data['Rolling Mean B'] + data['Rolling Std B'], color='red', alpha=0.2, label='Rolling Std B')
plt.xlabel('Week')
plt.xticks(rotation=90, ha='right')
plt.ylabel('Number of Cases')
plt.title('Influenza Type B Cases with Rolling Mean and Standard Deviation')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
