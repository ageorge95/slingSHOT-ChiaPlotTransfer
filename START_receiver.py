from pyFTT._01_pyFTT import pyFTT
from pyFTT._00_pFTT_base import configure_logger
from threading import Thread

configure_logger()

do = pyFTT(wd_path=r'C:\Users\g4m3rx\OneDrive\pyFTT',
           receiver_torrent_save_folder=r'H:\\')
Thread(target=do.thread_monitor_receiver).start()