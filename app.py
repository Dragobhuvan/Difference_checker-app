from flask import Flask, render_template, request
import pandas as pd
from io import StringIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare_csv_files():
    # Retrieve the file paths from the request form
    text1 = request.form['text1']
    text2 = request.form['text2']

    # if 'file1' not in request.files or 'file2' not in request.files:
    #     return "Error: Please upload both files."

    file1 = StringIO(text1)
    file2 = StringIO(text2)
    # Read the CSV files into Pandas DataFrames
    df1 = pd.read_csv(file1, sep='\t')
    df2 = pd.read_csv(file2, sep='\t')

    # print(df1)
    # print("----------")
    # print(df2)

    # Compare the two sheets
    diff = pd.concat([df1, df2]).drop_duplicates()

    # print("-----------------------")
    # print(diff)

    # Prepare the differences as a string
    if not diff.empty:
        differences = diff.to_string(index=False)
    else:
        differences = "No differences found between the two sheets."

    # Render the template with the differences
    return render_template('results.html', differences=differences)

if __name__ == '__main__':
    app.run(debug=True)


