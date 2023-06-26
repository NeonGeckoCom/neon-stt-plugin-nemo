# NeonAI Nemo STT Plugin 
[Mycroft](https://mycroft-ai.gitbook.io/docs/mycroft-technologies/mycroft-core/plugins) compatible
Neon Nemo STT Plugin Speech-to-Text.

## Configuration:
```yaml
stt:
    module: neon_stt_plugin_nemo 
    neon-stt-plugin-nemo: {}
```

## Docker Deployment
The dockerfile included in this repository can be used to build a container with
a minimal server that hosts Nemo STT. The below command runs the container and
binds the web UI to port 8080 on the host:

```shell
docker run -p 8080:8080 ghcr.io/neongeckocom/neon-stt-plugin-nemo:dev
```

From the host, a Web UI can be accessed at `127.0.0.1:8080/gradio` and STT
requests can be posted to `127.0.0.1:8080/stt`. Status is available at `127.0.0.1:8080/status`.

The [ovos-stt-plugin-server](https://github.com/OpenVoiceOS/ovos-stt-plugin-server)
STT plugin can be used to send requests to this deployed backend.