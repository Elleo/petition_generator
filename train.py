#!/usr/bin/env python3
import gpt_2_simple as gpt2
import os
import requests
import json

TRAINING_STEPS = 1000
MODEL_NAME = "124M"

if not os.path.isdir(os.path.join("models", MODEL_NAME)):
    print(f"Downloading {MODEL_NAME} model...")
    gpt2.download_gpt2(model_name=MODEL_NAME)

output_filename = "petitions.txt"

output = open(output_filename, 'w')

for dirname, subdirs, files in os.walk(os.path.join('uk_petitions_data', 'petitions')):
    print(dirname)
    for filename in files:
        if filename[-5:] == ".json":
            print(filename)
            petition_json = json.load(open(os.path.join(dirname, filename), 'r'))
            if 'data' in petition_json:
                petition = petition_json['data']['attributes']
            if 'attributes' in petition_json:
                petition = petition_json['attributes']
            else:
                continue
            output.write("<|startofpetition|>\n")
            output.write(petition['action'] + "\n")
            output.write("=================\n\n")
            if 'background' in petition and petition['background'] is not None:
                output.write(petition['background'].replace("\r", "") + "\n")
            if 'additional_details' in petition and petition['additional_details'] is not None:
                output.write(petition['additional_details'].replace("\r", "") + "\n")
            if petition['rejected_at'] is not None and petition['rejection']['details'] is not None and petition['rejection']['details'][:8] != "https://":
                output.write("\n\nReason for rejection:\n\n")
                output.write(petition['rejection']['details'].replace("\r", "") + "\n")
            output.write("<|endofpetition|>\n\n")

output.close()

sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
        output_filename,
        model_name=MODEL_NAME,
        steps=TRAINING_STEPS,
        save_every=100)
