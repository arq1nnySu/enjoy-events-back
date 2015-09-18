import os

from api import app, EVENTS
from model.event import Event
import services.userService
import services.eventService

if __name__ == '__main__':
    EVENTS.update({
        "1": Event({'id': "1", 'name': 'Choripateada'}),
        "2": Event({'id': "2", 'name': 'WISIT'}),
        "3": Event({'id': "3", 'name': 'Lollapalooza'}),
    })
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
