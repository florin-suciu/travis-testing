#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

echo "Doing stuff 1 start."
sleep 7
echo "Doing stuff 1 mid."
echo "Secret is: $SECRET."
sleep 7
echo "Doing stuff 1 end."
