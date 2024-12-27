import requests

class FitnessData:
    def __init__(self, whoop_api_token):
        self.api_token = whoop_api_token
        self.base_url = "https://api.whoop.com"

    def get_fitness_data(self):
        headers = {"Authorization": f"Bearer {self.api_token}"}
        # Fetch daily activity summary
        response = requests.get(f"{self.base_url}/v1/user/metrics/daily", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                "calories_burned": data["caloriesBurned"],
                "exercises": [activity["name"] for activity in data["activities"]],
                "strain": data["strainLevel"],
                "recovery": data["recoveryScore"]
            }
        else:
            raise ValueError("Error fetching fitness data from Whoop API.")
