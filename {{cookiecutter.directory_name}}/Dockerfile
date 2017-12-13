FROM ubuntu:16.04

# Shell Setup
SHELL ["/bin/bash", "-c"]
ENV LANG C.UTF-8

# Install Base OS Packages
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -q \
    && apt-get install -q -y --no-install-recommends \
    	apt-utils \
        ca-certificates \
        python3 \
        python3-pip \
        python3-setuptools \
    && pip3 install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


ADD . /opt/app
RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

CMD [ "python3", "/opt/app/{{cookiecutter.main_file}}.py" ]
