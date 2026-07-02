FROM python:3.11-slim
WORKDIR /metatime
COPY TIR/metatime_audit.py TIR/run_audit.py ./
CMD ["python3", "run_audit.py"]
