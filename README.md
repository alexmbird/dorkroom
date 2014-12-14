# Dorkroom

A simple tool that uses OSX's speech synth to talk you through developing a 35mm film.

## Timings

...are for Kodak TMax 400 in Ilfosol 3 developer @ 20 degrees c.  Adjust to suit other films & temperatures.


## Warning

I accept no responsibility for anything ever.

To state the obvious:

+ You should be doing this with your film in a light-tight developing tank
+ Your mac might not like a bath in developing fluid!


## Setup

1. Have Python 3 installed.  On a mac with Homebrew that's as simple as `brew install python3`

2. `git clone git@github.com:alexmbird/dorkroom.git`
3. `cd dorkroom`
4. `pyvenv _venv3`

Simples.


## Running

1. `cd /path/to/dorkroom`
2. `. _venv3/bin/activate.fish`
3. `./dorkroom.py`


# Potential Improvements

Easy:

+ Accept alternative timings on the command line
+ Support different platforms by overriding `say()` to use correct speech synth binary or a proper Python library


Hard:

+ Awareness of different films & developers; automatically calculate times from this plus the temperature.

Insane:

+ Read temperature from a sensor in the bath itself


# LICENSE

MIT.  Knock yourself out.
