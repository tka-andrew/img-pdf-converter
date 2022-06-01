FROM ubuntu:20.04

# Needed for Ubuntu installation
ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=Etc/UTC

# Install necessary packages
# The binutlis and python3-dev are needed for pyinstaller
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        pip  \
        python3.7 \
        python3-tk \
        binutils \
        python3-dev

RUN mkdir -p /src/img-pdf-converter/

WORKDIR /src
COPY requirements.txt .
RUN pip install pip
RUN pip install --default-timeout=10 --no-cache-dir -r requirements.txt

WORKDIR /src/img-pdf-converter

# REFERENCE: https://unix.stackexchange.com/questions/230238/x-applications-warn-couldnt-connect-to-accessibility-bus-on-stderr
ENV NO_AT_BRIDGE=1

CMD ["bash"]