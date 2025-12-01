---
layout: default
title: Audio transcription
parent: 17 Today-I-Learned
grand_parent: Lab Management
nav_order: 1
---

# Audio transcription

Transcribe audio with whisper

```
docker run --rm \
  -v "$PWD":/data \
  ghcr.io/ggerganov/whisper.cpp:latest \
  ./main -f /data/input_audio.mp3 -otxt -l en
```