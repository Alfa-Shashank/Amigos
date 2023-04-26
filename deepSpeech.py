#! /usr/bin/env python3

# import subprocess

# # subprocess.call(["deactivate"])

# # Replace 'myenv' with the name of your virtual environment
# subprocess.run(['. /home/shashank/dsp1/bin/activate'], shell=True)

# # # Now you can run commands within the virtual environment
# subprocess.run(['python3', '/home/shashank/Speech-To-Text-Scripts/dsp.py'])

# # subprocess.call(['deactivate'])

import subprocess
import os


class dsp:
    def __init__(self):
        # activate virtual environment
        self.venv_path = "/home/shashank/dsp1"
        self.bin_path = os.path.join(self.venv_path, "bin")
        self.env = os.environ.copy()
        self.env["PYTHONPATH"] = self.venv_path
        # self.env["PATH"] = f"{self.bin_path}:{self.env['PATH']}"
        self.env["PATH"] = "{}:{}".format(self.bin_path, self.env['PATH'])

        # run command in subprocess with virtual environment activated
    def start(self):
        subprocess.call(["python3", "/home/shashank/catkin_ws/src/amigos/src/dsp-original.py"], env=self.env)


# import subprocess
# import os

# # activate virtual environment
# venv_path = "/home/shashank/dsp1"
# bin_path = os.path.join(venv_path, "bin")
# env = os.environ.copy()
# env["PYTHONPATH"] = venv_path
# env["PATH"] = f"{bin_path}:{env['PATH']}"

# # run command in subprocess with virtual environment activated
# result = subprocess.run(["python3", "/home/shashank/Speech-To-Text-Scripts/dsp.py"], env=env, stdout=subprocess.PIPE)

# # print output of command
# print(result.stdout)

