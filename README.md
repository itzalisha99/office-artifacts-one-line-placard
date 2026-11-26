# Office Artifacts: The One-Line Placard Contest

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/itzalisha99/office-artifacts-one-line-placard/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![Reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/itzalisha99/office-artifacts-one-line-placard/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

A program that writes one museum placard — a single line, at most 180
characters — for an ordinary office object treated as an ancient
artifact, to `/output/entry.txt`.

## The placard

> Keyboard, c. 2001. Coffee-stained plastic. Each key a small prayer;
> the space bar, worn smooth by the faithful, answered none. Gift of
> the Typing Pool.

The conceit: a computer keyboard recast as a ritual object. Every key
is a small prayer; the space bar, worn smooth by generations of the
faithful, answered none of them. Catalogue details (date, material,
donor) sell the joke, and the line stays deadpan throughout.

## How it works

`main.py` (Python standard library only) holds the placard as a
constant, checks it through a `validate()` gate — UTF-8, 1–180
characters, non-blank, exactly one line — then writes it to
`/output/entry.txt`.

## Run

```sh
python3 main.py
```

## Bounty

[Office Artifacts: The One-Line Placard Contest](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2) on make.fun — $2 pool, winner takes all.

## License

MIT. See [LICENSE](LICENSE).
