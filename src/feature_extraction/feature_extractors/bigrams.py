#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bigram Feature
"""

import ast
import nltk
from src.feature_extraction.feature_extractors.feature_extractor import FeatureExtractor

class BigramFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_bigrams".format(input_column))
    
    def _set_variables(self, inputs):
        
        overall_text = []
        for line in inputs:
            tokens = ast.literal_eval(line.item())
            overall_text += tokens
        
        self._bigrams = nltk.bigrams(overall_text)