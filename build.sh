# Build:
PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.7.3
pyenv virtualenv 3.7.3 3.7.3-eqsoundtrigge
pyenv local 3.7.3-eqsoundtrigger
pip install -r requirements.txt
pip install py2app
py2applet -r zapsplat_emergency_alarm_siren_011_26617.mp3 --make-setup main.py
rm -rf build dist
python setup.py py2app

# Execute:
./dist/main.app/Contents/MacOS/main

