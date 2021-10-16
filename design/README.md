# Design for Sahaay

#### Setting up the environment

Install `expo-cli` globally

```bash
npm i -g expo-cli
```

or with yarn

```bash
yarn global add expo-cli
```

#### Development

The entry point of the app is at `index.js`. Expo takes care of setting up react properly for each environment - android, iOS and web, and imports the root component at `components/App.jsx`

Run `yarn dev` in your terminal, to start the live development server. The first time setup might take a moment, as webpack, and expo's android packager bundles the javascript. Subsequent reloads should be near-instant.

You will then see, in your terminal, the
- URL of the local server webpack is hosting your app on, which you can point your browser to.
- A QR code, which you can scan on your own mobile with the [Expo go](https://play.google.com/store/apps/details?id=host.exp.exponent) app on android, or the Camera app on iOS, to have your mobile application hot-reloaded.

Make changes in your code, and confirm that what you see in your phone reflects that change.

Note:
If you wish to use adb, or an iOS emulator you already have set up, you can use the react-native cli like so:
```bash
react-native start:android
```
```bash
react-native start:ios
```

#### Style guide

-   So as to maintain uniform code-styling across the codebase, [prettier](https://prettier.io/) has been setup. The `.prettierrc` file contains the configuration, and `.prettierignore` file contains the files to be ignored by the formatter.

-   The currently employed style guide uses 2 spaces for tabs, and avoids arrow function parentheses if possible, conforming to React style guides.

-   If you wish to use a different code style, make sure to run the `yarn format` command before pushing code to the repository, so as to make it uniform with the rest of the codebase. [TODO] Setup a github action to run code formatting on merges, and make this point obsolete.

#### Miscellaneous

A separate `.gitignore` file has been created in this folder, pre-configured for git to ignore expo-related build files. Make sure to add any `.env` files you may create to this `.gitignore`.