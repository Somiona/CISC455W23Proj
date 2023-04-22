Start-Process deno -ArgumentList "task --cwd .\\frontend -c .\\frontend\\deno.json start"
Start-Process pipenv -ArgumentList "run flask --app .\\backend\\index run"