#!/bin/bash
set -euo pipefail
SCRIPT_DIR=$(realpath "$(dirname "$0")")

if [[ $# != 1 ]]; then
  echo "Please provide a day number."
  echo "usage: $0 DAY"
  exit 1
fi

if [[ ! "$1" =~ ^(0[1-9]|1[0-9]|2[0-5])$ ]]; then
  echo "Argument '$1' is not a valid day."
  exit 1
fi

if [[ -z "${AOC_SESSION-"53616c7465645f5feb121b295be088bc3dd751050a30591abf79bdd1f761fa30c2647062b24109cba05ab9f862389989d237c29053036701ae9c2ef592262e8d"}" ]]; then
  echo "No session token set in \$AOC_SESSION."
  exit 1
fi

URL="https://adventofcode.com/2015/day/$(("10#$1" + 0))/input"
curl "$URL" --cookie "session=53616c7465645f5feb121b295be088bc3dd751050a30591abf79bdd1f761fa30c2647062b24109cba05ab9f862389989d237c29053036701ae9c2ef592262e8d" -s | tee "$SCRIPT_DIR/inputs/$1.in"
