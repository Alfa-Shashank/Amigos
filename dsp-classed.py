
import os

# Set the path to the Python interpreter that you want to use
python_path = '/home/shashank/dsp1/bin/python3'

# Set the PATH environment variable to include the path to the Python interpreter
os.environ['PATH'] = python_path + os.pathsep + os.environ['PATH']

import stt
import pyaudio
import numpy as np
import time
import signal
import re





DEEPSPEECH_MODEL_DIR = '/home/shashank/stt-models'
MODEL_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'model.tflite')
SCORER_FILE_PATH = os.path.join(DEEPSPEECH_MODEL_DIR, 'large_vocabulary.scorer')
LM_ALPHA = 0.75
LM_BETA = 1.85
BEAM_WIDTH = 500

model = stt.Model(MODEL_FILE_PATH)
model.enableExternalScorer(SCORER_FILE_PATH)
model.setScorerAlphaBeta(LM_ALPHA, LM_BETA)
model.setBeamWidth(BEAM_WIDTH)

stt_stream = model.createStream()


def timeout_handler(signum, frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(5)


# Encapsulate DeepSpeech audio feeding into a callback for PyAudio
text_so_far = ''
def process_audio(in_data, frame_count, time_info, status):
    global text_so_far
    data16 = np.frombuffer(in_data, dtype=np.int16)
    stt_stream.feedAudioContent(data16)
    text = stt_stream.intermediateDecode()
    if text != text_so_far:
        # print('Interim text = {}'.format(text[len(text_so_far)+1:]))
        text_so_far = text
    
    return (in_data, pyaudio.paContinue)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1024

# Feed audio to deepspeech in a callback to PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK_SIZE,
    stream_callback=process_audio
)

print('Please start speaking')
stream.start_stream()

# try: 
#     while stream.is_active():
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     # PyAudio
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#     print('Finished recording.')
#     exit(0)
#     # DeepSpeech
#     # text = stt_stream.finishStream()
#     # print('Final text = {}'.format(text))


try:
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    print(text_so_far)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print('Finished recording.')
    # exit(0)
