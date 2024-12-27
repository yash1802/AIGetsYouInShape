import csv
from datetime import datetime
import os

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
        
        # Define the file name
        file_name = "daily_data.csv"
        
        # Check if the file exists, create it with headers if not
        file_exists = os.path.exists(file_name)
        if not file_exists:
            with open(file_name, mode="w", newline='') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["date", "calories_consumed", "calories_burned", "net_calories", "calorie_goal_met", "strain", "recovery_percentage"])
        
        # Append the data to the file
        with open(file_name, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, calories_consumed, calories_burned, net_calories, calorie_goal_met, strain, recovery_percentage])
