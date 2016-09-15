a simple script to fetch the main content of a list of urls, then convert them to markdown, epubs, and mobis.

requires:
- calibre (`apt-get install calibre`)
- pandoc (`apt-get install pandoc`)
- newspaper3k (`pip install newspaper3k`)
- nom (`pip install nom`)

usage:
- write your list of urls to `urls.txt`, one url per line (see example)
- run `./go.sh`


notes:
- this does not fetch images!
- sometimes the titles/authors don't seem to work (at least for the mobi output), I'm not sure why