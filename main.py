from daily_summary import DailySummary
from fitness_data import FitnessData
from food_data import FoodData
from metrics import Metrics

def main():
    # API keys for FatSecret and Whoop
    fatsecret_api_key = "your_fatsecret_api_key"
    fatsecret_api_secret = "your_fatsecret_api_secret"
    whoop_api_token = "your_whoop_api_token"
    llm_api_key = "your_openai_api_key"

    # Fetch data dynamically from APIs
    fitness_data = FitnessData(whoop_api_token).get_fitness_data()
    food_data = FoodData(fatsecret_api_key, fatsecret_api_secret).get_food_data()
    metrics = Metrics("user_data.txt").get_metrics()

    # Generate and display the LLM-generated summary
    summary = DailySummary(fitness_data, food_data, metrics, llm_api_key).generate_summary()
    print(summary)

if __name__ == "__main__":
    main()
