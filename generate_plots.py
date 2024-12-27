import os
import pandas as pd
import matplotlib.pyplot as plt
import openai

class PlotGenerator:
    def __init__(self, csv_file, llm_api_key):
        self.csv_file = csv_file
        self.llm_api_key = llm_api_key
        self.plots_folder = "plots"

        # Create the plots folder if it doesn't exist
        if not os.path.exists(self.plots_folder):
            os.makedirs(self.plots_folder)

    def generate_plots(self):
        # Read the CSV file
        try:
            data = pd.read_csv(self.csv_file, parse_dates=["date"])
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

        # Plot 1: Calorie Intake vs. Burned Calories
        self.plot_calories(data)

        # Plot 2: Net Calories Over Time
        self.plot_net_calories(data)

        # Plot 3: Strain vs. Recovery (Scatter Plot)
        self.plot_strain_vs_recovery(data)

        # Plot 4: Caloric Surplus/Deficit (Bar Chart)
        self.plot_calorie_surplus_deficit(data)

        print("All plots generated and saved in the 'plots' folder.")

    def plot_calories(self, data):
        plt.figure(figsize=(10, 6))
        plt.bar(data['date'], data['calories_consumed'], label="Calories Consumed", alpha=0.7, color='blue')
        plt.bar(data['date'], data['calories_burned'], label="Calories Burned", alpha=0.7, color='green')
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.title("Calories Consumed vs. Burned")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_folder, "calories_intake_vs_burned.jpeg"))
        plt.close()

    def plot_net_calories(self, data):
        data['net_calories'] = data['calories_consumed'] - data['calories_burned']
        plt.figure(figsize=(10, 6))
        plt.plot(data['date'], data['net_calories'], marker='o', color='purple')
        plt.xlabel("Date")
        plt.ylabel("Net Calories")
        plt.title("Net Calories Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_folder, "net_calories_over_time.jpeg"))
        plt.close()

    def plot_strain_vs_recovery(self, data):
        plt.figure(figsize=(10, 6))
        plt.scatter(data['strain'], data['recovery'], color='orange')
        plt.xlabel("Strain Level")
        plt.ylabel("Recovery Percentage")
        plt.title("Strain vs. Recovery")
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_folder, "strain_vs_recovery.jpeg"))
        plt.close()

    def plot_calorie_surplus_deficit(self, data):
        data['calorie_deficit_surplus'] = data['calories_consumed'] - data['calories_burned']
        plt.figure(figsize=(10, 6))
        plt.bar(data['date'], data['calorie_deficit_surplus'], color='red', alpha=0.7)
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("Date")
        plt.ylabel("Calories (Surplus/Deficit)")
        plt.title("Calorie Surplus/Deficit Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.plots_folder, "calorie_surplus_deficit.jpeg"))
        plt.close()

    def interpret_plots(self):
        insights = []
        for plot_file in os.listdir(self.plots_folder):
            if plot_file.endswith(".jpeg"):
                file_path = os.path.join(self.plots_folder, plot_file)
                insights.append(self.query_gpt_vision(file_path))
        return insights

    def query_gpt_vision(self, image_path):
        openai.api_key = self.llm_api_key
        try:
            with open(image_path, "rb") as image_file:
                response = openai.Image.create_edit(
                    image=image_file,
                    prompt="Provide detailed insights based on this fitness plot.",
                    n=1,
                    size="1024x1024"
                )
                return response["choices"][0]["text"].strip()
        except Exception as e:
            return f"Error interpreting plot {image_path}: {str(e)}"

# Main execution
if __name__ == "__main__":
    csv_file = "daily_data.csv"  # Ensure this file exists in the same directory
    llm_api_key = "your_openai_api_key"  # Replace with your OpenAI GPT API key

    plot_gen = PlotGenerator(csv_file, llm_api_key)
    plot_gen.generate_plots()

    print("\nInterpreting plots using GPT-Vision...")
    insights = plot_gen.interpret_plots()
    for i, insight in enumerate(insights, 1):
        print(f"\nInsight {i}:\n{insight}")
