$nodeProcess = Start-Process deno -ArgumentList "task --cwd .\\frontend -c .\\frontend\\deno.json start" -PassThru

# Launch Flask server
$flaskProcess = Start-Process pipenv -ArgumentList "run flask --app .\\backend\\index run" -PassThru