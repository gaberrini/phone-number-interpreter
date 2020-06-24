FROM python:3.8

COPY phone_number_interpreter /phone_number_interpreter

ENTRYPOINT [ "python", "-m", "phone_number_interpreter" ]
