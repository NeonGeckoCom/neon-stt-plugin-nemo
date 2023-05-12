FROM python:3.9-slim AS compile-image

COPY . /tmp/neon-stt-plugin-nemo

RUN pip install wheel && \
    pip install --user --no-cache-dir \
    /tmp/neon-stt-plugin-nemo/[docker] --extra-index-url https://download.pytorch.org/whl/cpu

# Copy built packages to a clean image to exclude build-time extras from final image
FROM python:3.9-slim AS build-image

COPY --from=compile-image /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg

ENTRYPOINT ovos-stt-server --engine neon-stt-plugin-nemo --gradio \
--title "NeonAI Nemo STT Plugin" \
--description "Perform fast STT without a GPU using NVIDIA NeMo" \
--info "more info at [Neon Nemo STT Plugin](https://github.com/NeonGeckoCom/neon-stt-plugin-nemo)"