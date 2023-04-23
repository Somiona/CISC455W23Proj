# Author: Somiona Tian (17ht13@queensu.ca)
# Disclaimer: This code is being tested under powershell core 7.3.4 under Windows 11

$yarn_cmd = "yarn --cwd .\\frontend dev"
$flask_cmd = "pipenv run flask --app .\\backend\\index run"

concurrently --kill-others --names "yarn,flask" --prefix-colors "bgBlue,bgGreen" "$yarn_cmd" "$flask_cmd"