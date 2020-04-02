#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from moviepy.editor import *

video = VideoFileClip('/tmp/jd02.mp4')
audio = video.audio
audio.write_audiofile('/tmp/jd02.mp3')
