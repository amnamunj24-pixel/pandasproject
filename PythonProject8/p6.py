# delay_analyzer.py
import pandas as pd
import os

class Flight:
    def __init__(self, flight_num, delay_time):
        self.flight_num = flight_num
        self.delay_time = delay_time

    def check_severity(self):
        if 30 < self.delay_time <= 60:
            print(f"WARNING: Flight {self.flight_num} delayed {self.delay_time} minutes")
        elif self.delay_time > 60:
            print(f"SEVERE DELAY: Flight {self.flight_num} delayed {self.delay_time} minutes. Alert ops team!")

df = pd.read_csv("arrivals.csv")
df['Minutes_Delayed'] = df['Minutes_Delayed'].fillna(0)

# find flights delayed more than 30 min
delayed = df[df['Minutes_Delayed'] > 30]

if not delayed.empty:
    # get the most delayed one
    worst_flight_row = delayed.loc[delayed['Minutes_Delayed'].idxmax()]

    f = Flight(worst_flight_row['Flight_Number'], worst_flight_row['Minutes_Delayed'])
    f.check_severity()

    # log it
    log_data = {
        'Flight_Number': [f.flight_num],
        'Airline': [worst_flight_row['Airline']],
        'Minutes_Delayed': [f.delay_time],
        'Date_Logged': [pd.Timestamp.now().strftime('%Y-%m-%d')]
    }
    new_log = pd.DataFrame(log_data)

    if os.path.exists("severe_delays_log.csv"):
        existing_log = pd.read_csv("severe_delays_log.csv")
        updated_log = pd.concat([existing_log, new_log], ignore_index=True)
    else:
        updated_log = new_log

    updated_log.to_csv("severe_delays_log.csv", index=False)
else:
    print("No major delays today")