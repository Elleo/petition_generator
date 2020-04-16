#!/usr/bin/env python3
import gpt_2_simple as gpt2
import json

pregenerated = open('pregenerated.json', 'r')
entries = json.load(pregenerated)
pregenerated.close()

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

petitions = gpt2.generate(sess, prefix="<|startofpetition|>", truncate="<|endofpetition|>", include_prefix=False, return_as_list=True, batch_size=10, nsamples=10)

for petition in petitions:
    petition = petition.replace("<|startofpetition|>", "") # Sometimes this gets duplicated
    petition = petition.replace("Reason for rejection:", "<strong>Why was this petition rejected?</strong>")
    lines = petition.split("\n")
    if lines[0].strip() == "":
        start = 1
    else:
        start = 0
    entry = {
            'title': lines[start],
            'body': "<br />".join(lines[start+2:])
    }
    entries.append(entry)

pregenerated = open('pregenerated.json', 'w')
json.dump(entries, pregenerated, indent=4)
pregenerated.close()
