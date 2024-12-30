from flask import Flask, render_template
import pandas as pd
import jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/policies')
def policies():
    return render_template('policies.html')
    
@app.route('/api/housing_data')
def housing_data():
    data = pd.read_json('data/housing_data.json')
    return jsonify(data.to_dict(orient="records"))

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/impact')
def impact():
    return render_template('impact.html')

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')

@app.route('/join-movement')
def join_movement():
    return render_template('join_movement.html')

if __name__ == '__main__':
    app.run(debug=True)
