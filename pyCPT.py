from pyFTT._01_pyFTT import pyFTT
from os import listdir,\
    path
from subprocess import call
from time import sleep

class pyCPT(pyFTT):

    def __init__(self,
                 wd_path: str,
                 plotting_full_CLI_command: str,
                 plotting_wd: str,
                 plots_cache : int = 1,
                 sender_torrent_file_folder : str = None,
                 receiver_torrent_save_folder : str = None,
                 qbHost : str = 'localhost',
                 qbPort : int = 8085,
                 qbPassword : str = 'admin',
                 qbUsername : str = 'adminadmin',
                 max_plots : int = None
                 ):

        super(pyCPT, self).__init__(wd_path = wd_path,
                                     sender_torrent_file_folder = sender_torrent_file_folder,
                                     receiver_torrent_save_folder = receiver_torrent_save_folder,
                                     qbHost = qbHost,
                                     qbPort = qbPort,
                                     qbPassword = qbPassword,
                                     qbUsername = qbUsername)

        self.plotting_full_CLI_command = plotting_full_CLI_command
        self.plots_cache = plots_cache
        self.plotting_wd = plotting_wd
        self.max_plots = max_plots

    def thread_monitor_plotter(self):
        current_plot = 0
        while True:
            # check existing plots addition to the transfer list
            for potential_file in listdir(self.plotting_wd):
                if potential_file.endswith('.plot'):
                    if not potential_file in listdir(self.wd_path):
                        self.sender_torrent_file_folder = path.join(self.plotting_wd, potential_file)
                        self.create_torrent()

            # check if new plots can be created
            if len(list(filter(lambda x: x.endswith('.plot'), listdir(self.plotting_wd)))) >= self.plots_cache:
                self._log.info('Cache already full. Waiting for ongoing transfers ...')
            else:
                self._log.info('Cache free for more entries. Begining plotting ...')
                call(self.plotting_full_CLI_command)
                current_plot += 1

            sleep(5)

            if self.max_plots and current_plot == self.max_plots:
                self._log.info('Reached the max limit of plots. Exiting ...')
                break