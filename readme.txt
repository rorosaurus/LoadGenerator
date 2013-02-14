One way to ensure process continues after SSH session closes:
	$> nohup python loadgen.py &

Process can be killed using the kill command and the -9 arg
	$> kill -9 2430

Obtain the pid (the second argument) by observing the output of
	$> ps -ef | grep python
