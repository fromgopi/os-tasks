#pylint: disable=missing-final-newline,pointless-string-statement
""" Flask context entry point """
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    """Main Method
    """
    app.run(host='0.0.0.0', port=os.getenv('PORT'))