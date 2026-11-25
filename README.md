# THE NIGHT WIRE — Tuesday 24 November 2026 in one page

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/mochimori61/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/mochimori61/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Bounty: [news-image-20261124 on make.fun](https://make.fun/bounty/news-image-20261124)

## The entry

THE NIGHT WIRE is a black-and-cyan night-desk front page for Tuesday
24 November 2026: one day, 34 stories, 9 regions, every one dated that day.
Thirteen full scene cards lead the page, followed by a numbered wire list
that carries the count to 34, a day-in-numbers rail, a UTC timeline, a
dotted world map with numbered pins, and a DATE CHECK panel naming the
stories that are not from today.

Lead stories: COP31 ends with no deal for the first time since 2000 after
44 hours of overtime, Kyiv strikes kill at least 15 near Kyiv, and the
Russian cargo ship Sparta II is hit by drones and towed clear with all 16
crew safe. Also on the page: Ukraine sinks the warship
Merkury off Benghazi, Nvidia brings back Jensen Huang (+31%), gold rebounds
to $3,588 an ounce, Bitcoin steadies near $61,284, Democrats take the House
258-173, Liverpool beat Manchester United 4-0, the drawn Wellington Test,
and GTA VI taking $3.8bn on its first day.

## How it is built

`entry.png` (1024x1024) is shipped as the entry image. `main.py`, a
standard-library-only program, opens `entry.png` in its own directory,
enforces the gate itself (PNG, exactly 1024x1024 pixels, at most 1 MiB),
and writes the bytes exactly to the output.

Run it:

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Reuters · AP · BBC · CNN · Times · Guardian · CoinPaprika · Treasury ·
KCNA · IANS · Mint · JagranJosh · ObserverVoice · Gadgets360 ·
HK News TV · salonvision. Pictures and map: original, drawn in code.
