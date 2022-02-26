from pyFTT._01_pyFTT import pyFTT
from os import listdir,\
    path
from subprocess import call
from time import sleep
from logging import getLogger

class pyCPT():

    def __init__(self,
                 working_directory: str,
                 plotting_full_CLI_command: str,
                 plotting_wd: str,
                 plots_cache : int = 1,
                 max_plots : int = None
                 ):

        self.working_directory = working_directory
        self.plotting_full_CLI_command = plotting_full_CLI_command
        self.plots_cache = plots_cache
        self.plotting_wd = plotting_wd
        self.max_plots = max_plots

        self._log = getLogger()

    def thread_monitor_plotter(self):
        current_plot = 0
        while True:
            # check existing plots addition to the transfer list
            for potential_file in listdir(self.plotting_wd):
                if potential_file.endswith('.plot'):
                    if not potential_file in listdir(self.working_directory):
                        self._log.info(f"Creating torrent for { potential_file } ...")
                        self.sender_torrent_file_folder = path.join(self.plotting_wd, potential_file)
                        do = pyFTT(working_directory=self.working_directory,
                                   file_or_folder_to_send=self.sender_torrent_file_folder)
                        do.create_torrent()

            # check if new plots can be created
            if len(list(filter(lambda x: x.endswith('.plot'), listdir(self.plotting_wd)))) >= self.plots_cache:
                self._log.info('Cache already full. Waiting for ongoing transfers ...')
            else:
                if self.max_plots and current_plot == self.max_plots:
                    self._log.info('Reached the max limit of plots. Not plotting anymore ...')
                else:
                    self._log.info('Cache free for more entries. Beginning plotting ...')
                call(self.plotting_full_CLI_command)
                current_plot += 1

            sleep(5)
