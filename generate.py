#!/usr/bin/env python3
import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

petition = gpt2.generate(sess, prefix="<|startofpetition|>", truncate="<|endofpetition|>", include_prefix=False, return_as_list=True)[0]
petition = petition.replace("<|startofpetition|>", "") # Sometimes this gets duplicated

print(petition)
