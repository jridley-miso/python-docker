FROM python:3.11
LABEL authors="jridley"
ADD .env .
ADD python_docker.py .
RUN pip install python-dotenv
CMD ["python", "./python_docker.py"]