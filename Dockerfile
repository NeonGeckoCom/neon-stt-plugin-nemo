FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    gcc \
    g++

COPY . /tmp/neon-stt-plugin-nemo
RUN pip install wheel cython && \
    pip install \
    /tmp/neon-stt-plugin-nemo/[docker] --extra-index-url https://download.pytorch.org/whl/cpu

ENTRYPOINT ovos-stt-server --engine neon-stt-plugin-nemo --gradio \
--title "NeonAI Nemo STT Plugin" \
--description "Perform fast STT without a GPU using NVIDIA NeMo" \
--info "more info at [Neon Nemo STT Plugin](https://github.com/NeonGeckoCom/neon-stt-plugin-nemo)"