import sys
sys.path.append("python_files")

from app import app
from index import *
from education import *
from research import *
from athletics import *
from volunteering import *


if __name__ == "__main__":
    app.run(debug=True)
