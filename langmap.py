#Language Map Maker
#ShotgunOverbeck, 2015.03.19

try:
	import sys
	import os
	import tkinter as tk
	from translate import Translator
	import random
	import webbrowser
	import threading
	import queue
	from transliterateScripts import *
except Exception as error:
	print('Error importing dependencies: ' + str(error))
	input('Press enter to quit: ')
	sys.exit()

threadQueue = queue.Queue()

def openSOHomepage():
	webbrowser.open_new('http://shotgunoverbeck.com')

class countryData:
	def __init__(self, name, posX, posY, langName, langISO6391, langISO6393):
		self.name = name
		self.posX = posX
		self.posY = posY
		self.langName = langName
		self.langISO6391 = langISO6391
		self.langISO6393 = langISO6393

root = tk.Tk()
fontSizeV = tk.StringVar()
fontWeightV = tk.StringVar()
fontFamilyV = tk.StringVar()
errorTextV = tk.StringVar()
focusWordV = tk.StringVar()
outputLocationV = tk.StringVar()
textColorV = tk.StringVar()
romanizeRussianV = tk.IntVar()
romanizeRussianV.set(1)
romanizeArabicV = tk.IntVar()
romanizeArabicV.set(1)
romanizeGreekV = tk.IntVar()
romanizeGreekV.set(1)
romanizeHebrewV = tk.IntVar()
romanizeHebrewV.set(1)
romanizeArmenianV = tk.IntVar()
romanizeArmenianV.set(1)
romanizeGeorgianV = tk.IntVar()
romanizeGeorgianV.set(1)
romanizeBelarusianV = tk.IntVar()
romanizeBelarusianV.set(1)
romanizeSerbianV = tk.IntVar()
romanizeSerbianV.set(1)
romanizeBulgarianV = tk.IntVar()
romanizeBulgarianV.set(1)
romanizeKazakhV = tk.IntVar()
romanizeKazakhV.set(1)
romanizeMacedonianV = tk.IntVar()
romanizeMacedonianV.set(1)
romanizeUkrainianV = tk.IntVar()
romanizeUkrainianV.set(1)
romanizePersianV = tk.IntVar()
romanizePersianV.set(1)
wordLangV = tk.StringVar()
wordFormatV = tk.StringVar()
transliteratedWordFormatV = tk.StringVar()
makePNGV = tk.IntVar()

euroLanguageData = [
	countryData('Albania', 1159, 1274, 'Albanian', 'sq', 'sqi'),
	countryData('Algeria', 682, 1478, 'Arabic', 'ar', 'ara'),
	countryData('Andorra', 672, 1225, 'Catalan', 'ca', 'cat'),
	countryData('Armenia', 1798, 1093, 'Armenian', 'hy', 'hye'),
	countryData('Austria', 996, 1068, 'German', 'de', 'deu'),
	countryData('Azerbaijan', 1868, 1057, 'Azerbaijani', 'az', 'aze'),
	countryData('Basque Country', 578, 1202, 'Basque', 'eu', 'eus'),
	countryData('Belarus', 1262, 816, 'Belarusian', 'be', 'bel'),
	countryData('Belgium', 771, 949, 'French', 'fr', 'fra'),
	countryData('Bosnia', 1092, 1174, 'Bosnian', 'bs', 'bos'),
	countryData('Bulgaria', 1285, 1198, 'Bulgarian', 'bg', 'bul'),
	countryData('Croatia', 1054, 1124, 'Croatian', 'hr', 'hrv'),
	countryData('Cyprus', 1563, 1400, 'Greek', 'el', 'ell'),
	countryData('Czech Republic', 1006, 978, 'Czech', 'cs', 'ces'),
	countryData('Denmark', 877, 766, 'Danish', 'da', 'dan'),
	countryData('England', 650, 782, 'English', 'en', 'eng'),
	countryData('Estonia', 1182, 633, 'Estonian', 'et', 'est'),
	countryData('Faroe Islands', 616, 508, 'Faroese', 'fo', 'fao'),
	countryData('Finland', 1150, 481, 'Finnish', 'fi', 'fin'),
	countryData('France', 710, 1094, 'French', 'fr', 'fra'),
	countryData('Georgia', 1740, 1058, 'Georgian', 'ka', 'kat'),
	countryData('Germany', 893, 946, 'German', 'de', 'deu'),
	countryData('Gibraltar', 438, 1418, 'English', 'en', 'eng'),
	countryData('Greece', 1232, 1326, 'Greek', 'el', 'ell'),
	countryData('Greenland', 300, 93, 'Kalaallisut', 'kl', 'kal'),
	countryData('Hungary', 1112, 1066, 'Hungarian', 'hu', 'hun'),
	countryData('Iceland', 478, 363, 'Icelandic', 'is', 'isl'),
	countryData('Iran', 1934, 1185, 'Persian', 'fa', 'fas'),
	countryData('Iraq', 1872, 1353, 'Arabic', 'ar', 'ara'),
	countryData('Ireland', 524, 820, 'Irish', 'ga', 'gle'),
	countryData('Israel', 1648, 1478, 'Hebrew', 'he', 'heb'),
	countryData('Italy', 963, 1238, 'Italian', 'it', 'ita'),
	countryData('Jordan', 1692, 1472, 'Arabic', 'ar', 'ara'),
	countryData('Kaliningrad Oblast', 1129, 790, 'Russian', 'ru', 'rus'),
	countryData('Kazakhstan', 1875, 700, 'Kazakh', 'kk', 'kaz'),
	countryData('Latvia', 1180, 701, 'Latvian', 'lv', 'lav'),
	countryData('Lebanon', 1650, 1412, 'Arabic', 'ar', 'ara'),
	countryData('Liechtenstein', 881, 1080, 'German', 'de', 'deu'),
	countryData('Lithuania', 1170, 757, 'Lithuanian', 'lt', 'lit'),
	countryData('Macedonia', 1207, 1250, 'Macedonian', 'mk', 'mkd'),
	countryData('Malta', 1017, 1468, 'Maltese', 'mt', 'mlt'),
	countryData('Moldova', 1337, 1018, 'Romanian', 'ro', 'ron'),
	countryData('Monaco', 815, 1198, 'French', 'fr', 'fra'),
	countryData('Montenegro', 1140, 1212, 'Montenegrin', '', ''),
	countryData('Morocco', 444, 1482, 'Arabic', 'ar', 'ara'),
	countryData('Netherlands', 792, 894, 'Dutch', 'nl', 'nld'),
	countryData('Norway', 885, 583, 'Norwegian', 'no', 'nor'),
	countryData('Occitania', 692, 1188, 'Occitan', 'oc', 'oci'),
	countryData('Poland', 1096, 891, 'Polish', 'pl', 'pol'),
	countryData('Portugal', 384, 1290, 'Portuguese', 'pt', 'por'),
	countryData('Romania', 1255, 1092, 'Romanian', 'ro', 'ron'),
	countryData('Russia', 1551, 500, 'Russian', 'ru', 'rus'),
	countryData('San Marino', 957, 1190, 'Italian', 'it' ,'ita'),
	countryData('Saudi Arabia', 1866, 1475, 'Arabic', 'ar', 'ara'),
	countryData('Serbia', 1173, 1173, 'Serbian', 'sr', 'srp'),
	countryData('Slovakia', 1104, 1012, 'Slovak', 'sk', 'slk'),
	countryData('Slovenia', 1006, 1116, 'Slovene', 'sl', 'slv'),
	countryData('Spain', 526, 1298, 'Spanish', 'es', 'spa'),
	countryData('Sweden', 975, 591, 'Swedish', 'sv', 'swe'),
	countryData('Switzerland', 854, 1090, 'German', 'de', 'deu'),
	countryData('Syria', 1713, 1352, 'Arabic', 'ar', 'ara'),
	countryData('Tunisia', 878, 1472, 'Arabic', 'ar', 'ara'),
	countryData('Turkey', 1567, 1248, 'Turkish', 'tr', 'tur'),
	countryData('Ukraine', 1380, 932, 'Ukrainian', 'uk', 'ukr'),
	countryData('Vatican City', 963, 1270, 'Latin', 'la', 'lat'),
	countryData('Wales', 595, 873, 'Welsh', 'cy', 'cym')
]

def getTextVariableInformation():
	print('Variables useable in text output:')
	print('abc123 - abc123')
	print('{{Language}} - Name of the language')
	print('{{Region}} - Name of the region')
	print('{{TranslatedWord}} - Translated (and romanized) word')
	print('{{OriginalWord}} - Translated word in its original script')
	print('Examples:')
	print('ERROR = ERROR')
	print('{{Language}}: {{TranslatedWord}} = English: hello')
	print('Done\n')

def listLanguageData():
	print('Mappable European regions (region name, language name)')
	for country in euroLanguageData:
		print(country.name + ', ' + country.langName)
	print('Done\n')

def checkLanguages():
	print('Checking language translation support')
	failTextPhrase = 'If this sentence is returned, then this lanuage cannot be translated correctly! Otherwise, you should be okay'
	languageList = []
	for country in euroLanguageData:
		if country.langISO6391 not in languageList:
			languageList.append(country)
	languageList = sorted(languageList)
	for country in languageList:
		translator = Translator(to_lang=country.langISO6391, from_lang='en')
		if translator.translate(failTextPhrase) == failTextPhrase and country.langISO6391 != 'en':
			print(country.langName+': NOT WORKING')
		else:
			print(country.langName+': working')
	print('Done\n')

def createMap():
	try:
		urlTestWord = Translator(to_lang='fr', from_lang='en').translate('hello')
	except Exception as error:
		print('Translation API was unable to connect to the translation servers. Check that you are connected to the internet, and then try again.')
		return
	global fontSizeV
	fontSize = int(fontSizeV.get())
	fontWeight = fontWeightV.get()
	fontFamily = fontFamilyV.get()
	errorText = errorTextV.get()
	focusWord = focusWordV.get()
	outputLocation = outputLocationV.get()
	textColor = textColorV.get()
	romanizeRussian = romanizeRussianV.get()
	romanizeArabic = romanizeArabicV.get()
	romanizeGreek = romanizeGreekV.get()
	romanizeHebrew = romanizeHebrewV.get()
	romanizeArmenian = romanizeArmenianV.get()
	romanizeGeorgian = romanizeGeorgianV.get()
	romanizeBelarusian = romanizeBelarusianV.get()
	romanizeSerbian = romanizeSerbianV.get()
	romanizeBulgarian = romanizeBulgarianV.get()
	romanizeKazakh = romanizeKazakhV.get()
	romanizeMacedonian = romanizeMacedonianV.get()
	romanizeUkrainian = romanizeUkrainianV.get()
	romanizePersian = romanizePersianV.get()
	wordLang = wordLangV.get()
	makePNG = makePNGV.get()
	wordFormat = wordFormatV.get()
	transliteratedWordFormat = transliteratedWordFormatV.get()

	ignoredCountries = ignoreCountriesBox.get(1.0, 'end-1c').split('\n')

	blankMap = open('maps/europe_map.svg', 'r')
	outMap = []
	for line in blankMap:
		outMap.append(line)
	lastLineSave = outMap[len(outMap)-1]
	del outMap[len(outMap)-1]
	print('Mapping: '+focusWord)
	for country in euroLanguageData:
		if country.name in ignoredCountries:
			print(country.name + ': ' + country.langName+' - Ignored')
			continue
		isError = False
		isTransliterated = False
		translatedWord = Translator(to_lang=country.langISO6391, from_lang=wordLang).translate(focusWord)
		originalWord = translatedWord
		infoOut = country.name + ': ' + country.langName
		if translatedWord == focusWord:
			failTextPhrase = 'If this sentence is returned, then this lanuage cannot be translated correctly! Otherwise, you should be okay'
			failTextPhrase = Translator(to_lang=wordLang, from_lang=wordLang).translate(failTextPhrase)
			translator = Translator(to_lang=country.langISO6391, from_lang=wordLang)
			if translator.translate(failTextPhrase) == failTextPhrase and country.langISO6391 != wordLang:
				infoOut += ' - Translation not supported'
				isError = True
		print(infoOut)

		rusScriptLangs = ['rus']
		if romanizeRussian and country.langISO6393 in rusScriptLangs:
			translatedWord = romanizeCharacters(rus_engDict, translatedWord, False)
			isTransliterated = True
		belScriptLangs = ['bel']
		if romanizeBelarusian and country.langISO6393 in belScriptLangs:
			translatedWord = romanizeCharacters(bel_engDict, translatedWord, False)
			isTransliterated = True
		ukrScriptLangs = ['ukr']
		if romanizeUkrainian and country.langISO6393 in ukrScriptLangs:
			translatedWord = romanizeCharacters(ukr_engDict, translatedWord, False)
			isTransliterated = True
		srpScriptLangs = ['srp']
		if romanizeSerbian and country.langISO6393 in srpScriptLangs:
			translatedWord = romanizeCharacters(srp_engDict, translatedWord, False)
			isTransliterated = True
		bulScriptLangs = ['bul']
		if romanizeBulgarian and country.langISO6393 in bulScriptLangs:
			translatedWord = romanizeCharacters(bul_engDict, translatedWord, False)
			isTransliterated = True
		mkdScriptLangs = ['mkd']
		if romanizeMacedonian and country.langISO6393 in mkdScriptLangs:
			translatedWord = romanizeCharacters(mkd_engDict, translatedWord, False)
			isTransliterated = True
		kazScriptLangs = ['kaz']
		if romanizeKazakh and country.langISO6393 in kazScriptLangs:
			translatedWord = romanizeCharacters(kaz_engDict, translatedWord, False)
			isTransliterated = True
		araScriptLangs = ['ara']
		if romanizeArabic and country.langISO6393 in araScriptLangs:
			translatedWord = romanizeCharacters(ara_engDict, translatedWord, False)
			isTransliterated = True
		fasScriptLangs = ['fas']
		if romanizePersian and country.langISO6393 in fasScriptLangs:
			translatedWord = romanizeCharacters(ara_engDict, translatedWord, False)
			isTransliterated = True
		ellScriptLangs = ['ell']
		if romanizeGreek and country.langISO6393 in ellScriptLangs:
			translatedWord = romanizeCharacters(ell_engDict, translatedWord, False)
			isTransliterated = True
		hebScriptLangs = ['heb']
		if romanizeHebrew and country.langISO6393 in hebScriptLangs:
			translatedWord = romanizeCharacters(heb_engDict, translatedWord, False)
			isTransliterated = True
		hyeScriptLangs = ['hye']
		if romanizeArmenian and country.langISO6393 in hyeScriptLangs:
			translatedWord = romanizeCharacters(hye_engDict, translatedWord, False)
			isTransliterated = True
		katScriptLangs = ['kat']
		if romanizeGeorgian and country.langISO6393 in katScriptLangs:
			translatedWord = romanizeCharacters(kat_engDict, translatedWord, False)
			isTransliterated = True

		if isTransliterated:
			wordOutput = transliteratedWordFormat
		else:
			wordOutput = wordFormat
		wordOutput = wordOutput.replace('{{Language}}', country.langName, len(wordOutput))
		wordOutput = wordOutput.replace('{{Region}}', country.name, len(wordOutput))
		wordOutput = wordOutput.replace('{{TranslatedWord}}', translatedWord, len(wordOutput))
		wordOutput = wordOutput.replace('{{OriginalWord}}', originalWord, len(wordOutput))
		if isError:
			wordOutput = errorText
		outMap.append('<text font-weight="'+fontWeight+'" font-family="'+fontFamily+'" font-size="'+str(fontSize)+'" x="'+str(round(country.posX - (0.25 * fontSize * len(wordOutput))))+'" y="'+str(country.posY + (0.5 * fontSize))+'" fill="'+str(textColor)+'">'+str(wordOutput)+'</text>\n')
	outMap.append(lastLineSave)
	print('Saving as .svg...')
	outputFile = open(outputLocation, 'w', encoding='utf-8')
	for line in outMap:
		outputFile.write(line)
	outputFile.close()
	if makePNG:
		print('Saving as .png...')
		try:
			import cairosvg
			outputFile = open(str(os.path.splitext(outputLocation)[0])+'.png', 'wb')
			cairosvg.svg2png(bytestring=''.join(outMap).encode('utf-8'), write_to=outputFile)
			outputFile.close()
		except ImportError as error:
			print('CairoSVG not found')
	print('Finished: '+focusWord+'\n')

def startMapCreation():
	mapThread = threading.Thread(target=createMap)
	mapThread.daemon = True
	mapThread.start()

def closeProgram():
	root.destroy()

def main():
	class Window(tk.Frame):
		def __init__(self, master=None):
			tk.Frame.__init__(self, master)
			settingsStartRow = 4
			standardFont = ('Courier New', 10)
			titleFont = ('Courier New', 10, 'underline')
			tk.Label(text='Language Mapper', font=standardFont).grid(row=1, column=0)
			tk.Button(text='- ShotgunOverbeck', font=standardFont, command=openSOHomepage).grid(row=2, column=0)
			
			tk.Label(text='', font=standardFont).grid(row=0, column=0)
			tk.Label(text='', font=standardFont).grid(row=settingsStartRow+6, column=0)
			tk.Label(text='          ', font=standardFont).grid(row=settingsStartRow, column=2)
			tk.Label(text='', font=standardFont).grid(row=settingsStartRow-1, column=7)
			tk.Label(text='', font=standardFont).grid(row=settingsStartRow+120, column=0)

			tk.Button(text='Map It!', fg='red', command=startMapCreation, font=standardFont).grid(row=1, column=2)
			tk.Button(text='Quit', command=closeProgram, font=standardFont).grid(row=2, column=2)
			tk.Label(text='Word:', font=standardFont).grid(row=1, column=3, sticky=tk.E)
			defaultWords = ['dog', 'walk', 'ball', 'man', 'woman', 'happy', 'sad', 'pineapple', 'hi', 'hello', 'goodbye', 'apple', 'tree', 'fish', 'thank you', 'crazy', 'English', 'Germany', 'book', 'red', 'blue', 'ocean', 'green']
			focusWordBox = tk.Entry(textvariable=focusWordV, width=25, font=standardFont)
			focusWordBox.grid(row=1,column=4, sticky=tk.W)
			focusWordBox.insert(0, random.choice(defaultWords))
			tk.Label(text='Output:', font=standardFont).grid(row=2, column=3, stick=tk.E)
			outputLocationBox = tk.Entry(textvariable=outputLocationV, width=25, font=standardFont)
			outputLocationBox.grid(row=2,column=4, sticky=tk.W)
			outputLocationBox.insert(0, 'output.svg')

			tk.Label(text='Romanization Settings', font=titleFont).grid(row=settingsStartRow, column=0)
			tk.Label(text='Russian:', font=standardFont).grid(row=settingsStartRow+1, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeRussianV).grid(row=settingsStartRow+1, column=1, sticky=tk.W)
			tk.Label(text='Greek:', font=standardFont).grid(row=settingsStartRow+2, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeGreekV).grid(row=settingsStartRow+2, column=1, sticky=tk.W)
			tk.Label(text='Arabic:', font=standardFont).grid(row=settingsStartRow+3, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeArabicV).grid(row=settingsStartRow+3, column=1, sticky=tk.W)
			tk.Label(text='Persian:', font=standardFont).grid(row=settingsStartRow+4, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizePersianV).grid(row=settingsStartRow+4, column=1, sticky=tk.W)
			tk.Label(text='Hebrew:', font=standardFont).grid(row=settingsStartRow+5, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeHebrewV).grid(row=settingsStartRow+5, column=1, sticky=tk.W)
			tk.Label(text='Armenian:', font=standardFont).grid(row=settingsStartRow+6, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeArmenianV).grid(row=settingsStartRow+6, column=1, sticky=tk.W)
			tk.Label(text='Georgian:', font=standardFont).grid(row=settingsStartRow+7, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeGeorgianV).grid(row=settingsStartRow+7, column=1, sticky=tk.W)
			tk.Label(text='Belarusian:', font=standardFont).grid(row=settingsStartRow+8, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeBelarusianV).grid(row=settingsStartRow+8, column=1, sticky=tk.W)
			tk.Label(text='Ukrainian:', font=standardFont).grid(row=settingsStartRow+9, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeUkrainianV).grid(row=settingsStartRow+9, column=1, sticky=tk.W)
			tk.Label(text='Serbian:', font=standardFont).grid(row=settingsStartRow+10, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeSerbianV).grid(row=settingsStartRow+10, column=1, sticky=tk.W)
			tk.Label(text='Macedonian:', font=standardFont).grid(row=settingsStartRow+11, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeMacedonianV).grid(row=settingsStartRow+11, column=1, sticky=tk.W)
			tk.Label(text='Kazakh:', font=standardFont).grid(row=settingsStartRow+12, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeKazakhV).grid(row=settingsStartRow+12, column=1, sticky=tk.W)
			tk.Label(text='Bulgarian:', font=standardFont).grid(row=settingsStartRow+13, column=0, sticky=tk.E)
			tk.Checkbutton(master, variable=romanizeBulgarianV).grid(row=settingsStartRow+13, column=1, sticky=tk.W)

			tk.Label(text='Font Settings', font=titleFont).grid(row=settingsStartRow, column=3)
			tk.Label(text='Text Color: ', font=standardFont).grid(row=settingsStartRow+1, column=3, sticky=tk.E)
			textColorBox = tk.Entry(textvariable=textColorV, font=standardFont, width=25)
			textColorBox.grid(row=settingsStartRow+1, column=4, sticky=tk.W)
			textColorBox.insert(0, 'red')
			tk.Label(text='Font Size: ', font=standardFont).grid(row=settingsStartRow+2, column=3, sticky=tk.E)
			fontSizeBox = tk.Entry(textvariable=fontSizeV, width=25, font=standardFont)
			fontSizeBox.grid(row=settingsStartRow+2,column=4, sticky=tk.W)
			fontSizeBox.insert(0, 16)
			tk.Label(text='Font Family: ', font=standardFont).grid(row=settingsStartRow+3, column=3, sticky=tk.E)
			fontFamilyBox = tk.Entry(textvariable=fontFamilyV, width=25, font=standardFont)
			fontFamilyBox.grid(row=settingsStartRow+3,column=4, sticky=tk.W)
			fontFamilyBox.insert(0, 'monospace')
			tk.Label(text='Font Weight: ', font=standardFont).grid(row=settingsStartRow+4, column=3, sticky=tk.E)
			fontWeightBox = tk.Entry(textvariable=fontWeightV, width=25, font=standardFont)
			fontWeightBox.grid(row=settingsStartRow+4,column=4, sticky=tk.W)
			fontWeightBox.insert(0, 'normal')

			tk.Label(text='More Settings', font=titleFont).grid(row=settingsStartRow+6, column=3)
			tk.Label(text='Text Var. Info:', font=standardFont).grid(row=settingsStartRow+7, column=3, sticky=tk.E)
			tk.Button(text='Click', command=getTextVariableInformation, font=standardFont).grid(row=settingsStartRow+7, column=4, sticky=tk.W)
			tk.Label(text='Output Text: ', font=standardFont).grid(row=settingsStartRow+8, column=3, sticky=tk.E)
			errorTextBox = tk.Entry(textvariable=wordFormatV, width=25, font=standardFont)
			errorTextBox.grid(row=settingsStartRow+8,column=4, sticky=tk.W)
			errorTextBox.insert(0, '{{TranslatedWord}}')
			tk.Label(text='Romanized Text: ', font=standardFont).grid(row=settingsStartRow+9, column=3, sticky=tk.E)
			errorTextBox = tk.Entry(textvariable=transliteratedWordFormatV, width=25, font=standardFont)
			errorTextBox.grid(row=settingsStartRow+9,column=4, sticky=tk.W)
			errorTextBox.insert(0, '{{TranslatedWord}}')
			tk.Label(text='Error Text: ', font=standardFont).grid(row=settingsStartRow+10, column=3, sticky=tk.E)
			errorTextBox = tk.Entry(textvariable=errorTextV, width=25, font=standardFont)
			errorTextBox.grid(row=settingsStartRow+10,column=4, sticky=tk.W)
			errorTextBox.insert(0, '')
			tk.Label(text='Input Language: ', font=standardFont).grid(row=settingsStartRow+11, column=3, sticky=tk.E)
			wordLangVBox = tk.Entry(textvariable=wordLangV, width=25, font=standardFont)
			wordLangVBox.grid(row=settingsStartRow+11,column=4, sticky=tk.W)
			wordLangVBox.insert(0, 'en')
			tk.Label(text='PNG (CairoSVG): ', font=standardFont).grid(row=settingsStartRow+12, column=3, sticky=tk.E)
			tk.Checkbutton(master, variable=makePNGV).grid(row=settingsStartRow+12, column=4, sticky=tk.W)
			tk.Label(text='See Lang. Support:', font=standardFont).grid(row=settingsStartRow+13, column=3, sticky=tk.E)
			tk.Button(text='Click', command=checkLanguages, font=standardFont).grid(row=settingsStartRow+13, column=4, sticky=tk.W)
			tk.Label(text='List Map Regions:', font=standardFont).grid(row=settingsStartRow+14, column=3, sticky=tk.E)
			tk.Button(text='Click', command=listLanguageData, font=standardFont).grid(row=settingsStartRow+14, column=4, sticky=tk.W)
			tk.Label(text='Ignore Regions:', font=standardFont).grid(row=settingsStartRow+15, column=3, sticky=tk.NE)
			global ignoreCountriesBox
			ignoreCountriesBox = tk.Text(height=5, width=25, font=standardFont)
			ignoreCountriesBox.grid(row=settingsStartRow+15, column=4, columnspan=5, sticky=tk.W)
			ignoreCountriesBox.insert(1.0, 'Gibraltar\nLiechtenstein\nSan Marino')

	mainWindow = Window(master=root)
	root.wm_title('Language Mapper - ShotgunOverbeck')
	mainWindow.mainloop()

try:
	main()
except Exception as error:
	print('Error: ' + str(error))
	input('Press enter to exit: ')
	sys.exit()