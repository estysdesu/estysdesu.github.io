from flask_frozen import Freezer
from mySite import mySiteApp

freezer = Freezer(mySiteApp)

if __name__ == '__main__':
    freezer.freeze()
