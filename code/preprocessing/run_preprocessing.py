#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runs the specified collection of preprocessing steps
"""

import argparse, csv, pickle
from ast import literal_eval
import pandas as pd
from sklearn.pipeline import make_pipeline
from code.preprocessing.punctuation_remover import PunctuationRemover
from code.preprocessing.tokenizer import Tokenizer
from code.util import COLUMN_TWEET, SUFFIX_TOKENIZED


def main():
    # setting up CLI
    parser = argparse.ArgumentParser(description = "Various preprocessing steps")
    parser.add_argument("input_file", help = "path to the input csv file")
    parser.add_argument("output_file", help = "path to the output csv file")
    parser.add_argument("-p", "--punctuation", action = "store_true", help = "remove punctuation")
    parser.add_argument("-t", "--tokenize", action = "store_true", help = "tokenize given column into individual words")
    parser.add_argument("--tokenize_input", help = "input column to tokenize", default = COLUMN_TWEET)
    parser.add_argument("-e", "--export_file", help = "create a pipeline and export to the given location", default = None)
    args = parser.parse_args()

    # load data
    df = pd.read_csv(args.input_file, quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

    df["mentions"] = df["mentions"].apply(literal_eval)
    df["mentions_count"] = df["mentions"].str.len()
    df = df.drop(columns=["mentions"])

    drop_cols = [
        "id", "conversation_id", "created_at", "timezone", "user_id", "name", "place",
        "replies_count", "retweets_count", "likes_count",
        # "cashtag" only few records have this filled. Might be useless
        # always the same value for all records
        "retweet", "near","geo","source","user_rt_id","user_rt","retweet_id",
        "retweet_date","translate","trans_src"
        # "trans_dest" for some reason there is a line break in the csv after "trans_dest
        # therefore the column cannot be removed without extra effort
    ]

    # TODO filter by language
    # drop language column

    df = df.drop(columns=drop_cols)

    # collect all preprocessors
    preprocessors = []
    if args.punctuation:
        preprocessors.append(PunctuationRemover())
    if args.tokenize:
        preprocessors.append(Tokenizer(args.tokenize_input, args.tokenize_input + SUFFIX_TOKENIZED))

    # call all preprocessing steps
    for preprocessor in preprocessors:
        df = preprocessor.fit_transform(df)

    # store the results
    df.to_csv(args.output_file, index = False, quoting = csv.QUOTE_NONNUMERIC, line_terminator = "\n")

    # create a pipeline if necessary and store it as pickle file
    if args.export_file is not None:
        pipeline = make_pipeline(*preprocessors)
        with open(args.export_file, 'wb') as f_out:
            pickle.dump(pipeline, f_out)


if __name__ == "__main__":
    main()
