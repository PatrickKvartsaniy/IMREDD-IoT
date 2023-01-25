FROM python:3.10.2-slim

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip

RUN pip install --root-user-action=ignore --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python", "main.py"]