import os
import cv2 as cv
import argparse

import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from PIL import Image

def get_argparser():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--data_root", type=str, default='data', 
                        help='path to dataset')
    parser.add_argument("--dataset_ver", type=str, default='211018', 
                        help='version of dataset folder')
    
    return parser
    
def main():
    
    '''
    < sample image >
    2110108/Raw data with gray/Mild_1_HT
    2110108/Raw data with mask/Mild_1_HT_mask
    
    TIFF, (871, 498), L (8-bit pixels, black and white)
    '''
    
    opts = get_argparser().parse_args()
    
    rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    print(' (1) Current working directory: {}'.format(rootDir))
    if not os.path.exists(rootDir):
        raise FileNotFoundError
    
    dataDir = os.path.join(rootDir, opts.data_root, opts.dataset_ver)
    print(' (2) Dataset directory: {}'.format(dataDir))
    if not os.path.exists(dataDir):
        raise FileNotFoundError
    
    dstDir = os.path.join(rootDir, 'output')
    print(' (3) Output directory: {}'.format(dstDir))
    if not os.path.exists(dstDir):
        raise FileNotFoundError
    
    sampleIM = Image.open(os.path.join(dataDir, 'Raw data with gray', 'Mild_1_HT.tif'))
    sampleMASK = Image.open(os.path.join(dataDir, 'Raw data with mask', 'Mild_1_HT_mask.tif'))
    
    print(sampleIM.format, sampleIM.size, sampleIM.mode)
    print(sampleMASK.format, sampleMASK.size, sampleMASK.mode)
    
    sampleIM = cv.imread(os.path.join(dataDir, 'Raw data with gray', 'Mild_1_HT.tif'))
    cv.imshow('sample image', sampleIM)
    cv.waitKey()
    cv.destroyAllWindows()
    
if __name__ == "__main__":
    main()