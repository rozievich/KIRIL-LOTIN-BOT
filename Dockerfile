FROM python:3.11-alpine
LABEL authors="Rozievich"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /apps
COPY . /apps

RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirement.txt
RUN sed -i 's/\r$//g' /apps/entrypoint.sh
RUN chmod +x /apps/entrypoint.sh

ENTRYPOINT ["/apps/entrypoint.sh"]
