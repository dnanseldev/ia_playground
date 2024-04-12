FROM python:3.11.9
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN python -m pip install \
--upgrade \
--pre \
--index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple \
--extra-index-url https://pypi.org/simple \
matplotlib
#CMD ["python", "src/app.py"]
