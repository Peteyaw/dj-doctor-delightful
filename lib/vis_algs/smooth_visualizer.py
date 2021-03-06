import numpy as np

from vis_algs import smoothing_utils
from vis_algs import vis_alg_base
import utils


class Visualizer(vis_alg_base.VisualizationAlgorithm):

    def freq_to_hex(self, freq):

        self.log_time()

        sigma = 8

        amplitudes_gauss = smoothing_utils.gaussian_smooth(
                freq, self.nlights, sigma)

        assert len(amplitudes_gauss) == self.nlights
        assert all(not np.isnan(a) for a in amplitudes_gauss)

        normed_amplitudes = self.norm_amplitudes(amplitudes_gauss)

        final_hex_vals = []
        for i in range(self.nlights):

            hue = float(i) / self.nlights
            sat = 1.0
            val = utils.convex_poly_ramp(
                    normed_amplitudes[i], d=4)

            final_hex_vals.append(utils.hsv_to_hex(hue, sat, val))

        return final_hex_vals
