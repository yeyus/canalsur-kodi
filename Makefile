KODI_FOLDER=$(HOME)/Library/Application Support/Kodi/addons
copy:
	rsync -av --exclude="env" --exclude=".git" --exclude=".vscode" --out-format="[%t]:%o:%f:Last Modified %M" ./ "$(KODI_FOLDER)/canalsur-kodi/"