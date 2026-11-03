#!/usr/bin/env bash
# Compatible entry point; Python owns path validation, packaging and provenance.
set -euo pipefail
exec "${PYTHON:-python3}" "$(dirname "$0")/build_plugin.py" "$@"
