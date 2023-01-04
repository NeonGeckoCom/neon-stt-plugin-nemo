# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numpy as np

from streaming_stt_nemo import Model
from ovos_plugin_manager.templates.stt import STT
from ovos_utils.log import LOG
from speech_recognition import AudioData


class NemoSTT(STT):
    default_lang = "en"

    def __init__(self, config: dict = None):
        super().__init__(config)

        self.lang = self.config.get('lang') or self.default_lang
        self.transcriptions = []

        self._engines = {}
        self.cache_engines = self.config.get("cache", True)
        if self.cache_engines:
            self._init_model(self.lang)

    def _init_model(self, language) -> Model:
        language = language or self.lang
        if language not in self._engines:
            model = Model(language)
            if self.cache_engines:
                self._engines[language] = model
        else:
            model = self._engines[language]

        return model


    def execute(self, audio: AudioData, language = None):
        '''
        Executes speach recognition

        Parameters:
                    audio : input audio file path
        Returns:
                    text (str): recognized text
        '''
        model = self._init_model(language)

        audio_buffer = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
        self.transcriptions = model.stt(audio_buffer, audio.sample_rate)

        if not self.transcriptions:
            LOG.info("Transcription is empty")
            self.transcriptions = []
        else:
            LOG.debug("Audio had data")

        return self.transcriptions
