def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")
    
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Determine BMI category
    category = bmi_category(bmi)
    
    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()
