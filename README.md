music-controller
================

Have I left my music on to irritate you? Fix it by emailing my account to turn it off!


The credfile is where the login details are stored for use by the script. Obviously they should not be in the 
git repo ;)

The credfile is a simple text file with a field per line in this order:
    username
    password (cleartext)
    email address to notify of muting
    imap server address
    imap server port
    smtp server address
    smtp server port
    logfile path

The credfile path is specified by the -c parameter to the script e.g.
    python musicctl.py -c credfile
