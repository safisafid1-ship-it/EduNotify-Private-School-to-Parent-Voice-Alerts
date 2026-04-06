from flask import Flask, request, jsonify
from voice_engine import EduAlertSystem

app = Flask(__name__)
notif_system = EduAlertSystem('ACxxx', 'TOKENxxx', '+123456')

@app.route('/notify-parent', methods=['POST'])
def notify():
    data = request.json
    # Send notification logic
    sid = notif_system.notify_absence(data['phone'], data['student'])
    return jsonify({"status": "Alert Sent", "call_id": sid})

if __name__ == '__main__':
    app.run(debug=True)
