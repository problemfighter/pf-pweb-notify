from flask_socketio import SocketIO, Namespace, send, emit
from pf_pweb_notify.pfpn_default_namespace import DefaultNamespace

_websocket = SocketIO()


class PWebNotify:

    @staticmethod
    def init(pweb_app):
        _websocket.init_app(pweb_app)
        PWebNotify.register_namespace(DefaultNamespace("/"))

    @staticmethod
    def register_namespace(namespace: Namespace):
        _websocket.on_namespace(namespace)

    @staticmethod
    def send_data(event, data, namespace: str = None, broadcast: bool = False):
        params = {}
        # return
        if namespace:
            params["namespace"] = namespace
        if broadcast:
            params["broadcast"] = broadcast
        _websocket.emit(event, data, **params)
