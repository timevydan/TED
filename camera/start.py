from camera import find_faces
from dir_watcher import Watcher
from faces_train import train_faces
from rds_query import connect
import os

connect()
os.system("python3 dir_watcher.py & ")
train_faces()
