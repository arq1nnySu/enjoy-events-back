import os
from api import app
import services.userService
import services.eventService
import services.assistanceService

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
