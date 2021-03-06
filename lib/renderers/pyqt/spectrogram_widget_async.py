import utils

import numpy as np
import pyqtgraph as pg
import pyaudio
from PyQt5 import QtCore, QtGui

import matplotlib.pyplot as plt

class SpectrogramWidget(pg.PlotWidget):

    read_collected = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, spectrum_analyzer, max_freq=22000):
        super(SpectrogramWidget, self).__init__()

        self.max_freq = max_freq

        freqs = spectrum_analyzer.get_freqs()
        nyquist_freq = freqs[-1]
        print('Nyquist freq:', nyquist_freq)
        print('Raw number of freqs:', len(freqs))

        self.crop_index = len(freqs)
        if max_freq < nyquist_freq:
            self.crop_index = int(len(freqs) * max_freq / nyquist_freq)
            freqs = freqs[:self.crop_index]

        print('Max freq:', freqs[-1])
        print('Number of freqs:', len(freqs))

        # Make image
        self.img = pg.ImageItem()
        self.addItem(self.img)

        # Get chunk size and sample rate from spectrum analyzer
        nsamples = spectrum_analyzer.nsamples
        sample_rate = spectrum_analyzer.sample_rate

        # Instantiate image array
        self.img_array = np.zeros((150, self.crop_index))

        # Get colormap
        np_cmap = plt.get_cmap('viridis')
        cmap = utils.get_pyqt_cmap(np_cmap)
        lut = cmap.getLookupTable(0.0, 1.0, 256, alpha=False)

        # Set colormap
        self.img.setLookupTable(lut)
        self.img.setLevels([15,60])

        # Setup the correct scaling for y-axis
        yscale = freqs[-1] / self.img_array.shape[1]
        self.img.scale(nsamples / sample_rate, yscale)

        self.setLabel('left', 'Frequency', units='Hz')

        self.show()

    def update(self, chunk):

        spectrum = self.get_spectrum(chunk)[:self.crop_index]

        p10 = np.percentile(spectrum, 10)
        p90 = np.percentile(spectrum, 90)

        print('p10:', p10, '\tp90:', p90, '\t\tmin:', spectrum.min(), '\tmax:', spectrum.max())

        # Roll down one and replace leading edge with new data
        self.img_array = np.roll(self.img_array, -1, 0)
        self.img_array[-1:] = spectrum

        self.img.setImage(self.img_array, autoLevels=False)
