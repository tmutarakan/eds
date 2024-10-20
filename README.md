# electronic digital signature
export PYTHONPATH=$PWD/src
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install poetry
poetry install