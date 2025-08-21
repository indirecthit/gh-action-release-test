#!/usr/bin/env bash
set -euo pipefail
VERSION=$(cat VERSION)
echo "Deploying v${VERSION}..."
sleep 1
echo "Deployed!"
