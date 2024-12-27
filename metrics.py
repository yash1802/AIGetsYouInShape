class Metrics:
    def __init__(self, user_data_file):
        self.user_data_file = user_data_file

    def get_metrics(self):
        with open(self.user_data_file, "r") as file:
            data = {}
            for line in file:
                key, value = line.strip().split(":")
                data[key.lower()] = value.strip()

        weight_pounds = float(data["weight"])
        height_feet, height_inches = map(int, data["height"].split("'"))
        weight_kg = weight_pounds * 0.453592
        height_m = (height_feet * 12 + height_inches) * 0.0254

        bmi = weight_kg / (height_m**2)
        target_weight_kg = float(data["target weight"]) * 0.453592
        bmr = self.calculate_bmr(
            weight_kg,
            height_m,
            int(data["age"]),
            data["gender"].lower()
        )

        target_calories = bmr + (500 if target_weight_kg > weight_kg else -500)

        metrics = {
            "bmi": round(bmi, 2),
            "bmr": round(bmr, 2),
            "target_calories": round(target_calories, 2)
        }

        with open("metrics.txt", "w") as metrics_file:
            for key, value in metrics.items():
                metrics_file.write(f"{key.capitalize()}: {value}\n")

        return metrics

    def calculate_bmr(self, weight, height, age, gender):
        if gender == "male":
            return 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
        else:
            return 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
