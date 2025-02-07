import pandas as pd
import matplotlib.pyplot as plt

class FitnessTracker:
    def __init__(self):
        self.data = pd.DataFrame(columns=["Date", "Steps", "Calories"])
    def add_entry(self, date, steps, calories):
        new_entry = pd.DataFrame({"Date": [date], "Steps": [steps], "Calories": [calories]})
        self.data = pd.concat([self.data, new_entry], ignore_index=True)
    def view_stats(self):
        print(self.data)
    
    def plot_progress(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        self.data.plot()
        plt.title('Fitness Progress')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.show()
tracker = FitnessTracker()
tracker.add_entry('2023-02-01', 5000, 250)
tracker.add_entry('2023-02-02', 7000, 300)
tracker.add_entry('2024-02-03', 10000, 730)
tracker.view_stats()
tracker.plot_progress()

