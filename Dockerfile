FROM python:3.8
WORKDIR /
COPY . /
#ENV PYTHONPATH "${PYTHONPATH}:/"
RUN apt-get update
RUN apt-get install -y poppler-utils
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip3 install --timeout 0 -r /requirements.txt
#RUN pip install flask gunicorn
RUN chmod 744 /run.sh
EXPOSE 7000
CMD /run.sh

