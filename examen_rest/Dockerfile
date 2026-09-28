FROM python:3.12-slim

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=120 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    i=0; \
    until pip install --retries 5 -r requirements.txt; do \
      i=$((i+1)); \
      if [ "$i" -ge 8 ]; then exit 1; fi; \
      echo "Reintento ${i}..."; \
      sleep 2; \
    done

COPY . .

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8000"]
