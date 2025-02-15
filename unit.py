import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap import Window

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x400")

        # Initialize the UI elements
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the unit converter."""
        # Input field for value
        self.value_var = tk.DoubleVar()
        self.value_entry = ttk.Entry(self.root, textvariable=self.value_var, font=("Arial", 14))
        self.value_entry.grid(row=0, column=1, padx=10, pady=10)

        # Labels
        self.value_label = ttk.Label(self.root, text="Value", font=("Arial", 14))
        self.value_label.grid(row=0, column=0, padx=10, pady=10)

        # Output field for converted value
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.root, text="Converted Value", font=("Arial", 14))
        self.result_label.grid(row=1, column=0, padx=10, pady=10)

        self.result_display = ttk.Label(self.root, textvariable=self.result_var, font=("Arial", 14))
        self.result_display.grid(row=1, column=1, padx=10, pady=10)

        # Dropdown for unit selection
        self.unit_type = ttk.Combobox(self.root, values=["Length", "Mass", "Temperature"], font=("Arial", 12), state="readonly")
        self.unit_type.set("Length")  # Default selection
        self.unit_type.grid(row=2, column=0, padx=10, pady=10)

        # Unit selection (from)
        self.from_unit = ttk.Combobox(self.root, values=[], font=("Arial", 12), state="readonly")
        self.from_unit.grid(row=3, column=0, padx=10, pady=10)

        # Unit selection (to)
        self.to_unit = ttk.Combobox(self.root, values=[], font=("Arial", 12), state="readonly")
        self.to_unit.grid(row=3, column=1, padx=10, pady=10)

        # Update unit selections when unit type changes
        self.unit_type.bind("<<ComboboxSelected>>", self.update_unit_options)
        self.update_unit_options()  # Update on start

        # Convert button
        self.convert_button = ttk.Button(self.root, text="Convert", command=self.convert_units, style="success.TButton")
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_unit_options(self, event=None):
        """Update the unit dropdown options based on the selected unit type."""
        unit_type = self.unit_type.get()

        if unit_type == "Length":
            # Length units: metric and imperial
            self.from_unit.config(values=["Meters", "Centimeters", "Millimeters", "Kilometers", "Inches", "Feet", "Yards"])
            self.to_unit.config(values=["Meters", "Centimeters", "Millimeters", "Kilometers", "Inches", "Feet", "Yards"])
        elif unit_type == "Mass":
            # Mass units: metric and imperial
            self.from_unit.config(values=["Grams", "Kilograms", "Pounds", "Ounces"])
            self.to_unit.config(values=["Grams", "Kilograms", "Pounds", "Ounces"])
        elif unit_type == "Temperature":
            # Temperature units: Celsius and Fahrenheit
            self.from_unit.config(values=["Celsius", "Fahrenheit"])
            self.to_unit.config(values=["Celsius", "Fahrenheit"])

    def convert_units(self):
        """Convert units based on the selected type and units."""
        value = self.value_var.get()
        unit_type = self.unit_type.get()
        from_unit = self.from_unit.get()
        to_unit = self.to_unit.get()

        if unit_type == "Length":
            result = self.convert_length(value, from_unit, to_unit)
        elif unit_type == "Mass":
            result = self.convert_mass(value, from_unit, to_unit)
        elif unit_type == "Temperature":
            result = self.convert_temperature(value, from_unit, to_unit)

        # Display the result
        self.result_var.set(f"{result:.2f}")

    def convert_length(self, value, from_unit, to_unit):
        """Convert between length units."""
        # Length conversion factors
        length_conversions = {
            "Meters": 1,
            "Centimeters": 100,
            "Millimeters": 1000,
            "Kilometers": 0.001,
            "Inches": 39.3701,
            "Feet": 3.28084,
            "Yards": 1.09361
        }

        # Convert the value to meters first
        value_in_meters = value / length_conversions[from_unit]

        # Convert the value in meters to the target unit
        return value_in_meters * length_conversions[to_unit]

    def convert_mass(self, value, from_unit, to_unit):
        """Convert between mass/weight units."""
        # Mass conversion factors (metric and imperial)
        mass_conversions = {
            "Grams": 1,
            "Kilograms": 0.001,
            "Pounds": 0.00220462,
            "Ounces": 0.035274
        }

        # Convert the value to grams first
        value_in_grams = value / mass_conversions[from_unit]

        # Convert the value in grams to the target unit
        return value_in_grams * mass_conversions[to_unit]

    def convert_temperature(self, value, from_unit, to_unit):
        """Convert between temperature units (Celsius ↔ Fahrenheit)."""
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        else:
            return value  # No conversion if both units are the same
def main():
# Create the main window using ttkbootstrap Window class
    root = Window(themename="flatly")  # You can change the theme here
    app = UnitConverterApp(root)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
