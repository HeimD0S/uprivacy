## uprivacy 
### An Ad-Block-Compatible List Based On the EFF's Privacy Badger Seed List

A short and sweet list that updates based on EFF's Privacy Badger Seed List found here:

https://github.com/EFForg/privacybadger

I created this because I leverage AdNauseam, which is a fork of ublock origin, and it comes into conflict when using Privacy Badger. 
Because heuristics is disabled by default since it can finger print, EFF pre-loads Privacy Badger with a seed list of known tracker domains. When comparing it to some of the existing built-in lists of ublock, not all domains were covered, so I created a short script to manage the gaps in coverage, allowing you to import it directly into ublock.

### How To Install
1. Open ublock
2. Click the Cog Wheel to open up the Extension settings
3. At the top, find 'Filter Lists' and navigate there.
4. Scroll to the bottom, find 'Import...' and select it.
5. Paste `https://raw.githubusercontent.com/HeimD0S/uprivacy/main/privacybadger.txt` into the empty box. If your import lists already has items, create a new line and insert the list URL there.
7. Look at the top of your page and you should see the '✓ Apply Changes' button. Select it.
8. Refresh the page and you should see a new 'Custom' category at the bottom of the Filter Lists, with 'EFF Privacy Badger Blocklist' added and already selected.
9. Adding this list enables the blocking of domains based on EFF's rulesets they built for Privacy Badger.

## Go Support the EFF
https://www.eff.org/ 
