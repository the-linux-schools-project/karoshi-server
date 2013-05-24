#!/bin/bash
#Copyright (C) 2012 Robin McCorkell
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#The Karoshi Team can be contacted at: 
#mpsharrad@karoshi.org.uk
#jharris@karoshi.org.uk
#aball@karoshi.org.uk
#
#Website: http://www.karoshi.org.uk

#Note: No validation of actual file path or correct permissions performed.
#	If the running user does not have correct writing permissions, or the
#	file directory is missing, this script will fail.

#####################
#function definitions
#####################

#_check_file			check if file exists and is not empty
#_no_data				error handling
#_to_date				convert UNIX timestamp to dd/mm/yyyy hh:mm:ss
#_conv_time				convert seconds to full time
#_calc_percentage		calculate percentage of $1 / $2 to 4 decimal places

#file_session_boottime	get boot time for session $1
#file_session_endtime	get time at end of session $1
#file_session_uptime	get uptime for session $1
#file_session_count		get number of sessions in file
#file_total_time		get time between first recorded boot and last update
#file_total_uptime		get total recorded uptime
#file_update_uptime		update uptime information in file

#session_uptime			get uptime of this session
#session_boottime		get boot time of this session

#output_downtime		output total downtime
#output_uptime			output total uptime
#output_all_data		output all recorded data
#output_start_time		output first recorded boot time
#output_summary_table	output summary data

#display_help			output help

#parse_options			parse options
#parse_command			parse command
#parse_other			parse other options

version="2.6"

uptimefile="/var/spool/karoshi-uptime"
command=""
outputformat="r"
otherparams=""
optionhelp=false

##################
#primary functions
##################

#check if file exists and is not empty
function _check_file {
	if [ ! -s "$uptimefile" ]; then
		false
	else
		true
	fi
	return
}
#error handling
function _no_data {
	echo "No data found!"
}
#get boot time for session $1
function file_session_boottime {
	if [ "$1" ]; then
		echo `sed "$(( ($1 * 2) -  1 ))q;d" "$uptimefile"`
	fi
}
#get uptime for session $1
function file_session_uptime {
	if [ "$1" ]; then
		echo `sed "$(( $1 * 2 ))q;d" "$uptimefile"`
	fi
}
#number of sessions in file
function file_session_count {
	echo $(( $(wc -l "$uptimefile" | cut -d " " -f 1) / 2 ))
}
#convert UNIX timestamp to dd/mm/yyyy hh:mm:ss
function _to_date {
	date --date="@$1" "+%d/%m/%Y %T"
}
#convert seconds to full time
function _conv_time {
	_conv_time_format=""
	if [ "$2" = "s" ]; then
		_conv_time_format="%dd, %02dh, %02dm, %02ds"
	else
		_conv_time_format="%d days, %02d hours, %02d minutes, %02d seconds"
	fi
	printf "${_conv_time_format}\n" $(( $1 / 86400 )) $(( $1 / 3600 % 24 )) $(( $1 / 60 % 60 )) $(( $1 % 60 ))
}
#get current uptime of this session
function session_uptime {
	session_uptime_local=`cut -d " " -f 1 /proc/uptime`
	echo ${session_uptime_local%.*}
}
#calculate percentage to 4 decimal places
function _calc_percentage {
	echo "$1 $2" | awk '{printf "%.4f\n", $1*100/$2}'
}


####################
#secondary functions
####################

#get time at end of session $1
function file_session_endtime {
	if [ "$1" ]; then
		echo $(( `file_session_boottime $1` + `file_session_uptime $1` ))
	fi
}
#get boot time of this session
function session_boottime {
	echo $(( `date +%s` - `session_uptime` ))
}


###################
#tertiary functions
###################

#get time between first recorded boot and last update
function file_total_time {
	echo $(( `file_session_endtime $(file_session_count)` - `file_session_boottime 1` ))
}
#get total reported uptime
function file_total_uptime {
	file_total_uptime_entries=$(file_session_count)
	file_total_uptime_uptime=`file_session_uptime $(file_session_count)`
	for (( i = 1; i < $file_total_uptime_entries; ++i )); do
		(( file_total_uptime_uptime += `file_session_uptime $i` ))
	done
	echo $file_total_uptime_uptime
}
#update uptime information in file
function file_update_uptime {
	file_update_uptime_uptime=`session_uptime`
	file_update_uptime_time=`date +%s`
	function append_new {
		echo `session_boottime` >> "$uptimefile"
		echo $file_update_uptime_uptime >> "$uptimefile"
	}
	function update_last {
		file_update_uptime_uptime=$(( $file_update_uptime_time - `file_session_boottime $(file_session_count)` ))
		sed -i "\$s/.*/$file_update_uptime_uptime/" "$uptimefile"
	}
	
	if ! _check_file ; then
		append_new
	else
		if [ `session_boottime` -lt `file_session_endtime $(file_session_count)` ]; then
			update_last
		else
			append_new
		fi
	fi
}

#################
#output functions
#################
#output downtime
function output_downtime {
	if _check_file; then
		output_downtime_totaltime=$(file_total_time)
		output_downtime_totaldowntime=$(( $output_downtime_totaltime - `file_total_uptime` ))
		case "$1" in
		p)
			_calc_percentage $output_downtime_totaldowntime $output_downtime_totaltime
			;;
		n)
			_conv_time $output_downtime_totaldowntime
			;;
		*)
			echo $output_downtime_totaldowntime
			;;
		esac
	else
		_no_data
	fi
}
#output uptime
function output_uptime {
	if _check_file; then
		output_uptime_totaltime=$(file_total_time)
		output_uptime_totaluptime=$(file_total_uptime)
		case "$1" in
		p)
			_calc_percentage $output_uptime_totaluptime $output_uptime_totaltime
			;;
		n)
			_conv_time $output_uptime_totaluptime
			;;
		*)
			echo $output_uptime_totaluptime
			;;
		esac
	else
		_no_data
	fi
}
#output all data
function output_all_data {
	if _check_file; then
		output_all_data_entry_count=$(file_session_count)
		for (( i = 1; i < $output_all_data_entry_count; ++i)); do
			output_all_data_boot=`file_session_boottime $i`
			output_all_data_down=`file_session_endtime $i`
			if [ "$1" = "n" ]; then
				output_all_data_boot="`_to_date "$output_all_data_boot"`"
				output_all_data_down="`_to_date "$output_all_data_down"`"
			fi
			echo "$output_all_data_boot,$output_all_data_down"
		done
		output_all_data_boot=`file_session_boottime $i`
		[ "$1" = "n" ] && output_all_data_boot="`_to_date "$output_all_data_boot"`"
		echo $output_all_data_boot
	else
		_no_data
	fi
}
#output first boot time
function output_start_time {
	output_start_time_starttime=`file_session_boottime 1`
	case "$1" in
	n)
		_to_date "$output_start_time_starttime"
		;;
	*)
		echo "$output_start_time_starttime"
		;;
	esac
}
#output help
function display_help {
	echo "Karoshi Uptime Script v$version"
	echo "Copyright 2012 The Linux Schools Project"
	echo "Maintained by Robin McCorkell"
	echo
	echo "Data file is: $uptimefile"
	echo "Session boot time is: `_to_date $(session_boottime)`"
	echo "Usage: $0 [options] command"
	echo
	echo "Options: "
	echo -e "  -n, --natural\t\toutput in full date format"
	echo -e "  -r, --raw\t\tdefault, output in UNIX timestamp"
	echo -e "  -p, --percent\t\toutput downtime as percentage"
	echo -e "      --file=[file]\tstore uptime data in [file]"
	echo
	echo "Commands:"
	echo -e "  update\tupdate uptime file with latest information"
	echo -e "  reset\t\tclear downtime data and restart uptime counter"
	echo -e "  auto [n]\trun forever, updating automatically every [n] seconds"
	echo -e "  start-time\treturn first recorded boot time"
	echo -e "  downtime\treturn downtime since first recorded boot"
	echo -e "  uptime\treturn uptime since first recorded boot"
	echo -e "  all-data\treturn array of boottime,shutdowntime separated by newline"
	echo -e "  summary\treturn table of all information, in a human readable format"
}
#output full data table
function output_summary_table {
	output_summary_table_entry_count=`file_session_count`
	for (( i = 1; i < $output_summary_table_entry_count; ++i )); do
		echo -e " $i\t  `_to_date $(file_session_boottime $i)`\t  `_to_date $(file_session_endtime $i)`\t  `_conv_time $(file_session_uptime $i) s`"
	done
	echo -e " cur\t  `_to_date $(file_session_boottime $i)`\t\t\t\t  `_conv_time $(file_session_uptime $i) s`"
}

##################
#parsing functions
##################
function parse_options {
	if [ ${1:0:1} = "-" ]; then
		case "${1:1}" in
		help)
			optionhelp=true
			;;
		natural)
			outputformat="n"
			;;
		raw)
			outputformat="r"
			;;
		percent)
			outputformat="p"
			;;
		file*)
			parse_options_file=${1:6}
			if [ ! "$parse_options_file" ]; then
				echo "No file specified!"
				exit
			fi
			uptimefile="$parse_options_file"
			;;
		esac
	else
		for (( i=0; i<${#1}; ++i )); do
			case "${1:$i:1}" in
			n)
				outputformat="n"
				;;
			r)
				outputformat="r"
				;;
			p)
				outputformat="p"
				;;
			esac
		done
	fi
}
function parse_command {
	command=$1
}
function parse_other {
	if [ $otherparams ]; then otherparams="$otherparams $1"
	else otherparams="$1"; fi
}

#################
#argument parsing
#################
for arg in "$@"; do
	if [ ${arg:0:1} = "-" ]; then
		parse_options "${arg:1}"
	else
		if [ ! "$command" ]; then
			parse_command "$arg"
		else
			parse_other "$arg"
		fi
	fi
done

$optionhelp && display_help && exit

###################
#command processing
###################
case "$command" in
debug-command)
	eval "$otherparams"
	;;
update)
	file_update_uptime
	;;
start-time)
	output_start_time $outputformat
	;;
downtime)
	output_downtime $outputformat
	;;
uptime)
	output_uptime $outputformat
	;;
all-data)
	output_all_data $outputformat
	;;
reset)
	cat /dev/null > "$uptimefile"
	file_update_uptime
	;;
auto)
	interval=`echo "$otherparams" | sed "s/.* \([^ ]*\)\$/\1/"`
	if [ "$interval" -gt 0 ]; then
		while true; do
			file_update_uptime
			sleep $interval
		done
	else
		echo "Invalid interval specified - $interval"
	fi
	;;
summary)
	echo -e " id\t| boot time\t\t| shutdown time\t\t| uptime"
	output_summary_table
	echo
	echo "First boot: `_to_date $(file_session_boottime 1)`"
	echo "    Uptime: $(output_uptime n) - $(output_uptime p)%"
	echo "  Downtime: $(output_downtime n) - $(output_downtime p)%"
	;;
*)
	echo "Invalid command $command - try --help"
	;;
esac
