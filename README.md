# Spotify App Extraction
### Spotify desktop builds (windows/linux/osx) *only tested on windows*

# What this is
This is a guide to decompiling, editing and making aditional pages to be added to spotify desktop versions. Currently I haven't explored this much but have found you can add pages which can be accessed via the search bar with the **spotify:** prefix. e.g. add a page called test which can be accessed by searching for **spotify:test**

# My ideas for use cases
- Custom spotify extensions built into the desktop app

# How to 
In the spotify directory (windows: ~\AppData\Roaming\Spotify\) there is a folder named **Apps**. This contains multiple .spa files, these are simply renamed .zip files (application/x-zip). Each contains a **manifest.json** and **index.html**, most of the time they contain **bundle.js** and a css folder.
These can be edited re-zipped (make sure they are in the base directory of zip folder), renamed to .spa and dropped straight back into the apps folder where they will be run next time spotify is launched.

**(It doesn't matter the name of the .spa file it will be loaded if it is in the Apps folder)**

# Examples
The manifest.json files look something like this ( [skip](#end-manifest) )
```javascript
{
  "BundleIdentifier": "test",
  "BundleType": "Application",
  "BundleVersion": "0.1",
  "VendorIdentifier": "com.spotify",
  "UserInstallable": false,
  "AppDescription": {
    "en": "",
    "cs": "",
    "de": "",
    "el": "",
    "es": "",
    "es-419": "",
    "fi": "",
    "fr": "",
    "fr-CA": "",
    "hu": "",
    "id": "",
    "it": "",
    "ja": "",
    "nl": "",
    "pl": "",
    "pt-BR": "",
    "sv": "",
    "th": "",
    "tr": "",
    "vi": "",
    "zh-Hant": "",
    "zsm": ""
  },
  "AppName": {
    "en": "Test",
    "cs": "Test",
    "de": "Test",
    "el": "Test",
    "es": "Test",
    "es-419": "Test",
    "fi": "Test",
    "fr": "Test",
    "fr-CA": "Test",
    "hu": "Test",
    "id": "Test",
    "it": "Test",
    "ja": "Test",
    "nl": "Test",
    "pl": "Test",
    "pt-BR": "Test",
    "sv": "Test",
    "th": "Test",
    "tr": "Test",
    "vi": "Test",
    "zh-Hant": "Test",
    "zsm": "Test"
  },
  "SupportedLanguages": [
    "cs",
    "de",
    "el",
    "en",
    "es",
    "es-419",
    "fi",
    "fr",
    "fr-CA",
    "hu",
    "id",
    "it",
    "ja",
    "nl",
    "pl",
    "pt-BR",
    "sv",
    "th",
    "tr",
    "vi",
    "zh-Hant",
    "zsm"
  ],
  "SupportedDeviceClasses": [
    "Desktop"
  ],
  "BridgeDependencies": {
    "bridge-desktop": "0.25.0",
    "bridge-web": "2.50.0",
    "bridge-zelda": "1.0.0"
  },
  "Dependencies": {
    "api": "1.0.0"
  },
  "InjectScripts": false,
  "InjectStylesheets": false,
  "SkipLanguageValidation": true,
  "SkipUnrequireValidation": true,
  "SpmApp": true,
  "GitRevision": "1fcff12"
}
```
###### end-manifest
| Key | Explanation |
| :---: | :--- |
| **Bundle-Identifier** | will change what you must type into the search bar after **spotify:** to open **index.html** |
| **InjectScripts** | Haven't tested this yet |
| **InjectStylesheets** | Haven't tested this yet |
| **AppName** | Not sure what this is for |
| **Everything else** | I have just left as is because is the same in all other apps |

---
# unzip.py
This short python script will extract everything that is a zipfile in the data directory to the output directory. As seen with test.spa.
