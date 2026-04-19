#!/usr/bin/env bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
if ! command -v mysqld >/dev/null 2>&1 && ! command -v mysql >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq mysql-server default-mysql-client
fi
if command -v service >/dev/null 2>&1; then
  sudo service mysql start 2>/dev/null || sudo service mysqld start 2>/dev/null || true
fi
sudo mysql -e "SELECT 1" >/dev/null
echo "MySQL ready. Procedural files with DELIMITER: chmod +x run_source.sh && ./run_source.sh proc_lab <file.sql>"
