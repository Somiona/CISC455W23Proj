# How to start coding

## Prerequisites
You need to install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable), [NodeJS](https://nodejs.org/en/download) and [pipenv](https://pypi.org/project/pipenv/#installation) for this project to run.

On windows, you need npm package concurrently to run

``` terminal
>| npm install -g concurrently
```

On Unix-like systems, you don't need concurrently package

To render documentation as a website, you need to install [docsify](https://docsify.js.org/#/quickstart)

``` terminal
$| npm i docsify-cli -g
```

To run documentation website, run

``` terminal
$| docsify serve documentation
```
## How to run the project
Before running `launch_all.sh`, make sure you've run `pipenv install` inside the root dir of this project!
Not inside Backend

Also, remember use CISC455W23Proj.code-workspace instead of directly open the folder.