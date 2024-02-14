# Daily Grammar Practice Solver
## Important information
- The code may, or may not work. I'm new to coding and this is a fork of my APCSP project. _I've also never used github before_
- When referring to parts of speech, normally 'pos' will be used.
- The code is being actively migrated from code.org which uses a different version of javascript. The code for **Version 1** is done and **Version 2** is being worked on.
## Current/Planned Versions
- Version 1 of this app is able to check the pos of a word based off a given dictionary that has a bunch of words and their most common POS.
- Version 2 is in the works and will be able to use logic to defer what type of pos each word is using context in the sentence and using version 1 as a 'baseline' to check against to help infer which pos the word probably is. 

## Benefits
This is not a comprehensive list, just a quick write-up made in a few minutes.
### Version 1
- Allows you to get a rough estimation of what the POS is for each word in the sentence.
### Version 2
- Allows you to get a rough _but more accurate_ estimation of the POS for each word.
- Isn't limited to a dictonary. _Though it may be limited to how well version one is, due to it relying on version one for a baseline. Will figure out later._
## Disadvantages
### Version 1
- Can only give the POS of the words that also are in the dictionary.
- Cannot detect which POS the word should be using context, for example the word brown can either be an adjective, noun, or verb.
### Version 2
- Relies on version 1 which relies on the dictionary, will have to fix later.
- May give the incorrect POS
