#!/usr/bin/env bash
set -o errexit
set -o nounset
set -o pipefail

echo "Doing stuff 2 start."
sleep 10
echo "Doing stuff 2 mid."
echo "Secret is: $SECRET."
sleep 10
echo "Doing stuff 2 end."
