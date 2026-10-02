import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

def generate_fitness_plan(age, weight, goal, intensity):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Create 7-day workout plan for Age {age}, Weight {weight}kg, Goal {goal}, Intensity {intensity}"
    response = model.generate_content(prompt)
    return response.text