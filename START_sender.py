from pyFTT._01_pyFTT import pyFTT
from pyFTT._00_pFTT_base import configure_logger
from pyCPT import pyCPT
from threading import Thread

configure_logger()

do = pyFTT(working_directory=r'C:\Users\g4m3rx\OneDrive\pyFTT')
Thread(target=do.thread_monitor_sender).start()

do = pyCPT(working_directory=r'C:\Users\g4m3rx\OneDrive\pyFTT',
           plotting_wd=r'E:\chia_nft_plots_temp',
           plotting_full_CLI_command=r'"C:\Program Files\madMAx43v3r_chia-plotter_win_v0.1.6-chives\chia_plot.exe" -t D:\ -d D:\ -k 29 -x 9699 -r 8 -f <key> -p <key>',
           plots_cache=0)
Thread(target=do.thread_monitor_plotter).start()