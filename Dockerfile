FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
        pip install --upgrade pip && \
        pip install -r /requirements.txt && \
        apk del .tmp && \
        chmod +x /scripts/* && \
        adduser -D user

WORKDIR /app
USER user

CMD ["entrypoint.sh"]
