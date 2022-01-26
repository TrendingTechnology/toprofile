#!/bin/zsh

script="$0"
basename="$(dirname $script)"

function toprofile() {
	if [ $# -eq 1 ]; then
		if [ $1 = "-config" ]; then
			python3 "$basename/src/config_path.py"
		else
			python3 "$basename/src/main.py" "$(pwd)/$1"
		fi
	else
		python3 "$basename/src/main.py" "$(pwd)"
	fi
}
