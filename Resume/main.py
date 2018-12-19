import sys
sys.path.append("python_files")

from app import app
from index import *
from education import *
from research import *


if __name__ == "__main__":
    app.run(debug=True)
