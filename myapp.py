from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for cities
city_data = {
    "Calgary": {"engineering": {"likelihood": 0.30, "accommodation": 0.70, "family_support": 0.80},
                "it": {"likelihood": 0.45, "accommodation": 0.70, "family_support": 0.80}},
    "Saint John": {"engineering": {"likelihood": 0.20, "accommodation": 0.65, "family_support": 0.65},
                   "it": {"likelihood": 0.35, "accommodation": 0.65, "family_support": 0.65}},
    "Toronto": {"engineering": {"likelihood": 0.35, "accommodation": 0.60, "family_support": 0.75},
                "it": {"likelihood": 0.50, "accommodation": 0.60, "family_support": 0.75}},
    # Add data for other cities...
}

def calculate_success_percentage(city, job_type, age, family_status):
    data = city_data.get(city, {}).get(job_type, {})
    if age >= 35:
        data["likelihood"] += 0.05
    if family_status == "with_family":
        data["accommodation"] += 0.05
        data["family_support"] += 0.05
    combined_percentage = (data["likelihood"] + data["accommodation"] + data["family_support"]) / 3
    return round(combined_percentage * 100, 2)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    city = data['city']
    job_type = data['jobType']
    age = data['age']
    family_status = data['familyStatus']
    success_percentage = calculate_success_percentage(city, job_type, age, family_status)
    return jsonify({"success_percentage": success_percentage})

if __name__ == '__main__':
    app.run(debug=True)
