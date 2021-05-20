# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jeremy.zhang(szujeremy@gmail.com, Shenzhen University, China)

import SimpleITK as sitk
import numpy as np
import shutil
from paddlennunet.utilities.file_and_folder_operations import *
from multiprocessing import Pool
from collections import OrderedDict


def get_patient_identifiers_from_cropped_files(folder):
    return [i.split("/")[-1][:-4] for i in subfiles(folder, join=True, suffix=".npz")]