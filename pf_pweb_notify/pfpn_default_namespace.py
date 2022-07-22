from flask_socketio import Namespace


class DefaultNamespace(Namespace):

    def on_connect(self):
        print("Connected")

    def on_disconnect(self):
        print("Disconnected")

    def on_data(self, data):
        print(data)
