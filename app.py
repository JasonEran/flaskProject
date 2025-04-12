from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/convert/<celsius>')
def convert_temperature(celsius):
    try:
        celsius_float = float(celsius)  # Convert string to float
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        # Version 1: Return just the Fahrenheit value
        # return f"{fahrenheit}"
        # Version 2: Return input and result with useful text
        return f"{celsius_float}°C is equal to {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid input: Please provide a valid number for Celsius"

if __name__ == '__main__':
    app.run(debug=True)