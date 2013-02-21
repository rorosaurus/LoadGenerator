This python script simply consumes CPU cycles and memory.  It also makes a couple http requests to facilitate network usage.

Here are some helpful commands and tips.

One way to ensure the process continues after your SSH session closes:
	$> nohup python loadgen.py &

Obtain the pid of the script you wish to kill by observing the output of
	$> ps -ef | grep python
or
	$> ps -ef | grep loadgen.py
The pid should be the second column of this output.  You can verify this by running
	$> ps -ef
without piping it into grep.

Process can be killed using the kill command and the -9 arg.  The final argument is the pid of the process to kill.
	$> kill -9 2430

You can also edit the rc.local file in /etc/ to have this script start automatically upon boot.  Simply add:
	python /location/to/repository/LoadGenerator/loadgen.py
and save the file.
