Web Development
===============================================================================

[TOC]

-------------------------------------------------------------------------------
# Node JS / NPM

## Installation und Berechtigungen

Command                                | Remark
-------------------------------------- | --------------------------------------
sudo apt install npm                   | Installation (1)
npm install npm -g                     | Aktualisierung von npm
npm -v                                 | Anzeige Version
npm config get prefix                  | Anzeige Installationsverzeichnis (i.d.R. /usr/local)
ls -la /usr/local/lib/node_modules/    | Anzeige Berechtigungen
sudo chown -R <username> /usr/local    | Rekursive Benutzer wechseln für npm (2)

1. /usr/bin/env: ‘node’: No such file or directory
   Das Problem ist, das node je nach Installationsart unter /usr/bin/nodejs installiert wird,
   Abhilfe schafft ein symbolischer Link:
   > cd /usr/bin
   > sudo ln -s /usr/bin/nodejs /usr/bin/node

2. Anstelle von allen Verzeichnissen innerhalb /usr/local können i.d.R. auch    
   die folgenden drei Verchzeichnisse angepasst werden:
   > /usr/local/bin
   > /usr/local/share
   > /usr/local/lib/node_moduls


## Package Management

Command                                | Remark
-------------------------------------- | --------------------------------------
npm ls                                 | Anzeige Packages (vom Projekt)
npm outdated                           | Anzeige veraltete Packages
npm update                             | Update Packages gemäss den Semantic Versioning Rules
npm uninstall <package>                | Entfernt Package aus lokalem Repo
npm uninstall --save <package>         | Entfernt Package aus lokalem Repo und package.json
npm prune                              | Löschen der nicht verwendenten (extraneous) Packages


## Hello World (mit lokal installierten Packages)

- Verzeichnis erstellen ( ../playground/npm-hello)

- Datei erstellen package.json mit Name und Version (Datei kann auch mit 'npm init' erstellt werden)
  {
  	"name": "npm-hello",
  	"version": "1.0.0"
  }

- NPM wird dann alle aufgeführten packages lokal installieren; Mit der save Option kann auch ein
  Package installiert und automatisch dem package.json File hinzugefügt werden.

- Beispiel: npm install lodash --save
  {
	   "name": "npm-hello",
	   "version": "1.0.0",
	   "dependencies": {
		    "lodash": "^4.17.4"
	   }
  }

- Versionierung:
  - Patch Release: 1.0 or 1.0.x or ~1.0.4 - Bugfixes
  - Minor Release: 1   or 1.x   or ^1.0.4 - neue Funktionen, Rückwärtskompatibel
  - Major Release: x   or *               - neue Version, API Break

- Jetzt hat npm ein lokales Unterverzeichnis "node_modules" erstellt und die entsprechenden Library
  dort abgespeichert

- Neue Datei hello.js wie folgt erstellen:
  var lodash = require ('lodash');
  var result = lodash.without(["Hello", "World", "extra"], "extra");
  console.log(result);

- Aufruf: node hello


## Samples

### Initialization of a project
- npm install                           // install
- npm run typings -- install            // if typings folder doesn't show up after install

- npm start                             // start command first compiles the application,
                                        // then simultaneously re-compiles and runs the lite-server.
                                        // Both the compiler and the server watch for file changes.

- <ctrl><c>                             // shut down manually


### We've captured many of the most useful commands in npm scripts defined in the package.json:

npm start               // runs the compiler and a server at the same time, both in "watch mode".

npm run tsc             // runs the TypeScript compiler once.
npm run tsc:w           // runs the TypeScript compiler in watch mode; the process keeps running,
                        // awaiting changes to TypeScript files and re-compiling when it sees them.

npm run lite            // runs the lite-server, a light-weight, static file server, written and
                        // maintained by John Papa and Christopher Martin with excellent support
                        // for Angular apps that use routing.

npm run typings         // runs the typings tool.

npm run postinstall     // called by npm automatically after it successfully completes package
                        // installation. This script installs the TypeScript definition files
                        // this app requires.

### Here are the test related scripts:

Attention:
It is unwise and rarely possible to run the application, the unit tests, and the e2e tests at
the same time. We recommend that you shut down one before starting another.

npm test                // compiles, runs and watches the karma unit tests

npm run e2e             // run protractor e2e tests, written in JavaScript (*e2e-spec.js)


### Unit Tests

TypeScript unit-tests are usually in the app folder. Their filenames must end in .spec.

Look for the example app/app.component.spec.ts. Add more .spec.ts files as you wish;
we configured karma to find them.

Run it with npm test

That command first compiles the application, then simultaneously re-compiles and runs the karma
test-runner. Both the compiler and the karma watch for (different) file changes.

Shut it down manually with Ctrl-C.

Test-runner output appears in the terminal window. We can update our app and our tests in real-time,
keeping a weather eye on the console for broken tests. Karma is occasionally confused and it is often necessary to shut down its browser or even shut the command down (Ctrl-C) and restart it.

No worries; it's pretty quick.

### End-to-end (E2E) Tests

E2E tests are in the e2e directory, side by side with the app folder.
Their filenames must end in .e2e-spec.ts.

Look for the example e2e/app.e2e-spec.ts. Add more .e2e-spec.js files as you wish (although one usually suffices for small projects); we configured protractor to find them.

Thereafter, run them with npm run e2e.

That command first compiles, then simultaneously starts the Http-Server at localhost:8080
and launches protractor.

The pass/fail test results appear at the bottom of the terminal window. A custom reporter (see protractor.config.js) generates a ./_test-output/protractor-results.txt file which is easier to read;
this file is excluded from source control.

Shut it down manually with Ctrl-C.




## References
- www.npmjs.com


-------------------------------------------------------------------------------
# Browser Sync

## Commands
Command                                           | Remark
------------------------------------------------- | -----------------------------------------------
npm install -g browser-sync                       | Install browser-sync globally (for all projects)
browser-sync start --server --files "css/*.css"   | Start Mini Server and watch css directory
browser-sync start --proxy  --files "css/*.css"   | Start Proxy around existing vhost


## Requirements
Browsersync works by injecting an asynchronous script tag (<script async>...</script>) right after
the <body> tag during initial request. In order for this to work properly the <body> tag must be present.


## Help
- Get help for the start command only
  $ browser-sync start --help

- Get help for the recipe command only
  $ browser-sync recipe --help


## Start

### Start a server from the `app` directory, watching all files
  $ browser-sync start --server 'app' --files 'app'

### Start a server from the `app` & `.tmp` directories (short hand) (requires 2.12.1)
  $ browser-sync start -s 'app' '.tmp' -f 'app' '.tmp'

### Proxy a PHP app + serve static files & watch them
  $ browser-sync start --proxy 'mylocal.dev' --serveStatic 'public' --files 'public'

### Start Browsersync from a config file
  $ browser-sync start --config 'conf/browser-sync.js'

### Start Browsersync from a config file with overriding flags
  $ browser-sync start --config 'conf/browser-sync.js' --port 4000


## Receipe

### List all available recipes
  $ browser-sync recipe ls

### Copy files for gulp.sass recipe
  $ browser-sync recipe 'gulp.sass'

### Copy files for gulp.sass recipe into custom output directory
  $ browser-sync recipe 'gulp.sass' -o 'my-project'


## Reload

### Reload assuming standard address of http://localhost:3000
  $ browser-sync reload

### Reload assuming standard address of http://localhost:3000
  $ browser-sync reload --port 4000 --files="*.css"

### Reload assuming standard address of http://localhost:3000
  $ browser-sync reload --url https://localhost:3000 --files="*.css"


## References
- www.browsersync.io


-------------------------------------------------------------------------------
# Sass

## Transform with watch
sass --watch app.scss:app.css                           // single file


## Transform materialize css
sass sass/materialize.scss css/materialize.css


## Reinstall new version
sudo apt-get remove ruby-sass
sudo apt-get remove ruby-compass
gem list --local
sass -v

sudo apt-get install ruby-full
sudo gem install sass
sudo gem install compass

sass --version
gem list --local

sudo gem install sass
sudo gem install sass-listen
gem list --local
sass -v
ruby -v


## Installation
sudo apt-get install ruby-full build-essential ruby
sudo gem install sass

sudo apt-add-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get install ruby2.4
sudo apt-get install ruby-sass
sudo apt-get install ruby-listen
sass -v


## Bugfix fuer die Meldung: uninitialized constant Listen::MultiListener (NameError)
sudo gem uninstall listen
sudo gem install listen -v 0.7.3
sudo gem install listen -v 0.7.3


-------------------------------------------------------------------------------
# Webpack

## Commands
Command                                           | Remark
------------------------------------------------- | -----------------------------------------------

## References
- webpack.js.io



-------------------------------------------------------------------------------
# Gradlew

## Commands
Command                                           | Remark
------------------------------------------------- | -----------------------------------------------
./gradlew build                                   | start build
./gradlew eclipse                                 | create eclipse project
./gradlew bootRun                                 | start application
./gradlew run                                     | start application
./gradlew watch                                   | watch
./gradlew npm_[command]                           | Alle npm Befehle können via gradle aufgerufen werden
./gradlew npm_help                                |  zeigt die npm Hilfe
./gradlew npm_show_webpack                        |  zeigt die möglichen Versionen vom webpack



-------------------------------------------------------------------------------
# More References

- Online Course
  https://www.codeschool.com


- Spring Boot
https://dzone.com/articles/7-things-to-know-getting-started-with-spring-boot?edition=351093&utm_source=Weekly%20Digest&utm_medium=email&utm_campaign=Weekly%20Digest%202018-01-10


-------------------------------------------------------------------------------
_The end._
