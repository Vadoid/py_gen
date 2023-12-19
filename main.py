from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# Function to generate random data and create a DataFrame
def generate_dataframe():
    data = {
        'Field1': np.random.randint(1, 100, 10),
        'Field2': np.random.rand(10),
        'Field3': np.random.choice(['A', 'B', 'C'], 10),
        'Field4': np.random.choice([True, False], 10)
    }
    df = pd.DataFrame(data)
    return df

# Route to display the DataFrame on the web page
@app.route('/')
def display_dataframe():
    df = generate_dataframe()
    return render_template('index.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
