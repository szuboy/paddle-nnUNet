# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jeremy.zhang(szujeremy@gmail.com, Shenzhen University, China)

from paddlennunet.utilities.file_and_folder_operations import *
from multiprocessing import Pool

from paddlennunet.configuration import default_num_threads
from paddlennunet.paths import nnUNet_raw_data, nnUNet_cropped_data
import numpy as np
import pickle
from paddlennunet.preprocessing.cropping import get_patient_identifiers_from_cropped_files
from skimage.morphology import label
from collections import OrderedDict


class DatasetAnalyzer(object):
    pass
