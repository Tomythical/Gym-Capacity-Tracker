import warnings
import pandas as pd
from fbprophet import Prophet

warnings.simplefilter('ignore')

df = pd.read_csv('/Users/ThomasMatheickal/Projects/Gym_Tracking/Data/Capacity_Final.csv')
df.columns = ['ds' , 'y']

# print(df.head())

m = Prophet(interval_width=0.95, daily_seasonality=True)
model = m.fit(df)

future = m.make_future_dataframe(periods =100)
forecast = m.predict(future)
# print(forecast.tail())

plot1 = m.plot(forecast).show()

