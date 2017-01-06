Language Mapper - Shotgun Overbeck
http://shotgunoverbeck.com/

ABOUT
#####

Language Mapper is an attempt to automate the creation of maps depicting the geography of different Indo-European languages. Given an English word, it will map the word in different countries' national language. It provides a simple GUI with a few customization options. The output will be a .svg vector image, consisting of the words overlaid on a politican map of Europe and western Asia. The map image used is from the Wikipedia Commons (http://commons.wikimedia.org/wiki/File:Europe_political_chart_complete_blank.svg), where it is licensed under the GNU Free Documentation license. This map is current as of 2009; changes in borders after this will not be shown.

UPDATE: Changes to Google Translate have made this project defunct.

TRANSLATION
###########

Translation is done by Google Translate, and thus only languages supported by Google Translate can be used. Any problems with translation are a result of a fault in the translation service, not this script. The computer must be able to connect to Google Translate's servers in order to use Language Mapper.

Non-Latin script can be automatically romanized to be more easily readable to English speakers. These transliterations are not guaranteed to be entirely correct. Unrecognized characters cannot be correctly translated to their Latin equivalents. Romanization of non-Latin scripts is created from data provided by the Unicode Consortium (http://unicode.org/repos/cldr/trunk/common/transforms/).

LICENSE
#######

This work is licensed under a Creative Commons Attribution 4.0 International License. Use as needed. Do not redistrubute. More information can be found on the Creative Commons website (http://creativecommons.org/licenses/by/4.0/legalcode).

REQUIREMENTS
############

Python Package:
	* Python 3.4+
	* Terryyin's Google-Translate-Python (https://github.com/terryyin/google-translate-python)
	* Tkinter (http://www.tkdocs.com/tutorial/install.html)
	* CairoSVG (Optional, for PNG output) (http://cairosvg.org/)
	* Internet connection (for connection to the translation service)

Windows Executable:
	* Windows XP+
	* Cairo Graphics (Optional, for PNG output) (http://cairographics.org/)
	* Internet connection (for connection to the translation service)

USAGE
#####

Run langmap.py (Python package) or langmap.exe (Windows executable), in the same directory as this file. The console window that opens next to the grey GUI will function as output for information about Language Mapper. Settings can be customized from the grey GUI window. The entry field labelled "Word" to the top-right of the window is the entry for the word that you wish to map. Once the settings are properly customized, press the red 'Map It!' button to the top of the window to generate the map. This may take a short time (maximum 30 seconds). Progress and errors may be tracked via the console window. The map will be saved in the same directory as Language Mapper as a .svg file. This .svg can be opened in many different programs, but it can be opened in most web browsers. A .png copy can be made if the 'PNG (CairoSVG)' checkbox is selected during mapping.

Explanation of Settings:

Romanization Settings: Toggle the automatic romanization of languages in non-Latin scripts on and off using the checkboxes.

Font Settings: Changes the font used on the map to display the word translations. All settings must be valid within a .svg file.

Output Text: Changes the format for the word displays on the map. This can be customized with certain variables, for example {{TranslatedWord}} will be replaced with the word translation. More information about these variables can be found by clicking 'Text Var. Info'.

Romanized Text: The same as Output Text, except for words whose translation has been romanized.

Error Text: The text to display in place of a word whose translation failed.

Input Language: The ISO-6391 code for the language of the input word. This is by default English ('en').

PNG (CairoSVG): Toggle whether or not to save a .png copy of the .svg file should be made. This will require support for the Python library CairoSVG. Some non-Latin characters may not show correctly in this .png.

See Lang. Support: Checks which languages can and cannot be properly translated. Results are printed to the console window.

List Map Regions: Writes a list of all used regions and their respective languages to the console window.

Ignore Regions: List region names (as named in 'List Map Regions'), separated by a line break, to ignore when mapping. This can be used to remove unwanted regions from the map. It is best used for microstates whose national language is identical to the region around them, and thus do not have so much need for a separate label.

Please note that this is a hobby project. It is not idiot proof. It can be glitchy, the output is not always pretty, the code is messy, and there may be unexpected errors. If you have any tips, possible improvements, or other comments, feel free to email me at joe@shotgunoverbeck.com.