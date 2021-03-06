def romanizeCharacters(translationDict, text, isReversed):
	if isReversed:
		text = text[::1]
	#Sort by length, so that combined glyphs get romanized together
	for rule in sorted(translationDict, key=lambda k: len(k), reverse=True):
		text = text.replace(rule, translationDict[rule])
	return text

rus_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'G',
	'г':'g',
	'Д':'D',
	'д':'d',
	'Е':'Ye',
	'Е':'E',
	'е':'ye',
	'е':'e',
	'Ё':'Yë',
	'Ё':'Ë',
	'ё':'yë',
	'ё':'ë',
	'Ж':'Zh',
	'ж':'zh',
	'З':'Z',
	'з':'z',
	'И':'I',
	'и':'i',
	'Й':'Y',
	'й':'y',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'С':'S',
	'с':'s',
	'ТС':'TS',
	'Тс':'Ts',
	'тс':'ts',
	'Т':'T',
	'т':'t',
	'У':'U',
	'у':'u',
	'Ф':'F',
	'ф':'f',
	'Х':'Kh',
	'х':'kh',
	'Ц':'Ts',
	'ц':'ts',
	'Ч':'Ch',
	'ч':'ch',
	'ШЧ':'SHCH',
	'Шч':'Shch',
	'шч':'shch',
	'Ш':'Sh',
	'ш':'sh',
	'Щ':'Shch',
	'Щ':'SHCH',
	'щ':'shch',
	'Ъ':'ʺ',
	'ъ':'ʺ',
	'Ы':'Y',
	'ы':'y',
	'Ь':'ʹ',
	'ь':'ʹ',
	'Э':'E',
	'э':'e',
	'Ю':'Yu',
	'ю':'yu',
	'Я':'Ya',
	'я':'ya'
}

bel_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'H',
	'г':'h',
	'Д':'D',
	'д':'d',
	'Е':'Ye',
	'е':'ye',
	'Ё':'Yo',
	'ё':'yo',
	'Ж':'Zh',
	'ж':'zh',
	'ЗГ':'Z·H',
	'Зг':'Z·h',
	'зг':'z·h',
	'З':'Z',
	'І':'I',
	'і':'i',
	'Й':'Y',
	'й':'y',
	'КГ':'K·H',
	'Кг':'K·h',
	'кг':'k·h',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'СГ':'S·H',
	'Сг':'S·h',
	'сг':'s·h',
	'С':'S',
	'с':'s',
	'ТС':'T·S',
	'Тс':'T·s',
	'тс':'t·s',
	'Т':'T',
	'т':'t',
	'У':'U',
	'у':'u',
	'Ў':'W',
	'ў':'w',
	'Ф':'F',
	'ф':'f',
	'Х':'Kh',
	'х':'kh',
	'ЦГ':'TS·H',
	'Цг':'Ts·h',
	'цг':'ts·h',
	'Ц':'Ts',
	'Ц':'TS',
	'ц':'ts',
	'Ч':'Ch',
	'ч':'ch',
	'Ы':'Y',
	'ы':'y',
	'Ь':'ʹ',
	'ь':'ʹ',
	'Э':'E',
	'э':'e',
	'Ю':'Yu',
	'ю':'yu',
	'Я':'Ya',
	'я':'ya',
	'’':'ʺ',
	'Ґ':'G',
	'ґ':'g'
}

srp_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'G',
	'г':'g',
	'Д':'D',
	'д':'d',
	'Ђ':'Đ',
	'ђ':'đ',
	'Е':'E',
	'е':'e',
	'Ж':'Ž',
	'ж':'ž',
	'З':'Z',
	'з':'z',
	'И':'I',
	'и':'i',
	'Ј':'J',
	'ј':'j',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'Љ':'Lj',
	'љ':'lj',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'Њ':'Nj',
	'њ':'nj',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'С':'S',
	'с':'s',
	'Т':'T',
	'т':'t',
	'Ћ':'Ć',
	'ћ':'ć',
	'У':'U',
	'у':'u',
	'Ф':'F',
	'ф':'f',
	'Х':'H',
	'х':'h',
	'Ц':'C',
	'ц':'c',
	'Ч':'Č',
	'ч':'č',
	'Џ':'Dž',
	'џ':'dž',
	'Ш':'Š',
	'ш':'š'
}

bul_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'G',
	'г':'g',
	'Д':'D',
	'д':'d',
	'Е':'E',
	'е':'e',
	'Ж':'Zh',
	'ж':'zh',
	'З':'Z',
	'з':'z',
	'И':'I',
	'и':'i',
	'Й':'Y',
	'й':'y',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'С':'S',
	'с':'s',
	'ТС':'T·S',
	'Тс':'T·s',
	'тс':'t·s',
	'Т':'T',
	'т':'t',
	'У':'U',
	'у':'u',
	'Ф':'F',
	'ф':'f',
	'Х':'Kh',
	'х':'kh',
	'Ц':'Ts',
	'ц':'ts',
	'Ч':'Ch',
	'ч':'ch',
	'ШТ':'SH·T',
	'Шт':'Sh·t',
	'шт':'sh·t',
	'Ш':'Sh',
	'ш':'sh',
	'Щ':'Sht',
	'щ':'sht',
	'Ъ':'Ŭ',
	'ъ':'ŭ',
	'Ь':'’',
	'ь':'’',
	'Ю':'Yu',
	'ю':'yu',
	'Я':'Ya',
	'я':'ya',
	'Ѫ':'Ŭ',
	'ѫ':'ŭ',
	'Ѣ':'Ye',
	'ѣ':'ye'
}

mkd_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'G',
	'г':'g',
	'Д':'D',
	'д':'d',
	'Ѓ':'G',
	'ѓ':'g',
	'Е':'E',
	'е':'e',
	'Ж':'Ž',
	'ж':'ž',
	'З':'Z',
	'з':'z',
	'Ѕ':'Dz',
	'ѕ':'dz',
	'И':'I',
	'и':'i',
	'Ј':'J',
	'ј':'J',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'Љ':'Lj',
	'љ':'lj',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'Њ':'Nj',
	'њ':'nj',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'С':'S',
	'с':'s',
	'Т':'T',
	'т':'t',
	'Ќ':'Ć',
	'ќ':'ć',
	'У':'U',
	'у':'u',
	'Ф':'F',
	'ф':'f',
	'Х':'H',
	'х':'h',
	'Ц':'C',
	'ц':'c',
	'Ч':'Č',
	'ч':'č',
	'Џ':'Dž',
	'џ':'dž',
	'Ш':'Š',
	'ш':'š'
}

kaz_engDict = {
	'А':'A',
	'а':'a',
	'Ә':'Ä',
	'ә':'ä',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'ГҺ':'G·H',
	'Гһ':'G·h',
	'гһ':'g·h',
	'Г':'G',
	'г':'g',
	'Ғ':'Gh',
	'ғ':'gh',
	'Д':'D',
	'д':'d',
	'Е':'E',
	'е':'e',
	'Ё':'Yo',
	'ё':'yo',
	'Ж':'Zh',
	'ж':'zh',
	'ЗҺ':'Z·H',
	'Зһ':'Z·h',
	'зһ':'z·h',
	'З':'Z',
	'з':'z',
	'И':'Ī',
	'и':'ī',
	'Й':'Y',
	'й':'y',
	'КҺ':'K·H',
	'Кһ':'K·h',
	'кһ':'k·h',
	'К':'K',
	'к':'k',
	'Қ':'Q',
	'қ':'q',
	'Л':'L',
	'л':'l',
	'М':'M',
	'м':'m',
	'НГ':'N·G',
	'Нг':'N·g',
	'нг':'n·g',
	'Н':'N',
	'н':'n',
	'Ң':'Ng',
	'ң':'ng',
	'О':'O',
	'о':'o',
	'Ө':'Ö',
	'ө':'ö',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'СҺ':'S·H',
	'Сһ':'S·h',
	'сһ':'s·h',
	'С':'S',
	'с':'s',
	'Т':'T',
	'т':'t',
	'У':'Ū',
	'у':'ū',
	'Ұ':'U',
	'ұ':'u',
	'Ү':'Ü',
	'ү':'ü',
	'Ф':'F',
	'ф':'f',
	'Х':'Kh',
	'х':'kh',
	'Һ':'H',
	'һ':'h',
	'ЦҺ':'TS·H',
	'Цһ':'Ts·h',
	'цһ':'ts·h',
	'Ц':'Ts',
	'ц':'ts',
	'Ч':'Ch',
	'ч':'ch',
	'ШЧ':'SH·CH',
	'Шч':'Sh·ch',
	'шч':'sh·ch',
	'Ш':'Sh',
	'ш':'sh',
	'Щ':'Shch',
	'щ':'shch',
	'Ъ':'ʺ',
	'ъ':'ʺ',
	'Ы':'Y',
	'ы':'y',
	'І':'I',
	'і':'i',
	'Ь':'ʹ',
	'ь':'ʹ',
	'Э':'Ė',
	'э':'ė',
	'Ю':'Yu',
	'ю':'yu',
	'Я':'Ya',
	'я':'ya'
}

ukr_engDict = {
	'А':'A',
	'а':'a',
	'Б':'B',
	'б':'b',
	'В':'V',
	'в':'v',
	'Г':'H',
	'г':'h',
	'Ґ':'G',
	'ґ':'g',
	'Д':'D',
	'д':'d',
	'Е':'E',
	'е':'e',
	'Є':'Ye',
	'є':'ye',
	'Ж':'Zh',
	'ж':'zh',
	'ЗГ':'Z·H',
	'Зг':'Z·h',
	'зг':'z·h',
	'З':'Z',
	'з':'z',
	'И':'Y',
	'и':'y',
	'І':'I',
	'і':'i',
	'Ї':'Yi',
	'ї':'yi',
	'Й':'Y',
	'й':'y',
	'КГ':'K·H',
	'Кг':'K·h',
	'кг':'k·h',
	'К':'K',
	'к':'k',
	'Л':'L',
	'л':'l',
	'М':'M',
	'м':'m',
	'Н':'N',
	'н':'n',
	'О':'O',
	'о':'o',
	'П':'P',
	'п':'p',
	'Р':'R',
	'р':'r',
	'СГ':'S·H',
	'Сг':'S·h',
	'сг':'s·h',
	'С':'S',
	'с':'s',
	'ТС':'T·S',
	'Тс':'T·s',
	'тс':'t·s',
	'Т':'T',
	'т':'t',
	'У':'U',
	'у':'u',
	'Ф':'F',
	'ф':'f',
	'Х':'Kh',
	'х':'kh',
	'ЦГ':'TS·H',
	'Цг':'Ts·h',
	'цг':'ts·h',
	'Ц':'Ts',
	'ц':'ts',
	'Ч':'Ch',
	'ч':'ch',
	'ШЧ':'SH·CH',
	'Шч':'Sh·ch',
	'шч':'sh·ch',
	'Ш':'Sh',
	'ш':'sh',
	'Щ':'Shch',
	'щ':'shch',
	'Ю':'Yu',
	'ю':'yu',
	'Я':'Ya',
	'Я':'YA',
	'я':'ya',
	'Ь':'ʹ',
	'ь':'ʹ',
	'’':'ʺ'
}

#includes persian characters to avoid the need for a second nearly-identical dictionary
ara_engDict = {
	'أ':'a',
	'ا':'a',
	'٫':',',
	'٬':'.',
	'،':',',
	'؛':';',
	'؟':'?',
	'٪':'%',
	'۰':'0',
	'۱':'1',
	'۲':'2',
	'۳':'3',
	'۴':'4',
	'۵':'5',
	'۶':'6',
	'۷':'7',
	'۸':'8',
	'۹':'9',
	'٠':'0',
	'١':'1',
	'٢':'2',
	'٣':'3',
	'٤':'4',
	'٥':'5',
	'٦':'6',
	'٧':'7',
	'٨':'8',
	'٩':'9',
	'ته':'th',
	'كه':'kh',
	'ده':'dh',
	'سه':'sh',
	'بّ':'bb',
	'تّ':'tt',
	'ثّ':'thth',
	'جّ':'jj',
	'حّ':'ḥḥ',
	'خّ':'khkh',
	'دّ':'dd',
	'ذّ':'dhdh',
	'رّ':'rr',
	'زّ':'zz',
	'سّ':'ss',
	'شّ':'shsh',
	'صّ':'ṣṣ',
	'ضّ':'ḍḍ',
	'طّ':'ṭṭ',
	'ظّ':'ẓẓ',
	'عّ':'‘‘',
	'غّ':'ghgh',
	'فّ':'ff',
	'قّ':'qq',
	'كّ':'kk',
	'لّ':'ll',
	'مّ':'mm',
	'نّ':'nn',
	'هّ':'hh',
	'وّ':'ww',
	'ىّ':'yy',
	'ء':'’',
	'ٱ':'’',
	'آ':'ā',
	'آ':'’ā',
	'ب':'b',
	'ت':'t',
	'ة':'h',
	'ث':'th',
	'ج':'j',
	'ح':'ḩ',
	'خ':'kh',
	'د':'d',
	'ذ':'dh',
	'ر':'r',
	'ز':'z',
	'س':'s',
	'ش':'sh',
	'ص':'ş',
	'ض':'ḑ',
	'ط':'ţ',
	'ظ':'z̧',
	'ع':'‘',
	'غ':'gh',
	'ف':'f',
	'ق':'q',
	'ک':'k',
	'ك':'k',
	'ل':'l',
	'م':'m',
	'ن':'n',
	'ه':'h',
	'و':'w',
	'ى':'y',
	'َا':'ā',
	'َى':'á',
	'َيْ':'ay',
	'َوْ':'aw',
	'َ':'a',
	'ِي':'ī',
	'ِ':'i',
	'ُو':'ū',
	'ُ':'u',
	'ً':'aⁿ',
	'ٍ':'iⁿ',
	'ٌ':'uⁿ',
	#persian characters
	'ی':'y',
	'پ':'p',
	'چ':'ch',
	'گ':'g',
	'ژ':'j',
	'ي':'a'
}

ell_engDict = {
	'Ἀ':'A',
	'Ἁ':'A',
	'ᾼ':'A',
	'ᾈ':'A',
	'ᾉ':'A',
	'ἀ':'a',
	'ἁ':'a',
	'ᾳ':'a',
	'ᾀ':'a',
	'ᾁ':'a',
	'Ἂ':'A',
	'Ἃ':'A',
	'Ἄ':'A',
	'Ἅ':'A',
	'Ἆ':'A',
	'Ἇ':'A',
	'ᾊ':'A',
	'ᾋ':'A',
	'ᾌ':'A',
	'ᾍ':'A',
	'ᾎ':'A',
	'ᾏ':'A',
	'Ὰ':'A',
	'Ά':'A',
	'ἂ':'a',
	'ἃ':'a',
	'ἄ':'a',
	'ἅ':'a',
	'ἆ':'a',
	'ἇ':'a',
	'ὰ':'a',
	'ά':'a',
	'ᾂ':'a',
	'ᾃ':'a',
	'ᾄ':'a',
	'ᾅ':'a',
	'ᾆ':'a',
	'ᾇ':'a',
	'ᾲ':'a',
	'ᾴ':'a',
	'ᾶ':'a',
	'ᾷ':'a',
	'Ἐ':'É',
	'Ἑ':'É',
	'ἐ':'é',
	'ἑ':'é',
	'ὲ':'é',
	'έ':'é',
	'Ἒ':'E',
	'Ἓ':'E',
	'Ἔ':'E',
	'Ἕ':'E',
	'Ὲ':'E',
	'Έ':'E',
	'ἒ':'é',
	'ἓ':'é',
	'ἔ':'é',
	'ἕ':'é',
	'Ἠ':'I',
	'Ἡ':'I',
	'ᾘ':'I',
	'ᾙ':'I ',
	'ῌ':'I',
	'ἠ':'i',
	'ἡ':'i',
	'ᾐ':'i',
	'ᾑ':'i',
	'ῃ':'η',
	'Ἢ':'Í',
	'Ἣ':'Í',
	'Ἤ':'Í',
	'Ἥ':'Í',
	'Ἦ':'Í',
	'Ἧ':'Í',
	'ᾚ':'Í',
	'ᾛ':'Í',
	'ᾜ':'Í',
	'ᾝ':'Í',
	'ᾞ':'Í',
	'ᾟ':'Í',
	'Ὴ':'Í',
	'Ή':'Ή',
	'ἢ':'í',
	'ἣ':'í',
	'ἤ':'í',
	'ἥ':'í',
	'ἦ':'í',
	'ἧ':'í',
	'ὴ':'í',
	'ή':'í',
	'ᾒ':'í',
	'ᾓ':'í',
	'ᾔ':'í',
	'ᾕ':'í',
	'ᾖ':'í',
	'ᾗ':'í',
	'ῂ':'í',
	'ῄ':'í',
	'ῆ':'í',
	'ῇ':'ή',
	'Ἰ':'I',
	'Ἱ':'I',
	'ἰ':'i',
	'ἱ':'i',
	'Ἲ':'Í',
	'Ἳ':'Í',
	'Ἴ':'Í',
	'Ἵ':'Í',
	'Ἶ':'Í',
	'Ἷ':'Í',
	'Ὶ':'Í',
	'Ί':'Í',
	'ἲ':'í',
	'ἳ':'í',
	'ἴ':'í',
	'ἵ':'í',
	'ἶ':'í',
	'ἷ':'í',
	'ὶ':'í',
	'ί':'í',
	'ῖ':'í',
	'Ὀ':'O',
	'Ὁ':'O',
	'ὀ':'o',
	'ὁ':'o',
	'Ὂ':'Ó',
	'Ὃ':'Ó',
	'Ὄ':'Ó',
	'Ὅ':'Ó',
	'Ὸ':'Ó',
	'Ό':'Ó',
	'ὂ':'ó',
	'ὃ':'ó',
	'ὄ':'ó',
	'ὅ':'ó',
	'ὸ':'ó',
	'ό':'ó',
	'ὐ':'v',
	'ὑ':'v',
	'Ὓ':'Í',
	'Ὕ':'Í',
	'Ὗ':'Í',
	'Ὺ':'Í',
	'Ύ':'Í',
	'ὒ':'í',
	'ὓ':'í',
	'ὔ':'í',
	'ὕ':'í',
	'ὖ':'í',
	'ὗ':'í',
	'ὺ':'í',
	'ύ':'í',
	'ῦ':'í',
	'Ὠ':'O',
	'Ὡ':'O',
	'ᾨ':'O',
	'ᾩ':'O',
	'ῼ':'O',
	'ὠ':'o',
	'ὡ':'o',
	'ᾠ':'o',
	'ᾡ':'o',
	'ῳ':'o',
	'Ὤ':'Ó',
	'Ὣ':'Ó',
	'Ὤ':'Ó',
	'Ὥ':'Ó',
	'Ὦ':'Ó',
	'Ὧ':'Ó',
	'ᾪ':'Ó',
	'ᾫ':'Ó',
	'ᾬ':'Ó',
	'ᾭ':'Ó',
	'ᾮ':'Ó',
	'ᾯ':'Ó',
	'Ὼ':'Ó',
	'Ώ':'Ó',
	'ὢ':'ó',
	'ὣ':'ó',
	'ὤ':'ó',
	'ὥ':'ó',
	'ὦ':'ó',
	'ὧ':'ó',
	'ὼ':'ó',
	'ώ':'ó',
	'ᾢ':'ó',
	'ᾣ':'ó',
	'ᾤ':'ó',
	'ᾥ':'ó',
	'ᾦ':'ó',
	'ᾧ':'ó',
	'ῲ':'ó',
	'ῴ':'ó',
	'ῶ':'ó',
	'ῷ':'ó',
	'Ῥ':'R',
	'ῤ':'r',
	'ῥ':'r',
	'Ϊ':'Ï',
	'Ϋ':'Ï',
	'ϊ':'ï',
	'ϋ':'ï',
	'ΐ':'ḯ',
	'ΰ':'ḯ',
	'Αε':'Aë',
	'αε':'aë',
	'Αη':'Aï',
	'αη':'aï',
	'Οη':'Oï',
	'οη':'oï',
	'Ωο':'Oö',
	'ωο':'oö',
	'Άε':'Áë',
	'άε':'áë',
	'Άη':'Áï',
	'άη':'áï',
	'Όη':'Óï',
	'όη':'óï',
	'Ώο':'Óö',
	'ώο':'óö',
	'ΑΙ':'AI',
	'Αι':'Ai',
	'αι':'ai',
	'ΑΥ':'AV',
	'Αυ':'Av',
	'αυ':'av',
	'Α':'A',
	'α':'a',
	'Ά':'Á',
	'ά':'á',
	'Β':'V',
	'β':'v',
	'ΓΓ':'NG',
	'Γγ':'Ng',
	'γγ':'ng',
	'ΓΚ':'G',
	'Γκ':'G',
	'γκ':'g',
	'ΓΚ':'NG',
	'Γκ':'Ng',
	'γκ':'ng',
	'Γ':'G',
	'Γ':'G',
	'Γ':'G',
	'Γ':'G',
	'γ':'g',
	'γ':'g',
	'Γ':'Y',
	'Γ':'Y',
	'Γ':'Y',
	'Γ':'Y',
	'γ':'y',
	'γ':'y',
	'Γ':'N',
	'Γ':'N',
	'γ':'n',
	'Γ':'G',
	'γ':'g',
	'ΝΔ':'D',
	'νδ':'d',
	'Δ':'Dh',
	'Δ':'DH',
	'δ':'dh',
	'ΕΙ':'I',
	'Ει':'I',
	'ει':'i',
	'ΕΪ':'EÏ',
	'Εϊ':'Eï',
	'εϊ':'eï',
	'ΕΥ':'EV',
	'Ευ':'Ev',
	'ευ':'ev',
	'Ε':'E',
	'ε':'e',
	'Έ':'É',
	'έ':'é',
	'Ζ':'Z',
	'ζ':'z',
	'ΗΥ':'IV',
	'Ηυ':'Iv',
	'ηυ':'iv',
	'Η':'I',
	'η':'i',
	'Ή':'Í',
	'ή':'í',
	'Θ':'Th',
	'Θ':'TH',
	'θ':'th',
	'Ι':'I',
	'ι':'i',
	'Ί':'Í',
	'ί':'í',
	'Κ':'K',
	'κ':'k',
	'Λ':'L',
	'λ':'l',
	'ΜΠ':'B',
	'Μπ':'B',
	'μπ':'b',
	'ΜΠ':'MB',
	'Μπ':'Mb',
	'μπ':'mb',
	'Μ':'M',
	'μ':'m',
	'ΝΤ':'D',
	'Ντ':'D',
	'ντ':'d',
	'ΝΤ':'ND',
	'Ντ':'Nd',
	'ντ':'nd',
	'Ν':'N',
	'ν':'n',
	'Ξ':'X',
	'ξ':'x',
	'ΟΙ':'OI',
	'Οι':'Oi',
	'οι':'oi',
	'ΟΥ':'OU',
	'Ου':'Ou',
	'ου':'ou',
	'Ο':'O',
	'ο':'o',
	'Ό':'Ó',
	'ό':'ó',
	'Π':'P',
	'π':'p',
	'Ρ':'R',
	'ρ':'r',
	'Σ':'S',
	'σ':'s',
	'ς':'s',
	'Τ':'T',
	'τ':'t',
	'Υ':'I',
	'υ':'i',
	'Ύ':'Í',
	'ύ':'í',
	'Φ':'F',
	'φ':'f',
	'Χ':'Kh',
	'Χ':'KH',
	'χ':'kh',
	'Ψ':'Ps',
	'Ψ':'PS',
	'ψ':'ps',
	'Ω':'O',
	'ω':'o',
	'Ώ':'Ó',
	'ώ':'ó'
}

heb_engDict = {
	'בּ':'b',
	'פּ':'P',
	'גּ':'g',
	'ג׳':'ǧ',
	'וּ':'u',
	'וֹ':'o',
	'צ׳':'č',
	'ז׳':'ž',
	'דּ':'d',
	'הּ':'h',
	'ךּ':'k',
	'כּ':'k',
	'ךְ':'kh',
	'תּ':'t',
	'א':'’',
	'ב':'v',
	'ג':'g',
	'ד':'d',
	'ה':'h',
	'ח':'ẖ',
	'ו':'w',
	'ז':'z',
	'ט':'t',
	'ת':'t',
	'י':'y',
	'כ':'kh',
	'ך':'kh',
	'ל':'l',
	'מ':'m',
	'ם':'m',
	'נ':'n',
	'ן':'n',
	'ס':'s',
	'ע':'‘',
	'פ':'f',
	'ף':'f',
	'צ':'ẕ',
	'ץ':'ẕ',
	'ק':'q',
	'ר':'r',
	'שׁ':'sh',
	'שׂ':'s',
	'ַ':'a',
	'ֲ':'a',
	'ָ':'o',
	'ֶ':'e',
	'ֱ':'e',
	'ֵי':'e',
	'ֵ':'e',
	'ְ':'e',
	'ִי':'i',
	'ִ':'i',
	'ֳ':'o',
	'ֻ':'u'
}

hye_engDict = {
	'Ա':'A',
	'ա':'a',
	'Բ':'B',
	'բ':'b',
	'Գ':'G',
	'գ':'g',
	'Դ':'D',
	'դ':'d',
	'Ե':'YE',
	'Ե':'Ye',
	'Ե':'Ye',
	'Ե':'E',
	'ե':'ye',
	'ե':'e',
	'Զ':'Z',
	'զ':'z',
	'Է':'E',
	'է':'e',
	'Ը':'Y',
	'ը':'y',
	'Թ':'T',
	'թ':'t',
	'Ժ':'Zh',
	'Ժ':'ZH',
	'ժ':'zh',
	'Ի':'I',
	'ի':'i',
	'Լ':'L',
	'լ':'l',
	'Խ':'Kh',
	'Խ':'KH',
	'խ':'kh',
	'Ծ':'Ts',
	'Ծ':'TS',
	'ծ':'ts',
	'Կ':'K',
	'կ':'k',
	'Հ':'H',
	'հ':'h',
	'Ձ':'Dz',
	'Ձ':'DZ',
	'ձ':'dz',
	'Ղ':'Gh',
	'Ղ':'GH',
	'ղ':'gh',
	'Ճ':'Ch',
	'Ճ':'CH',
	'ճ':'ch',
	'Մ':'M',
	'մ':'m',
	'Յ':'Y',
	'յ':'y',
	'Ն':'N',
	'ն':'n',
	'Շ':'Sh',
	'Շ':'SH',
	'շ':'sh',
	'Ու':'U',
	'ՈՒ':'U',
	'ու':'u',
	'ՈՎ':'OV',
	'Ով':'Ov',
	'ով':'ov',
	'Ո':'Vo',
	'Ո':'O',
	'ո':'vo',
	'ո':'o',
	'Չ':'Ch',
	'չ':'ch',
	'Պ':'P',
	'պ':'p',
	'Ջ':'J',
	'ջ':'j',
	'Ռ':'Rr',
	'ռ':'rr',
	'Ս':'S',
	'ս':'s',
	'Վ':'V',
	'վ':'v',
	'Տ':'T',
	'տ':'t',
	'Ր':'R',
	'ր':'r',
	'Ց':'Ts',
	'ց':'ts',
	'Փ':'P',
	'փ':'p',
	'Ք':'K',
	'ք':'k',
	'Օ':'O',
	'օ':'o',
	'Ֆ':'F',
	'ֆ':'f'
}

kat_engDict = {
	'წ':'tsʼ',
	'კ':'kʼ',
	'პ':'pʼ',
	'ჟ':'zh',
	'ტ':'tʼ',
	'ღ':'gh',
	'ყ':'qʼ',
	'შ':'sh',
	'ჭ':'chʼ',
	'ჩ':'ch',
	'ც':'ts',
	'ძ':'dz',
	'ხ':'kh',
	'ჳ':'ŭi',
	'ა':'a',
	'ბ':'b',
	'გ':'g',
	'დ':'d',
	'ე':'e',
	'ვ':'v',
	'ზ':'z',
	'თ':'t',
	'ი':'i',
	'ლ':'l',
	'მ':'m',
	'ნ':'n',
	'ო':'o',
	'რ':'r',
	'ს':'s',
	'უ':'u',
	'ფ':'p',
	'ქ':'k',
	'ჯ':'j',
	'ჰ':'h',
	'ჴ':'q'
}