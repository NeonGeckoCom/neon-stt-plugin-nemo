
FROM debian:buster-slim

RUN apt-get update && \
    apt-get install -y git python3 python3-dev python3-pip curl build-essential cmake

RUN pip3 install numpy
RUN pip3 install git+https://github.com/openvoiceos/ovos-plugin-manager.git@8101a0c9ae494be2f3a3eab4f98b2a3f2400a245
RUN pip3 install ovos-utils==0.0.25
RUN pip3 install ovos-stt-http-server==0.0.2a1
RUN pip3 install git+https://github.com/NeonGeckoCom/streaming-stt-nemo.git@26570448cd97f6787730a5ea0639eb49e59f09ca
RUN pip3 install SpeechRecognition

COPY . /tmp/neon-stt-plugin-nemo
RUN pip3 install /tmp/neon-stt-plugin-nemo

ENTRYPOINT ovos-stt-server --engine ovos-stt-plugin-nemo

