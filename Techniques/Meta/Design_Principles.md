# Design Principles for AI Prompts

## Goal

The general goal of all design for AI is to prove one thing.

```
Complex Language = Power
```

## Methodology

The general methodology for us to show the above goal is also in one sentence.

````
Understanding of Psychology = Complexity
````

## Limitations

Current limitations on AI is available on the internet and is easy to be searched out, for the time when this guideline is being written. Still, I want to address several limitations on the current AI Language model, GPT:

- Chat history is limited.
- Prompt length and answer length is limited.
- Focuses more on most current chats and ignores long-term history.

## Design Principles

Based on the above facts, now we want to arrive at the general principle for designing techniques to be utilized by GPT.

##### Chinese Character Technique Name

One should use Chinese Characters to name the techniques. This can save length in tokens.

> Up to now, several techniques are not being normalized in this way. This should be corrected in the future.

##### Aspects

One should consider how many aspects that one can think. For example, 内省, 外延, 简化, etc.

##### Section for a Technique File

A complete technique file should consist of the following:

- (System)Meta guidance for AI to understand the content followed
- (Prompt)Description on how to use the technique
- (Example)Concrete application in real examples for AI to see it clearly.
- (Test)A short exercise for AI to show how well it can make. If it goes more complicated, it will have to be tested with some benchmarks like how they do in the academic papers.