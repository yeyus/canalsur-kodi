KODI_FOLDER=$(HOME)/Library/Application Support/Kodi/addons
# Try to detect current branch if not provided from environment
BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)

# Commit hash from git
COMMIT=$(shell git rev-parse --short HEAD)

# Tag on this commit
TAG ?= $(shell git describe --tags --exact-match)

copy:
	rsync -av --exclude="env" --exclude=".git" --exclude=".vscode" --out-format="[%t]:%o:%f:Last Modified %M" ./ "$(KODI_FOLDER)/canalsur-kodi/"

release:
	@find . -name ".DS_Store" -delete
	cd ..; zip -r canalsur-kodi-$(BRANCH)-$(COMMIT) ./canalsur-kodi -x '*.git*' -x '*env*' -x '*.vscode*' -x '*__pycache__*'