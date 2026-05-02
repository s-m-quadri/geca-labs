#!/usr/bin/env bash
set -euo pipefail
DB="${1:?usage: run_source.sh <database> <file.sql>}"
FILE="${2:?}"
sudo mysql "$DB" -e "source $(readlink -f "$FILE")"
