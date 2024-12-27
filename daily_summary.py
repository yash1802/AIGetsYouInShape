import openai

class DailySummary:
    def __init__(self, fitness_data, food_data, metrics, llm_api_key):
        self.fitness_data = fitness_data
        self.food_data = food_data
        self.metrics = metrics
        self.llm_api_key = llm_api_key

    def generate_summary(self):
        # Calculate key metrics from fetched data
        calories_consumed = self.food_data["calories_consumed"]
        calories_burned = self.fitness_data["calories_burned"]
        net_calories = calories_consumed - calories_burned
        calorie_goal = self.metrics["target_calorie_intake"]
        calorie_goal_met = self.calculate_calorie_goal_status(calories_consumed, calorie_goal)
        exercise_types = ', '.join(self.fitness_data["exercises"])
        strain = self.fitness_data["strain"]
        recovery_percentage = self.fitness_data["recovery"]
        exercise_goal_met = self.calculate_exercise_goal_status(strain)
        
        # Generate the prompt for the LLM (using the data dynamically)
        prompt = f"""
        You are a fitness coach summarizing the day's fitness and nutrition for a user. Based on the following data, generate a summary with appropriate recommendations:

        - Calories consumed today: {calories_consumed}
        - Calories burned today: {calories_burned}
        - Net daily calorie intake: {net_calories}
        - Target daily calorie goal: {calorie_goal}
        - The user has {calorie_goal_met} their calorie goal by {abs(calories_consumed - calorie_goal)} calories.
        - Exercises performed: {exercise_types}
        - Strain: {strain}
        - Recovery percentage: {recovery_percentage}
        
        The summary should follow this format:

        "Today, you consumed <> calories and burnt <> calories, making your net daily calorie intake <>. Thus, you have <met/overshot/undershot> your target daily calorie goal by <>. 
        You performed the following exercises: <exercise types> and put <stress type> stress on yourself, which considering your recovery rate of <recovery percentage>, was/was not a good decision.

        I recommend a <light/moderate/heavy> workout tomorrow and eat <recommend specific food items>. This is because <rationale: recovery percentage, calorie deficit/surplus, nutrient needs, or long-term fitness goals>."

        Provide recommendations based on the calorie deficit or surplus, recovery percentage, and long-term fitness goals.
        """

        # Send prompt to LLM for summary generation
        return self.query_llm(prompt)

    def calculate_calorie_goal_status(self, calories_consumed, calorie_goal):
        if calories_consumed == calorie_goal:
            return "met"
        elif calories_consumed > calorie_goal:
            return "overshot"
        else:
            return "undershot"
        
    def calculate_exercise_goal_status(self, strain):
        if strain >= 14:
            return "met"
        else:
            return "not met"

    def query_llm(self, prompt):
        openai.api_key = self.llm_api_key
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # or whichever model you'd like to use
                prompt=prompt,
                max_tokens=200,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error generating summary: {str(e)}"
