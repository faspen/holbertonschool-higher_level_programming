#!/usr/bin/env bash
# Take url, send request
curl -s "$1" | wc -c
