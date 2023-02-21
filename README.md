# Neos Locale
This repository contains the locale assets for the core UI of Neos VR (www.neos.com) and allow anyone to contribute translations. The contents of this repository will be periodically merged with the public build released on Steam (https://store.steampowered.com/app/740250/Neos_VR/) and other platforms.

# Localization Status
Czech [cs] - 100.0% - Missing keys: 0  
German [de] - 96.2% - Missing keys: 66  
English (United Kingdom) [en-gb] - 2.0% - Missing keys: 1724  
English [en] - 100.0% - Missing keys: 0  
Esperanto [eo] - 83.7% - Missing keys: 287  
Spanish [es] - 99.3% - Missing keys: 13  
Estonian [et] - 59.3% - Missing keys: 716  
Finnish [fi] - 90.4% - Missing keys: 168  
French [fr] - 83.8% - Missing keys: 285  
Icelandic [is] - 33.9% - Missing keys: 1163  
Japanese [ja] - 100.0% - Missing keys: 0  
Korean [ko] - 100.0% - Missing keys: 0  
Dutch [nl] - 94.4% - Missing keys: 98  
Norwegian [no] - 47.1% - Missing keys: 930  
Polish [pl] - 77.8% - Missing keys: 390  
Russian [ru] - 100.0% - Missing keys: 0  
Swedish [sv] - 14.2% - Missing keys: 1510  
Turkish [tr] - 55.4% - Missing keys: 784  
Chinese (China) [zh-cn] - 100% - Missing keys: 0  
Chinese (Taiwan) [zh-tw] - 65.2% - Missing keys: 613  

Total keys: 1804

# How To Contribute
If you'd like to contribute translations, create a branch of fork of the repository, make the changes and once they are ready to be merged create a Pull Request, so the contributions can be checked and merged. You don't need to translate everything at once, if you cover part of the UI, the changes can be merged, with more translations coming later.

# Do's and don'ts
- Make sure the .json locale file is UTF8 encoded
- Always keep the "Dummy" : "Dummy" entry at the bottom of the file. This way you don't have to remember to remove the comma at the end of the last entry every time
- Copy & Paste the whole content of the file into this online validator to ensure you don't have any syntax errors: https://jsonformatter.curiousconcept.com/
- DO use spaces instead of tabs to keep the formatting of all documents consistent
- DO check if other users are making modifications to the same locale as you are in Issues and coordinate. If you send changes that conflict with other users, it's hard to resolve them on our end since we don't understand the language.
- DO keep the same style of formating and coloring where it's present in the text to ensure it stays consistent across locales. Coloring in particular can be contextual and used in other parts of the UI and changing or removing it would cause user confusion.

- DON'T update the Localization Status section of this document, it is automatically generated when changes are merged
- DON'T update the MISSING.md file manually, it's automatically generated as part of the build process based on the changes you submit
- DON'T convert the formatting of the entire document. This creates major merge conflicts and makes it hard to track what was actually changed, plus it introduces inconsistencies
- DON'T correct mistakes in the string keys, only report them. They will be fixed by a script, which will apply the correction to all locales at once.
- DON'T submit purely machine translated locales. Those often result in odd and confusing results for user interfaces. Using machine translation as basis for manual translation is ok.

# Translating the Store descriptions
If you're like, you can help translate the store descriptions as well (this is used on Steam for example), but we consider those highly optional since it's quite a lot of text. If you don't want to translate those, don't worry about them! The store descriptions do not count towards the translation completeness percerntage and are provided in separate files.

If you do translate them and you haven't added a credit yet, put your name in the regular .json file for translations of in-game strings, even if you haven't translated any in-game strings.

# If you're contributing a new language
1) Create a new Issue (https://github.com/Neos-Metaverse/NeosLocale/issues) for given language in format "Language [lang-code]", for example "English [en]", which will help coordinate efforts of different translators.

2) Verify that Neos' fork of ICU MessageFormat.NET has pluralizer for your language, by checking the "AddStandardPluralizers()" function in this file: https://github.com/Neos-Metaverse/messageformat.net/blob/master/src/Jeffijoe.MessageFormat/Formatting/Formatters/PluralFormatter.cs

If you can't find your language code in this file, please make a Issue either on the official Neos issue tracker (https://github.com/Neos-Metaverse/NeosPublic/issues) or in this repository.

Alternatively you can implement the pluralizer yourself based on the reference from the Unicode CLDR repository: https://github.com/unicode-org/cldr/blob/master/common/supplemental/plurals.xml and make a pull request for it to be merged with our fork or MessageFormat.NET

3) Add a new [lang-code].json file to your fork. We highly recommend creating a skeleton file first without any translation strings, just containing the Locale and Authors and creating a pull request, so it's clearer to other contributors that translations are being worked on by someone.

# Contributing translations to a language
If you'd like to contribute translations for existing language file (or one you have just created), we recommend the following:

1) Make a fork of the repository or your own branch.
2) Update the language file, either by modifying the translation strings or adding new ones for missing translations.
3) Ensure you do not have any left-over English strings in the file. Your file should only contain actually translated strings. Any missing strings will automatically fallback (see below for details)
4) Ensure your modified translation file works correctly in Neos (see below how to test)
5) Create a Pull Request for your translations to be merged into the main repository. After merging they will be available publicly in the next public build of Neos.

As Neos develop, we'll be constantly adding new strings in English or modifying the existing ones. We recommend watching the repository for activity through GitHub, so you can get notified when there are changes and new strings to be translated.

# Testing your translation in Neos
As you work on the translation we recommend that you periodically check it inside of Neos. This will not only help ensure that you don't have any syntax errors, but also make sure that the strings are correct in the context.

To test the translation, find folder where Neos.exe is installed (on Steam, you can do so by right clicking Neos, going to Properties -> LOCAL FILES -> BROWSE LOCAL FILES...) and then locate the "Locale" folder. Simply place your modified file into this folder and Neos will load it up.

By default, Neos uses your system locale to determine which file to load. You can override this by going to Settings and changing the "Override Locale" to a different language code.

- You can edit the translation file on the fly without shutting down Neos. To force it to reload, change the locale to "en" and then back to your own.
- Note that while most UI will change language immediately, not all of it would. Simply close and reopen the UI dialog to load the translated strings
- If the string is showing in English, you probably have a typo in the string key. It needs to match exactly
- If the translation isn't loading in Neos, it is likely JSON syntax error preventing it from being loaded
- If you see "ERROR!!!" instead of your translated string, you have a syntax error in the particular string. Check Neos' log file, which will contain details.

# The ICU MessageFormat Syntax for translation strings
Neos uses the ICU MessageFormat Syntax defined by the Unicode organization for its localized strings. This offers high amount of flexibility on how you translate strings and ensures that you can correctly follow the grammar rules of your language, particularly with regards to pluralization (e.g. displaying "1 item" vs "1 items"). This is why it's important to ensure that your language has a pluralizer implemented in our fork of MessageFormat.NET

To learn more about the ICU MessageFormat Syntax check the following links:
https://unicode-org.github.io/icu/userguide/format_parse/messages/

Formatting guide with examples (the C# version of the library currently doesn't implement all the formatters, but they will be added as needed):
https://messageformat.github.io/messageformat/page-guide

Language pluralization rules:
https://github.com/unicode-org/cldr/blob/master/common/supplemental/plurals.xml

Typically most strings are straight up replacements, with no complex syntax. Some use just a simple variable replacement (e.g. {name}), which will replace part of the message with given variable.

For cases when the structure of sentence changes based on the value of a number, you'll see pattern {variable, plural, ...}. Each language has a set of plural categories, like zero, one, two, few, many and other. Some languages have only "other", some (like English) have "one" and "other", while other languages have multiple. Make sure that you familiarize yourself with the plural categories in your language (using the links above) so you can correctly translate strings using this syntax.

Another common syntax is using the {variable, select, ...} form. This lets you match the variable against specific values and provide translated versions of each. You can either replace a single word (e.g. "Server status is {status, select, good {Good} bad {Not Good} }") or the whole sentence (e.g. "{status, select, good {Server is good!} bad {Oh no, servers are down!}}") depending on what works better in your language.

Please let us know if you have any questions or are unsure about certain things.

# Language codes and fallbacks
Neos uses the IETF language tags (https://en.wikipedia.org/wiki/IETF_language_tag) to load locales. These consist of a single primary language tag (typically two-letter language code from ISO 639-1 or a three-letter code from ISO 639-2 (1998), ISO 639-3 (2007) or ISO 639-5 (2008)) and and optional region subtag with country code.

When loading locale file, Neos will first check for the most specific locale file. Then it will load any missing strings from the general locale file and last it will load any missing strings from the English locale.

For example if your system locale is British English (en-gb), it will first look for "en-gb.json" file and then for the more general one "en.json".

We recommend putting most translations into the general language file (single two letter or three letter code) and if necessary only put specific overrides into the more specific language file. That way, most translations can be shared across variants of the language if possible.

Any strings you don't translate at all will also fall back into their English variants, so you don't have to worry about missing some of them, they can be translated later (or by another contributor). This also ensures that newly added strings in the English will show up and can be gradually translated as they come.

# What if I find string that cannot be translated?
While majority of Neos' UI has been converted to the localization system, there are likely a few stragglers and some parts that aren't translatable right now. If you encounter such place, create an Issue on this repository, ideally with screenshot of the non-translatable part, so we can convert it as well.

Currently there are a few known parts that cannot be translated, but are planned to:
- Enumerations (e.g. certain tool options that cycle through several options)
- Component names and categories (component names will still show original for technical reasons, but will show optional translation for non-English languages)
- LogiX node names and categories (same as above)
- Component fields (those will only show optional translated names on hover once tooltip system is implemented)

# If you use an external tool to do the translation and the JSON structure is mangled
You can use the python script in this repository: CleanJSON.py

For example to clean the french json, `./CleanJSON.py --en en.json --lang fr.json --out fr.json.cleaned`

```usage: CleanJSON.py [-h] [--en en_path] [--lang lang_path] [--out out_path]

This script will reformat a Babel style JSON for locales to match the en.json
baseline formating for git changes purposes.

optional arguments:
  -h, --help        show this help message and exit
  --en en_path      The path to the en.json Neos locale.
  --lang lang_path  The path to the LANG.json Neos locale to clean.
  --out out_path    The path to save the formated file.
```

# Any questions?
If you have questions or are unsure about something, you can create an Issue on this repository or reach out to our team on the official Discord: https://discord.gg/neosvr
