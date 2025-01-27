Creating a program like the Eco-Footprint-Tracker involves several components: collecting input from the user about their daily habits, calculating the carbon footprint based on those inputs, and visualizing the information. Below is a basic Python program that performs these tasks. The program uses matplotlib for visualization and assumes certain carbon emission factors for different activities like transportation, energy consumption, and diet.

```python
import matplotlib.pyplot as plt

# Constants for carbon emission factors per unit of activity.
CAR_EMISSIONS = {
    'car': 0.25,  # kg CO2 per km
    'bus': 0.05,  # kg CO2 per km
    'train': 0.04, # kg CO2 per km
    'plane': 0.15, # kg CO2 per km
}

ENERGY_EMISSIONS = {
    'electricity': 0.233,  # kg CO2 per kWh
    'gas': 2.0,            # kg CO2 per cubic meter
}

DIET_EMISSIONS = {
    'meat': 7.2,   # kg CO2 per day
    'vegetarian': 3.8, # kg CO2 per day
    'vegan': 2.9,  # kg CO2 per day
}

def get_user_data():
    """
    Collects user input for daily activities.
    """
    try:
        km_by_car = float(input("Enter kilometers traveled by car: "))
        km_by_bus = float(input("Enter kilometers traveled by bus: "))
        km_by_train = float(input("Enter kilometers traveled by train: "))
        km_by_plane = float(input("Enter kilometers traveled by plane: "))
        kwh_electricity = float(input("Enter daily electricity consumption in kWh: "))
        m3_gas = float(input("Enter daily gas consumption in cubic meters: "))
        
        print("Select your diet type:")
        print("1. Meat-based")
        print("2. Vegetarian")
        print("3. Vegan")
        diet_choice = int(input("Enter the number corresponding to your diet choice: "))
        
        diet_type = 'meat' if diet_choice == 1 else 'vegetarian' if diet_choice == 2 else 'vegan'

        return {
            'car': km_by_car,
            'bus': km_by_bus,
            'train': km_by_train,
            'plane': km_by_plane,
            'electricity': kwh_electricity,
            'gas': m3_gas,
            'diet': diet_type
        }
    except ValueError as e:
        print("Invalid input. Please enter numeric values for distances and consumption.")
        return None

def calculate_carbon_footprint(data):
    """
    Calculates the carbon footprint based on the user's daily activities.
    """
    if data is None:
        return None

    try:
        travel_emissions = (
            data['car'] * CAR_EMISSIONS['car'] +
            data['bus'] * CAR_EMISSIONS['bus'] +
            data['train'] * CAR_EMISSIONS['train'] +
            data['plane'] * CAR_EMISSIONS['plane']
        )
        energy_emissions = (
            data['electricity'] * ENERGY_EMISSIONS['electricity'] +
            data['gas'] * ENERGY_EMISSIONS['gas']
        )
        diet_emissions = DIET_EMISSIONS[data['diet']]

        total_emissions = travel_emissions + energy_emissions + diet_emissions

        return travel_emissions, energy_emissions, diet_emissions, total_emissions
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        return None

def visualize_results(results):
    """
    Generates a pie chart showing the carbon footprint distribution.
    """
    if results is None:
        print("No results to display.")
        return

    labels = ['Travel', 'Energy', 'Diet']
    sizes = [results[0], results[1], results[2]]
    explode = (0.1, 0, 0)  # explode the first slice for emphasis

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Your Daily Carbon Footprint")
    plt.show()

def main():
    user_data = get_user_data()
    if user_data:
        results = calculate_carbon_footprint(user_data)
        if results:
            print(f"Total carbon emissions: {results[3]:.2f} kg CO2 per day.")
            visualize_results(results)

if __name__ == "__main__":
    main()
```

### Key Features:
- **Error Handling:** The program handles ValueError during user input and general exceptions during calculations.
- **Input Validation:** Prompts the user for numeric values and uses simple diet selection through menu choices.
- **Visualization:** Uses `matplotlib` to create a pie chart that visualizes carbon footprint distribution among travel, energy, and diet.
- **Extensibility:** You can easily extend the program by adding more categories or integrating more precise emission factors.

### Note:
You'll need to have `matplotlib` installed to run this program. You can install it using pip:

```bash
pip install matplotlib
```

This was a simplified approach to track daily carbon footprint. For a more precise and personalized calculation, it might be necessary to account for more activities and use more detailed emission factors.