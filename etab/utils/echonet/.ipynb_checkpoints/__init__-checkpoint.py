"""
The echonet package contains code for loading echocardiogram videos, and
functions for training and testing segmentation and ejection fraction
prediction models.
"""

import click

from etab.utils.echonet.__version__ import __version__
from etab.utils.echonet.config import CONFIG as config
import etab.utils.echonet.datasets as datasets
import etab.utils.echonet.utils as utils


@click.group()
def main():
    """Entry point for command line interface."""


del click


main.add_command(utils.segmentation.run)
main.add_command(utils.video.run)

__all__ = ["__version__", "config", "datasets", "main", "utils"]
