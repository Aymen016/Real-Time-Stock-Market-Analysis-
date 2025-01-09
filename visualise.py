import pandas as pd
import boto3
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# AWS S3 configuration
s3 = boto3.client('s3')
bucket_name = 'kafka-stock-market12'
file_key = 'indexProcessed.csv'

# Download data from S3
response = s3.get_object(Bucket=bucket_name, Key=file_key)
data = pd.read_csv(StringIO(response['Body'].read().decode('utf-8')))

# Initial Data Exploration
print("First few rows of the dataset:\n", data.head())
print("\nMissing values:\n", data.isnull().sum())
print("\nSummary Statistics:\n", data.describe())

# Data Cleaning
data = data.dropna()  # Drop rows with missing values
data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime
data = data.sort_values(by='date')  # Sort by date

# Analysis
# Calculate Moving Averages
data['5-day MA'] = data['close'].rolling(window=5).mean()
data['10-day MA'] = data['close'].rolling(window=10).mean()

# Plot Closing Price Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['close'], label='Closing Price')
plt.plot(data['date'], data['5-day MA'], label='5-Day Moving Average')
plt.plot(data['date'], data['10-day MA'], label='10-Day Moving Average')
plt.legend()
plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Top Gainers and Losers
data['daily_change'] = data['close'] - data['open']
top_gainers = data.nlargest(5, 'daily_change')
top_losers = data.nsmallest(5, 'daily_change')

print("\nTop Gainers:\n", top_gainers[['date', 'symbol', 'daily_change']])
print("\nTop Losers:\n", top_losers[['date', 'symbol', 'daily_change']])

# Volatility Analysis
data['volatility'] = (data['high'] - data['low']) / data['open']
high_volatility_days = data.nlargest(5, 'volatility')
print("\nHigh Volatility Days:\n", high_volatility_days[['date', 'symbol', 'volatility']])

# Save Processed Data Back to S3
processed_file = 'processed_data.csv'
data.to_csv(processed_file, index=False)
s3.upload_file(processed_file, bucket_name, 'processed_data.csv')
print("\nProcessed data uploaded back to S3.")
