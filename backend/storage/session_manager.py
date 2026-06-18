import uuid


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "dataset": None,
            "df_json": None,
            "schema": None,
            "analytics": None,
            "report": None,
            "chat_history": [],
        }

        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def save_analysis(self, session_id, data):
        if session_id in self.sessions:
            self.sessions[session_id].update(data)

    def add_message(self, session_id, role, message):
        if session_id in self.sessions:
            self.sessions[session_id]["chat_history"].append(
                {"role": role, "content": message}
            )


session_manager = SessionManager()
