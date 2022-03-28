from flask import Flask, request, jsonify
import util

app = Flask('__name__')

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location' : util.get_location_names()
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/home_price_predict', methods=['POST'])
def home_price_predict():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    print(location)
    
    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, sqft, bhk, bath)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

if __name__ == '__main__':
    print('Starting server for Bengaluru Home Price Prdiction')
    app.run()