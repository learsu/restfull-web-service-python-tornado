#!/bin/bash
# Filename:    start.sh
. /etc/profile
#set listen line the same as you cpu core num
listen_line=2
listen_start=8889

CWD=`pwd`
cd $CWD

case "$1" in
	start)
		/bin/rm -rf main.port
		for (( i=0 ; i<${listen_line} ; i++)); do
			listen_port=$[${listen_start}+${i}]
			echo ${listen_port} >> main.port
			python start.py ${listen_port} &
		done
		echo "start ok !"
		;;
	stop)
		get_port_line=`/bin/cat main.port`
		for i in ${get_port_line};do
			now_pid=`/bin/ps -ef|grep ${i}|grep -v grep|awk ' ''{print $2}'`
			/bin/kill -9 $now_pid
		done
		echo "stop"
		;;
	status)
		get_port_line=`/bin/cat main.port`
		for i in ${get_port_line};do
			now_pid=`/bin/ps -ef|grep ${i}|grep -v grep`
			if [ -z "${now_pid}" ] ; then
				echo ${i} "is stop"
			else
				echo ${now_pid}
			fi
		done
		;;
	restart)
		$0 stop
		$0 start
		;;
	*)
		echo $"Usage: bash $0 {start|stop|restart|status}"
		exit 1
esac

exit 1