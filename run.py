#!/usr/bin/env python3.5
from application.app import app

import application.routes # noqa

if __name__ == '__main__':
    app.run()
