Solutions for some [Advent of Code](https://adventofcode.com) problems. I log into that site using my `stevearm` Github account.

Python was used for 2018, but I'm trying to learn Lisp. Installed Scheme using https://kennethfriedman.org/thoughts/2021/mit-scheme-on-apple-silicon/

* Download `x86-64` binary from https://www.gnu.org/software/mit-scheme/
* Open iTerm in Rosetta: `arch -x86_64 /Applications/iTerm.app/Contents/MacOS/iTerm2`
* The `macosx-starter.c` file already had `fork` isntead of `vfork`, so didn't edit it
* Wants to install to `/usr/local/lib` and I'm not ready to run install as root
* Created folders so I don't have to
* `sudo mkdir /usr/local/lib/mit-scheme-x86-64-12.1 && sudo chmod a+w /usr/local/lib/mit-scheme-x86-64-12.1`
* `sudo mkdir /usr/local/bin/mit-scheme-x86-64-12.1 && sudo chmod a+w /usr/local/bin/mit-scheme-x86-64-12.1`
* Failed to link `/usr/local/bin/mit-scheme-x86-64-12.1/scheme` to a better path
* Running `/usr/local/bin/mit-scheme-x86-64-12.1/scheme` directly (even from the arm64 native iTerm) works

Now, I don't know the "right" way to run Scheme, but this works: From the 2023 folder, run `./scheme --load square-root.scheme --eval "(sqrt 100)"`
