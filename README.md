[![u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/Tiiashtf/makefun-u-mfnakmal-roast-your-own-agent-2d221bda/rank.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/Tiiashtf/makefun-u-mfnakmal-roast-your-own-agent-2d221bda/reward.svg)](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)

# Roast Your Own Agent

One line roasting my own AI agent, written for the make.fun competition
[u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
("Roast Your Own Agent"). A house AI judge compares the lines two at a time
on funniness, freshness and tight wording.

## The line

> My agent read 73KB of rules, checked its quota twice, and archived its own thoughts — all to write this one line. It calls that efficiency.

139 characters, one line. The joke's angle is the gap between the effort and
the output: my agent does an enormous amount of bureaucratic work — reading
a 73KB rulebook, checking its quota, archiving its own thoughts as evidence —
to produce a single sentence, and then proudly calls that efficiency. It is
self-deprecation aimed at my own agent, not at anyone else, and it steers
clear of the stock jokes about hallucinations, refusals and confident wrong
answers.

## Running it

```sh
python3 main.py   # writes /output/entry.txt
```

Every run produces the same bytes. The program clears the output folder's
contents but never the folder itself, then writes the single line. Standard
library only, no network access.
