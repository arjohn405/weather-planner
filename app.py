from flask import Flask, request, jsonify
from flask_cors import CORS
from activity_planner import ActivityPlanner

app = Flask(__name__)
CORS(app)

planner = ActivityPlanner()

@app.route('/api/plan-activity', methods=['POST'])
def plan_activity():
    data = request.json
    result = planner.plan_activity(
        activity=data['activity'],
        date_time_str=data['dateTime'],
        people_count=data['peopleCount']
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 