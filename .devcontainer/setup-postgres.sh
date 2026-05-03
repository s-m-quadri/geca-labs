#!/usr/bin/env bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
if ! command -v psql >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo apt-get install -y -qq postgresql postgresql-client
fi
sudo service postgresql start 2>/dev/null || true
sudo -u postgres psql -c "SELECT 1" >/dev/null
echo "PostgreSQL ready. Run: sudo -u postgres psql -f file.sql"
