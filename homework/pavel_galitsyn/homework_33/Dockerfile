FROM python
COPY site_checker.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "site_checker.py"]