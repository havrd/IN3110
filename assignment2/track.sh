#! /bin/bash


function track(){
  if [[ -z "${LOGFILE}" ]]; then
  export LOGFILE=~/.local/share/.timer_logfile
  fi

  if [[ ! -f "~/.local/share/.timer_logfile" ]];
  then
      touch ~/.local/share/.timer_logfile
  fi



  if ([[ $# != 1 ]] && [[ $1 != "start" ]]) || ([[ $1 == "start" ]] && [[ $# != 2 ]]) ; then
    echo -e "\nUsage: $0 <command>"
    echo "To start tracking a new task, enter:            'track start <label>' "
    echo "To finish tracking current task, enter:         'track stop'"
    echo "To get info on current task, enter:             'track status'"
    echo "To see time used on all previous tasks, enter:  'track log'"
    return
  fi

  if ([[ $(cat $LOGFILE | tail -n 1 | cut -d ' ' -f1) != "END" ]] && [[ $1 == "start" ]]) && [[ -s $LOGFILE ]]; then
    echo "Cannot start a new task when another task is currently running."
     return
  fi

  if ([[ $(cat $LOGFILE | tail -n 1 | cut -d ' ' -f1) == "END" ]] && [[ $1 == "stop" ]]) && [[ -s $LOGFILE ]]; then
    echo "No task is currently running"
    return
  fi

  if [[ $1 == "start" ]]; then
     echo -e "START $(date) \nLABEL ${2}" >> $LOGFILE

  elif [[ $1 == "stop" ]]; then
     echo -e "END $(date)" >> $LOGFILE

  elif [[ $1 == "status" ]]; then
     if [[ $(cat $LOGFILE | tail -n 1 | cut -d ' ' -f1) == "LABEL" ]]; then
       echo "Task labled '$(cat $LOGFILE | tail -n 1 | cut -d ' ' -f2-)' currently running"
     else
       echo "No task currently running"
     fi

   elif [[ $1 == "log" ]]; then
     start=""
     end=""
     task=""
     diff=""
     while IFS='' read -r line || [ "$line" ]; do
        if [[ $(echo $line | cut -d " " -f1) == "LABEL" ]]; then
          task=${line:6}

        elif [[ $(echo $line | cut -d " " -f1) == "START" ]]; then
          start=${line:6}

        elif [[ $(echo $line | cut -d " " -f1) == "END" ]]; then
          end=${line:4}
          start=$(date -d "$start" +%s)
          end=$(date -d "$end" +%s)
          let t=$end-$start
          echo "$task: $(date -d@$t -u +$(($t/3600/24)):%H:%M:%S)"
        fi
      done < "$LOGFILE"

   else
     echo "Command not recognized"
  fi
}

