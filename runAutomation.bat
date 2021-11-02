pip install -r requirements
set YYYYMMDD=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%
set HHMMSS=%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%
python -m pytest --html=./log/%YYYYMMDD%%HHMMSS%-report.html --self-contained-html -n 4