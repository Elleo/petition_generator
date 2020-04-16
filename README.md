# Petition Generator

A silly project to generate UK government style petitions via a GPT-2 transformer.

You can view the generated petitions here: https://elleo.github.io/petition_generator/

## Generating output

To generate your own output you can download a checkpoint from the releases section and unpack it in the project directory, or train yourself (see below)

Install the requirements by running `pip3 install -r requirements.txt`

Then simply run `./generate.py` to output a petition

The `generate_json.py` script can be used to add additional entries to the `pregenerated.json` file which is used by the HTML viewer.

## Training

To train the model ensure you've checked out the `uk_petitions_data` submodule by running `git submodule update --init`

Then just run `./train.py`
