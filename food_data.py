import requests

class FoodData:
    def __init__(self, fatsecret_api_key, fatsecret_api_secret):
        self.api_key = fatsecret_api_key
        self.api_secret = fatsecret_api_secret
        self.base_url = "https://platform.fatsecret.com/rest/v2.0"

    def get_food_data(self):
        # Request user input for consumed food items
        food_input = input("Enter the foods you consumed today (comma-separated): ")
        food_items = [item.strip() for item in food_input.split(",")]
        total_calories = 0

        # Fetch calorie information for each food item
        for food in food_items:
            calories = self.fetch_calories(food)
            if calories is not None:
                total_calories += calories

        return {"calories_consumed": total_calories}

    def fetch_calories(self, food_item):
        # Authenticate with FatSecret API
        auth_response = requests.post(
            "https://oauth.fatsecret.com/connect/token",
            data={"grant_type": "client_credentials"},
            auth=(self.api_key, self.api_secret)
        )
        if auth_response.status_code != 200:
            raise ValueError("Error authenticating with FatSecret API.")
        
        access_token = auth_response.json()["access_token"]

        # Search for food and retrieve calorie details
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"method": "foods.search", "search_expression": food_item, "format": "json"}
        response = requests.get(self.base_url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            foods = data.get("foods", {}).get("food", [])
            if foods:
                return int(foods[0].get("food_description", "").split(" ")[0])  # Calories in description
        return None
