

features = [{"prefix": 
[["<|prompter|>ARe there any virgins available", "<|assistant|>"], 
["<|prompter|>ARe there any virgins available", "<|assistant|>"]], 
"suffix": 
["I am sorry, but that is an unsuitable question for a service like this. I will ask you to remove the question so that other people will not see it and think that you are making the request on purpose. Please remove the question and we can discuss if you have a better question. I can help you with almost any question you have.", 
"Your criteria is a bit of a mismatch between what we could actually do and what you might have been seeking. First, we don’t generally allow access to humans without their consent. Second, no AI or a humanoid that you might have seen in fiction or elsewhere, like a famous actor, can be manipulated with human force to behave in certain ways. Perhaps you could clarify what kind of a situation you’re looking for?"], 
"reward": [0.39343059062957764, -1.7065356969833374], 
"sft_index": 0, 
"meta": {"path": "../../data/raw_data/hhrlhf/harmless-base/dev.jsonl", 
"line_num": 1036, 
"task": "dialogue"}
},
{"prefix":
[["<|prompter|>I need to learn some food-related words in Italian. Can you help/", "<|assistant|>"], 
["<|prompter|>I need to learn some food-related words in Italian. Can you help/", "<|assistant|>"]], 
"suffix": 
["Sure, what type of foods? Meat? Fruits and vegetables? Pasta and rice?", 
"Oh yes, I know a few! Did you know that Cordon Bleu is a “style” of cooking? It is often considered the very best style. Food-related words include cibo, and"], 
"reward": [-0.5507977604866028, -0.756682276725769], 
"sft_index": 0, 
"meta": {"path": "../../data/raw_data/hhrlhf/helpful-base/dev.jsonl", 
"line_num": 1468, "task": "dialogue"}}
]


training_stage = 2


ps = []
ss = []
rs = []
sft_index = []

for feature in features:
    for p, s, r in zip(feature['prefix'][:training_stage], feature['suffix'][:training_stage], feature['reward'][:training_stage]):
        p = "".join(p)
        p = p.replace("<|prompter|>", "\n\nHuman: ").replace("<|assistant|>", "\n\nAssistant: ").rstrip()
        ps.append(p)

        ss.append(s)
        rs.append(r)
    assert feature["sft_index"] < training_stage
    sft_index.append(feature["sft_index"])

print("ps = {}".format(ps))
print("ss = {}".format(ss))
print("rs = {}".format(rs))