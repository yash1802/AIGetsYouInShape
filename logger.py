import csv
from datetime import datetime

class Logger:
    def __init__(self, fitness_data, food_data, metrics):
        self.fitness_data = fitness_data
        self.food_data = food_data
        self.metrics = metrics

    def log_data(self):
        # Get current date
        date = datetime.now().strftime("%m/%d/%Y")
        
        # Calculate net calories and calorie goal status
        calories_consumed = self.food_data["calories_consumed"]
        calories_burned = self.fitness_data["calories_burned"]
        net_calories = calories_consumed - calories_burned
        calorie_goal = self.metrics["target_calorie_intake"]
        calorie_goal_met = "Yes" if abs(calories_consumed - calorie_goal) <= 150 else "No"
        strain = self.fitness_data["strain"]
        recovery_percentage = self.fitness_data["recovery"]
        
        # Log the data into daily_data.csv
        with open("daily_data.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, calories_consumed, calories_burned, net_calories, calorie_goal_met, strain, recovery_percentage])
