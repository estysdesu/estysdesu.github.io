from flask_frozen import Freezer
from flaskApp import estysdesu

freezer = Freezer(estysdesu)

if __name__ == '__main__':
    freezer.freeze()
