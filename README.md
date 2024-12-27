## AI Gets You In Shape.

This project is a fitness tracking and analysis tool that integrates fitness and food data with advanced AI capabilities. It helps users gain a detailed daily summary of their fitness progress and provides actionable insights by analyzing visual data through GPT-Vision.

### Features
	1.	Daily Summary Generation:
	•	Fetches fitness data from Whoop and food data from FatSecret APIs.
	•	Summarizes calories consumed, calories burned, exercises performed, and recovery data using OpenAI’s GPT model.
	2.	Plot Generation and Analysis:
	•	Creates insightful plots from the daily data stored in daily_data.csv.
	•	Uses GPT-Vision API to analyze the plots and provide recommendations.
	3.	Customizable Metrics:
	•	Users can set target calorie intake and exercise strain goals through user_data.txt.

### Dependencies
openai, pandas, matplotlib: **pip install openai pandas matplotlib**

### File Structure
	•	main.py: Main script for generating daily fitness summaries.
	•	generate_plots.py: Script for generating plots and interpreting them.
	•	daily_summary.py: Handles summary creation logic.
	•	logging_utils.py: Provides logging functionality.
	•	fitness_data.py: Fetches fitness data from Whoop.
	•	food_data.py: Fetches food data from FatSecret.
	•	metrics.py: Reads user-defined metrics from user_data.txt.
	•	daily_data.csv: Stores daily fitness data (used by generate_plots.py).

 ### User Instructions

1. Generating the Daily Summary
To generate a daily fitness summary:
	1.	Ensure your Whoop and FatSecret API credentials are correctly added in main.py.
	2.	Open user_data.txt to customize your target metrics (e.g., calorie intake goal).
	3.	Run the following command: **python main.py**

 Output: A detailed daily summary displayed in the terminal. 

 Example: 
 *Today, you consumed 2000 calories and burned 800 calories, making your net daily calorie intake 1400. Thus, you have undershot your target daily calorie goal by 100.
 You performed the following exercises: Running, Weightlifting and put moderate stress on yourself, which considering your recovery rate of 75%, was a good decision.
 I recommend a moderate workout tomorrow and eat more protein-rich foods as well as complex carbohydrates like chicken or brown rice. 
 This is because your recovery rate is high and you have a small calorie deficit to balance.*

2. Generating and Analyzing Plots
To generate visual plots and get AI insights:
	1.	Ensure daily_data.csv is updated with your latest fitness data.
	•	File should include columns: date, calories_consumed, calories_burned, strain, recovery.
	2.	Run the following command: **python generate_plots.py**

  The script will: 

	•	Generate the following plots and save them in a folder called plots:
	•	Calories Consumed vs. Burned (Bar Chart)
	•	Net Calories Over Time (Line Plot)
	•	Strain vs. Recovery (Scatter Plot)
	•	Calorie Surplus/Deficit (Bar Chart)
	•	Use GPT-Vision API to analyze each plot and print insights in the terminal.


