from flask_socketio import SocketIO, Namespace, send

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
    def send_data(data, namespace: str = None, broadcast: bool = False):
        params = {}
        if namespace:
            params["namespace"] = namespace
        if broadcast:
            params["broadcast"] = broadcast
        send(data, **params)
