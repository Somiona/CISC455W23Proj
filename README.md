# CISC455W23Proj
EMOTIONAL DAMAGE! Haiya

You need to install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable), [NodeJS](https://nodejs.org/en/download) and [pipenv](https://pypi.org/project/pipenv/#installation) for this project to run.

On windows, you need npm package concurrently to run

``` powershell
npm install -g concurrently
```

On Unix-like systems, you don't need concurrently package

To render documentation as a website, you need to install [docsify](https://docsify.js.org/#/quickstart)

``` bash
npm i docsify-cli -g
```

To run documentation website, run

``` bash
docsify serve docs
```

Before running `launch_all.sh`, make sure you've run `pipenv install` inside the root dir of this project!
Not inside Backend

Also, remember use CISC455W23Proj.code-workspace instead of directly open the folder.