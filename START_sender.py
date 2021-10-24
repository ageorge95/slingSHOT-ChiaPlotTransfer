from pyFTT._00_pFTT_base import configure_logger
from pyCPT import pyCPT
from threading import Thread

configure_logger()

do = pyCPT(wd_path=r'C:\Users\g4m3rx\OneDrive\pyFTT',
           sender_torrent_file_folder=r'dummy',
           plotting_wd=r'D:\\',
           plotting_full_CLI_command=r'"C:\Program Files\madMAx43v3r_chia-plotter_win_v0.1.6-chives\chia_plot.exe" -t D:\ -d D:\ -k 29 -x 9699 -r 8 -f <key> -p <key>')
Thread(target=do.thread_monitor_plotter).start()
Thread(target=do.thread_monitor_sender).start()