from twilio.rest import Client

class EduAlertSystem:
    def __init__(self, sid, token, twilio_num):
        self.client = Client(sid, token)
        self.from_num = twilio_num

    def notify_absence(self, parent_phone, student_name):
        # Interactive Message
        twiml = f"""
        <Response>
            <Say voice="Polly.Russell" language="en-GB">
                Greeting from the School Office. This is an automated alert to inform you that {student_name} was marked absent today. 
                Press 1 to acknowledge this message, or 0 to speak with the administrator later.
            </Say>
            <Gather numDigits="1" action="/log-response" method="POST" />
        </Response>
        """
        return self.client.calls.create(twiml=twiml, to=parent_phone, from_=self.from_num)
