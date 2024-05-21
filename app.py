from flask import Flask, render_template, jsonify, request, send_file
import pandas as pd
from datetime import datetime
from converting_msg import Converter
from io import BytesIO
import os

app = Flask(__name__)

# Initialize DataFrame
data = {'Number': list(range(1, 101)), 'Price': [0] * 100}
df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_message():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        message = data.get('message', '')
        working = Converter.convert(message)
        for price, lst in working.items():
            price = int(price) if not isinstance(price, int) else price
            lst = [int(item) if not isinstance(item, int) else item for item in lst]
            df.loc[df['Number'].isin(lst), 'Price'] += price
        sumation = sum(df['Price'])
        reshaped_df = df.values.reshape(10, 10, 2)
        matrix = [[f"{cell[0]}   [{cell[1]}]" for cell in row] for row in reshaped_df]
        table_df = pd.DataFrame(matrix)
        table_html = table_df.to_html(classes='table table-striped table-bordered table-hover', index=False, header=False)
        return jsonify(table=table_html, sum=f'Total amount: {sumation}')
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/reset')
def reset_table():
    global df
    df['Price'] = 0
    reshaped_df = df.values.reshape(10, 10, 2)
    matrix = [[f"{cell[0]}  \n  [{cell[1]}]" for cell in row] for row in reshaped_df]
    table_df = pd.DataFrame(matrix)
    table_html = table_df.to_html(classes='table table-striped table-bordered table-hover', index=False, header=False)
    return jsonify(table=table_html, sum=f'Total amount: 0')

@app.route('/option/<value>')
def update_option(value):
    current_datetime = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    return jsonify(option=f'{value} \t\t {current_datetime}')

@app.route('/download', methods=['POST'])
def download_image():
    file = request.files['image']
    file.save('table.png')
    return send_file('table.png', mimetype='image/png', as_attachment=True, attachment_filename='table.png')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
