# -*- coding: UTF-8 -*-

"""
   This file contains a list of language and country names.

   >>> languages == getLanguages()
   True
   
   >>> len(languages) == len(getNativeLanguageNames())
   True

   >>> combined == getCombined()
   True

   >>> len(combined) == len(getCombinedLanguageNames())
   True

   >>> len(countries) == len(getCountries())
   True
"""

def getLanguages():
    """ Get all languages"""
    return languages.copy()

def getNativeLanguageNames():
    """ Get all native language names"""
    native_languages = {}
    for lc in languages:
        native_languages[lc] = languages.get(lc).get('native')
    return native_languages

def getCombined():
    """ Get all combined languages"""
    return combined.copy()

def getCombinedLanguageNames():
    """ Get all combined language names"""
    combined_languages = {}
    for lc in combined:
        combined_languages[lc] = combined.get(lc).get('english')
    return combined_languages

def getCountries():
    """ Get all countries"""
    return countries

# This is a dictionary of dictonaries:
#
# 'langcode-variation' : {native : 'Native name', english : 'English name', flag : 'flag-*.gif'}

languages = {
'aa' : {'native' : 'магIарул мацI', 'english' : 'Afar', 'flag' : 'flag-dj.gif'},
'ab' : {'native' : 'бызшәа', 'english' : 'Abkhazian', 'flag' : 'flag-ge.gif'},
'af' : {'native' : 'Afrikaans', 'english' : 'Afrikaans'},
'am' : {'native' : 'አማርኛ', 'english' : 'Amharic'},
'ar' : {'native' : 'العربية', 'english' : 'Arabic'},
'as' : {'native' : 'অসমিয়া', 'english' : 'Assamese'},
'ay' : {'native' : 'Aymara', 'english' : 'Aymara'},
'az' : {'native' : 'Azəri Türkçəsi', 'english' : 'Azerbaijani', 'flag' : 'flag-az.gif'},
'ba' : {'native' : 'Bashkir', 'english' : 'Bashkir'},
'be' : {'native' : 'Беларускі', 'english' : 'Belarussian', 'flag' : 'flag-by.gif'},
'bg' : {'native' : 'Български', 'english' : 'Bulgarian', 'flag' : 'flag-bg.gif'},
'bh' : {'native' : 'Bihari', 'english' : 'Bihari'},
'bi' : {'native' : 'Bislama', 'english' : 'Bislama'},
'bn' : {'native' : 'বাংলা', 'english' : 'Bengali'},
'bo' : {'native' : 'བོད་སྐད་', 'english' : 'Tibetan'},
'bs' : {'native' : 'Bosanski', 'english' : 'Bosnian', 'flag' : 'flag-ba.gif'},
'br' : {'native' : 'Brezhoneg', 'english' : 'Breton'},
'ca' : {'native' : 'Català', 'english' : 'Catalan'},
'co' : {'native' : 'Corsu', 'english' : 'Corsican'},
'cs' : {'native' : 'Čeština', 'english' : 'Czech', 'flag' : 'flag-cz.gif'},
'cy' : {'native' : 'Cymraeg', 'english' : 'Welsh', 'flag' : 'flag-cy.gif'},
'da' : {'native' : 'Dansk', 'english' : 'Danish', 'flag' : 'flag-dk.gif'},
'de' : {'native' : 'Deutsch', 'english' : 'German', 'flag' : 'flag-de.gif'},
'dz' : {'native' : 'Bhutani', 'english' : 'Indian Bhutani'},
'el' : {'native' : 'Ελληνικά', 'english' : 'Greek', 'flag' : 'flag-gr.gif'},
'en' : {'native' : 'English', 'english' : 'English', 'flag' : 'flag-gb.gif'},
'eo' : {'native' : 'Esperanto', 'english' : 'Esperanto', 'flag' : 'flag-eo.gif'},
'es' : {'native' : 'Español', 'english' : 'Spanish', 'flag' : 'flag-es.gif'},
'et' : {'native' : 'Eesti', 'english' : 'Estonian', 'flag' : 'flag-ee.gif'},
'eu' : {'native' : 'Euskara', 'english' : 'Basque', 'flag' : 'flag-eu.gif'},
'fa' : {'native' : 'فارسی', 'english' : 'Persian'},
'fi' : {'native' : 'Suomi', 'english' : 'Finnish', 'flag' : 'flag-fi.gif'},
'fj' : {'native' : 'Fiji', 'english' : 'Fiji', 'flag' : 'flag-fj.gif'},
'fo' : {'native' : 'Føroyska', 'english' : 'Faroese'},
'fr' : {'native' : 'Français', 'english' : 'French', 'flag' : 'flag-fr.gif'},
'fy' : {'native' : 'Frysk', 'english' : 'Frisian'},
'ga' : {'native' : 'Gaeilge', 'english' : 'Irish Gaelic'},
'gd' : {'native' : 'Gàidhlig', 'english' : 'Scottish Gaelic'},
'gl' : {'native' : 'Galego', 'english' : 'Galician'},
'gn' : {'native' : 'Guarani', 'english' : 'Guarani'},
'gu' : {'native' : 'ગુજરાતી', 'english' : 'Gujarati'},
'gv' : {'native' : 'Gaelg', 'english' : 'Manx Gaelic'},
'ha' : {'native' : 'هَوُس', 'english' : 'Hausa'},
'he' : {'native' : 'עברית', 'english' : 'Hebrew', 'flag' : 'flag-il.gif'},
'hi' : {'native' : 'हिंदी', 'english' : 'Hindi', 'flag' : 'flag-in.gif'},
'hr' : {'native' : 'Hrvatski', 'english' : 'Croatian', 'flag' : 'flag-hr.gif'},
'hu' : {'native' : 'Magyar', 'english' : 'Hungarian', 'flag' : 'flag-hu.gif'},
'hy' : {'native' : 'Հայերէն', 'english' : 'Armenian', 'flag' : 'flag-am.gif'},
'ia' : {'native' : 'Interlingua', 'english' : 'Interlingua'},
'id' : {'native' : 'Bahasa Indonesia', 'english' : 'Indonesian', 'flag' : 'flag-id.gif'},
'ie' : {'native' : 'Interlingue', 'english' : 'Interlingue'},
'ik' : {'native' : 'Inupiak', 'english' : 'Inupiak'},
'is' : {'native' : 'Íslenska', 'english' : 'Icelandic', 'flag' : 'flag-is.gif'},
'it' : {'native' : 'Italiano', 'english' : 'Italian', 'flag' : 'flag-it.gif'},
'iu' : {'native' : 'ᐃᓄᒃᑎᑐᑦ', 'english' : 'Inuktitut'},
'ja' : {'native' : '日本語', 'english' : 'Japanese', 'flag' : 'flag-jp.gif'},
'jw' : {'native' : 'Javanese', 'english' : 'Javanese'},
'ka' : {'native' : 'ქართული', 'english' : 'Georgian', 'flag' : 'flag-ge.gif'},
'kk' : {'native' : 'ﻗﺎﺯﺍﻗﺸﺎ', 'english' : 'Kazakh', 'flag' : 'flag-kz.gif'},
'kl' : {'native' : 'Greenlandic', 'english' : 'Greenlandic', 'flag' : 'flag-gl.gif'},
'km' : {'native' : 'ខ្មែរ', 'english' : 'Cambodian/Khmer', 'flag' : 'flag-kh.gif'},
'kn' : {'native' : 'ಕನ್ನಡ', 'english' : 'Kannada', 'flag' : 'flag-in.gif'},
'ko' : {'native' : '한국어', 'english' : 'Korean', 'flag' : 'flag-kr.gif'},
'ks' : {'native' : 'काऽशुर', 'english' : 'Kashmiri', 'flag' : 'flag-in.gif'},
'ku' : {'native' : 'Kurdí', 'english' : 'Kurdish'},
'kw' : {'native' : 'Kernewek', 'english' : 'Cornish'},
'ky' : {'native' : 'Кыргыз', 'english' : 'Kirghiz'},
'la' : {'native' : 'Latin', 'english' : 'Latin', 'flag' : 'flag-va.gif'},
'lb' : {'native' : 'Lëtzebuergesch', 'english' : 'Luxemburgish', 'flag' : 'flag-lu.gif'},
'li' : {'native' : 'Limburgs', 'english' : 'Limburgish'},
'ln' : {'native' : 'Lingala', 'english' : 'Lingala'},
'lo' : {'native' : 'ພາສາລາວ', 'english' : 'Laotian', 'flag' : 'flag-la.gif'},
'lt' : {'native' : 'Lietuviskai', 'english' : 'Lithuanian', 'flag' : 'flag-lt.gif'},
'lv' : {'native' : 'Latviešu', 'english' : 'Latvian'},
'mg' : {'native' : 'Malagasy', 'english' : 'Madagascarian', 'flag' : 'flag-mg.gif'},
'mi' : {'native' : 'Maori', 'english' : 'Maori'},
'mk' : {'native' : 'Македонски', 'english' : 'Macedonian', 'flag' : 'flag-mk.gif'},
'ml' : {'native' : 'മലയാളം', 'english' : 'Malayalam'},
'mn' : {'native' : 'Монгол', 'english' : 'Mongolian', 'flag' : 'flag-mn.gif'},
'mo' : {'native' : 'Moldavian', 'english' : 'Moldavian', 'flag' : 'flag-md.gif'},
'mr' : {'native' : 'मराठी', 'english' : 'Marathi'},
'ms' : {'native' : 'Bahasa Melayu', 'english' : 'Malay'},
'mt' : {'native' : 'Malti', 'english' : 'Maltese', 'flag' : 'flag-mt.gif'},
'my' : {'native' : 'Burmese', 'english' : 'Burmese'},
'na' : {'native' : 'Nauru', 'english' : 'Nauruan', 'flag' : 'flag-nr.gif'},
'ne' : {'native' : 'नेपाली', 'english' : 'Nepali'},
'nl' : {'native' : 'Nederlands', 'english' : 'Dutch', 'flag' : 'flag-nl.gif'},
'no' : {'native' : 'Norsk', 'english' : 'Norwegian', 'flag' : 'flag-no.gif'},
'nn' : {'native' : 'Nynorsk', 'english' : 'Norwegian Nynorsk'},
'oc' : {'native' : 'Occitan', 'english' : 'Occitan'},
'om' : {'native' : 'Oromo', 'english' : 'Oromo'},
'or' : {'native' : 'ଓଡ଼ିଆ', 'english' : 'Oriya'},
'pa' : {'native' : 'ਪੰਜਾਬੀ', 'english' : 'Punjabi'},
'pl' : {'native' : 'Polski', 'english' : 'Polish', 'flag' : 'flag-pl.gif'},
'ps' : {'native' : 'پښتو', 'english' : 'Pashto'},
'pt' : {'native' : 'Português', 'english' : 'Portuguese', 'flag' : 'flag-pt.gif'},
'qu' : {'native' : 'Quechua', 'english' : 'Quechua'},
'rm' : {'native' : 'Rhaeto-Romance', 'english' : ''},
'rn' : {'native' : 'Kirundi', 'english' : 'Kirundi'},
'ro' : {'native' : 'Română', 'english' : 'Romanian', 'flag' : 'flag-ro.gif'},
'ru' : {'native' : 'Русский', 'english' : 'Russian', 'flag' : 'flag-ru.gif'},
'rw' : {'native' : 'Kiyarwanda', 'english' : 'Kiyarwanda'},
'sa' : {'native' : 'संस्कृत', 'english' : 'Sanskrit'},
'sd' : {'native' : 'Sindhi', 'english' : 'Sindhi', 'flag' : 'flag-pk.gif'},
'se' : {'native' : 'Northern Sámi', 'english' : 'Northern Sámi'},
'sg' : {'native' : 'Sangho', 'english' : 'Sangho', 'flag' : 'flag-cf.gif'},
'sh' : {'native' : 'Serbo-Croatian', 'english' : 'Serbo-Croatian'},
'si' : {'native' : 'Singhalese', 'english' : 'Singhalese'},
'sk' : {'native' : 'Slovenčina', 'english' : 'Slovak', 'flag' : 'flag-sk.gif'},
'sl' : {'native' : 'Slovenščina', 'english' : 'Slovenian', 'flag' : 'flag-si.gif'},
'sm' : {'native' : 'Samoan', 'english' : 'Samoan'},
'sn' : {'native' : 'Shona', 'english' : 'Shona'},
'so' : {'native' : 'Somali', 'english' : 'Somali', 'flag' : 'flag-so.gif'},
'sq' : {'native' : 'Shqip', 'english' : 'Albanian', 'flag' : 'flag-al.gif'},
'sr' : {'native' : 'српски', 'english' : 'Serbian', 'flag' : 'flag-cs.gif'},
'ss' : {'native' : 'Siswati', 'english' : 'Siswati'},
'st' : {'native' : 'Sesotho', 'english' : 'Sesotho'},
'su' : {'native' : 'Sudanese', 'english' : 'Sudanese', 'flag' : 'flag-sd.gif'},
'sv' : {'native' : 'Svenska', 'english' : 'Swedish', 'flag' : 'flag-se.gif'},
'sw' : {'native' : 'Swahili', 'english' : 'Swahili'},
'ta' : {'native' : 'தமிழ', 'english' : 'Tamil'},
'te' : {'native' : 'తెలుగు', 'english' : 'Telugu'},
'tg' : {'native' : 'Тоҷики', 'english' : 'Tadjik', 'flag' : 'flag-tj.gif'},
'th' : {'native' : 'ไทย', 'english' : 'Thai', 'flag' : 'flag-th.gif'},
'ti' : {'native' : 'ትግርኛ', 'english' : 'Tigrinya'},
'tk' : {'native' : 'түркmенче', 'english' : 'Turkmen', 'flag' : 'flag-tm.gif'},
'tl' : {'native' : 'Tagalog', 'english' : 'Tagalog'},
'tn' : {'native' : 'Setswana', 'english' : 'Setswana', 'flag' : 'flag-bw.gif'},
'to' : {'native' : 'Tonga', 'english' : 'Tonga'},
'tr' : {'native' : 'Türkçe', 'english' : 'Turkish', 'flag' : 'flag-tr.gif'},
'ts' : {'native' : 'Tsonga', 'english' : 'Tsonga'},
'tt' : {'native' : 'татарча', 'english' : 'Tatar'},
'tw' : {'native' : 'Twi', 'english' : 'Twi'},
'ug' : {'native' : 'Uigur', 'english' : 'Uigur'},
'uk' : {'native' : 'Українська', 'english' : 'Ukrainian', 'flag' : 'flag-ua.gif'},
'ur' : {'native' : 'اردو', 'english' : 'Urdu'},
'uz' : {'native' : 'Ўзбекча', 'english' : 'Uzbek', 'flag' : 'flag-uz.gif'},
'vi' : {'native' : 'Tiếng Việt', 'english' : 'Vietnamese', 'flag' : 'flag-vn.gif'},
'vo' : {'native' : 'Volapük', 'english' : 'Volapük'},
'wa' : {'native' : 'Walon', 'english' : 'Walloon'},
'wo' : {'native' : 'Wolof', 'english' : 'Wolof'},
'xh' : {'native' : 'isiXhosa', 'english' : 'Xhosa'},
'yi' : {'native' : 'ײִדיש', 'english' : 'Yiddish', 'flag' : 'flag-il.gif'},
'yo' : {'native' : 'Yorùbá', 'english' : 'Yorouba'},
'za' : {'native' : 'Zhuang', 'english' : 'Zhuang'},
'zh' : {'native' : '简体中文', 'english' : 'Chinese', 'flag' : 'flag-cn.gif'},
'zu' : {'native' : 'isiZulu', 'english' : 'Zulu'}
}

combined = {
'ar-ae' : {'english' : 'Arabic (United Arab Emirates)'},
'ar-bh' : {'english' : 'Arabic (Bahrain)'},
'ar-dz' : {'english' : 'Arabic (Algeria)'},
'ar-eg' : {'english' : 'Arabic (Egypt)'},
'ar-il' : {'english' : 'Arabic (Israel)'},
'ar-iq' : {'english' : 'Arabic (Iraq)'},
'ar-jo' : {'english' : 'Arabic (Jordan)'},
'ar-kw' : {'english' : 'Arabic (Kuwait)'},
'ar-lb' : {'english' : 'Arabic (Lebanon)'},
'ar-ly' : {'english' : 'Arabic (Libya)'},
'ar-ma' : {'english' : 'Arabic (Morocco)'},
'ar-mr' : {'english' : 'Arabic (Mauritania)'},
'ar-om' : {'english' : 'Arabic (Oman)'},
'ar-ps' : {'english' : 'Arabic (Palestinian West Bank and Gaza)'},
'ar-qa' : {'english' : 'Arabic (Qatar)'},
'ar-sa' : {'english' : 'Arabic (Saudi Arabia)'},
'ar-sd' : {'english' : 'Arabic (Sudan)'},
'ar-so' : {'english' : 'Arabic (Somalia)'},
'ar-sy' : {'english' : 'Arabic (Syria)'},
'ar-td' : {'english' : 'Arabic (Chad)'},
'ar-tn' : {'english' : 'Arabic (Tunisia)'},
'ar-ye' : {'english' : 'Arabic (Yemen)'},
'bn-bd' : {'english' : 'Bengali (Bangladesh)'},
'bn-in' : {'english' : 'Bengali (India)'},
'bn-sg' : {'english' : 'Bengali (Singapore)'},
'ch-gu' : {'english' : 'Chamorro (Guam)'},
'ch-mp' : {'english' : 'Chamorro (Northern Mariana Islands)'},
'da-dk' : {'english' : 'Danish (Denmark)'},
'da-gl' : {'english' : 'Danish (Greenland)'},
'de-at' : {'english' : 'German (Austria)', 'native' : 'Deutsch (Österreich)',  'flag' : 'flag-at.gif'},
'de-be' : {'english' : 'German (Belgium)'},
'de-ch' : {'english' : 'German (Switzerland)', 'flag' : 'flag-ch.gif'},
'de-de' : {'english' : 'German (Germany)', 'flag' : 'flag-de.gif'},
'de-dk' : {'english' : 'German (Denmark)'},
'de-li' : {'english' : 'German (Liechtenstein)'},
'de-lu' : {'english' : 'German (Luxembourg)'},
'el-cy' : {'english' : 'Greek (Cyprus)'},
'el-gr' : {'english' : 'Greek (Greece)'},
'en-ag' : {'english' : 'English (Antigua and Barbuda)'},
'en-ai' : {'english' : 'English (Anguilla)'},
'en-as' : {'english' : 'English (American Samoa)'},
'en-au' : {'english' : 'English (Australia)'},
'en-bb' : {'english' : 'English (Barbados)'},
'en-bm' : {'english' : 'English (Bermuda)'},
'en-bn' : {'english' : 'English (Brunei)'},
'en-bs' : {'english' : 'English (Bahamas)'},
'en-bw' : {'english' : 'English (Botswana)'},
'en-bz' : {'english' : 'English (Belize)'},
'en-ca' : {'english' : 'English (Canada)'},
'en-ck' : {'english' : 'English (Cook Islands)'},
'en-cm' : {'english' : 'English (Cameroon)'},
'en-dm' : {'english' : 'English (Dominica)'},
'en-er' : {'english' : 'English (Eritrea)'},
'en-et' : {'english' : 'English (Ethiopia)'},
'en-fj' : {'english' : 'English (Fiji)'},
'en-fk' : {'english' : 'English (Falkland Islands)'},
'en-fm' : {'english' : 'English (Micronesia)'},
'en-gb' : {'english' : 'English (United Kingdom)'},
'en-gd' : {'english' : 'English (Grenada)'},
'en-gh' : {'english' : 'English (Ghana)'},
'en-gi' : {'english' : 'English (Gibraltar)'},
'en-gm' : {'english' : 'English (Gambia)'},
'en-gu' : {'english' : 'English (Guam)'},
'en-gy' : {'english' : 'English (Guyana)'},
'en-ie' : {'english' : 'English (Ireland)'},
'en-il' : {'english' : 'English (Israel)'},
'en-io' : {'english' : 'English (British Indian Ocean Territory)'},
'en-jm' : {'english' : 'English (Jamaica)'},
'en-ke' : {'english' : 'English (Kenya)'},
'en-ki' : {'english' : 'English (Kiribati)'},
'en-kn' : {'english' : 'English (St. Kitts-Nevis)'},
'en-ky' : {'english' : 'English (Cayman Islands)'},
'en-lc' : {'english' : 'English (St. Lucia)'},
'en-lr' : {'english' : 'English (Liberia)'},
'en-ls' : {'english' : 'English (Lesotho)'},
'en-mp' : {'english' : 'English (Northern Mariana Islands)'},
'en-ms' : {'english' : 'English (Montserrat)'},
'en-mt' : {'english' : 'English (Malta)'},
'en-mu' : {'english' : 'English (Mauritius)'},
'en-mw' : {'english' : 'English (Malawi)'},
'en-na' : {'english' : 'English (Namibia)'},
'en-nf' : {'english' : 'English (Norfolk Island)'},
'en-ng' : {'english' : 'English (Nigeria)'},
'en-nr' : {'english' : 'English (Nauru)'},
'en-nu' : {'english' : 'English (Niue)'},
'en-nz' : {'english' : 'English (New Zealand)'},
'en-pg' : {'english' : 'English (Papua New Guinea)'},
'en-ph' : {'english' : 'English (Philippines)'},
'en-pk' : {'english' : 'English (Pakistan)'},
'en-pn' : {'english' : 'English (Pitcairn)'},
'en-pr' : {'english' : 'English (Puerto Rico)'},
'en-pw' : {'english' : 'English (Palau)'},
'en-rw' : {'english' : 'English (Rwanda)'},
'en-sb' : {'english' : 'English (Solomon Islands)'},
'en-sc' : {'english' : 'English (Seychelles)'},
'en-sg' : {'english' : 'English (Singapore)'},
'en-sh' : {'english' : 'English (St. Helena)'},
'en-sl' : {'english' : 'English (Sierra Leone)'},
'en-so' : {'english' : 'English (Somalia)'},
'en-sz' : {'english' : 'English (Swaziland)'},
'en-tc' : {'english' : 'English (Turks and Caicos Islands)'},
'en-tk' : {'english' : 'English (Tokelau)'},
'en-to' : {'english' : 'English (Tonga)'},
'en-tt' : {'english' : 'English (Trinidad and Tobago)'},
'en-ug' : {'english' : 'English (Uganda)'},
'en-us' : {'english' : 'English (USA)'},
'en-vc' : {'english' : 'English (St. Vincent and the Grenadi)'},
'en-vg' : {'english' : 'English (British Virgin Islands)'},
'en-vi' : {'english' : 'English (U.S. Virgin Islands)'},
'en-vu' : {'english' : 'English (Vanuatu)'},
'en-ws' : {'english' : 'English (Western Samoa)'},
'en-za' : {'english' : 'English (South Africa)'},
'en-zm' : {'english' : 'English (Zambia)'},
'en-zw' : {'english' : 'English (Zimbabwe)'},
'es-ar' : {'english' : 'Spanish (Argentina)'},
'es-bo' : {'english' : 'Spanish (Bolivia)'},
'es-cl' : {'english' : 'Spanish (Chile)'},
'es-co' : {'english' : 'Spanish (Colombia)'},
'es-cr' : {'english' : 'Spanish (Costa Rica)'},
'es-cu' : {'english' : 'Spanish (Cuba)'},
'es-do' : {'english' : 'Spanish (Dominican Republic)'},
'es-ec' : {'english' : 'Spanish (Ecuador)'},
'es-es' : {'english' : 'Spanish (Spain)'},
'es-gq' : {'english' : 'Spanish (Equatorial Guinea)'},
'es-gt' : {'english' : 'Spanish (Guatemala)'},
'es-hn' : {'english' : 'Spanish (Honduras)'},
'es-mx' : {'english' : 'Spanish (Mexico)'},
'es-ni' : {'english' : 'Spanish (Nicaragua)'},
'es-pa' : {'english' : 'Spanish (Panama)'},
'es-pe' : {'english' : 'Spanish (Peru)'},
'es-pr' : {'english' : 'Spanish (Puerto Rico)'},
'es-py' : {'english' : 'Spanish (Paraguay)'},
'es-sv' : {'english' : 'Spanish (El Salvador)'},
'es-us' : {'english' : 'Spanish (USA)'},
'es-uy' : {'english' : 'Spanish (Uruguay)'},
'es-ve' : {'english' : 'Spanish (Venezuela)'},
'fr-ad' : {'english' : 'French (Andorra)'},
'fr-be' : {'english' : 'French (Belgium)'},
'fr-bf' : {'english' : 'French (Burkina Faso)'},
'fr-bi' : {'english' : 'French (Burundi)'},
'fr-bj' : {'english' : 'French (Benin)'},
'fr-ca' : {'english' : 'French (Canada)'},
'fr-cd' : {'english' : 'French (Democratic Republic of Congo)'},
'fr-cf' : {'english' : 'French (Central African Republic)'},
'fr-cg' : {'english' : 'French (Congo)'},
'fr-ch' : {'english' : 'French (Switzerland)'},
'fr-ci' : {'english' : 'French (Cote d\'Ivoire)'},
'fr-cm' : {'english' : 'French (Cameroon)'},
'fr-dj' : {'english' : 'French (Djibouti)'},
'fr-fr' : {'english' : 'French (France)'},
'fr-ga' : {'english' : 'French (Gabon)'},
'fr-gb' : {'english' : 'French (United Kingdom)'},
'fr-gf' : {'english' : 'French (French Guiana)'},
'fr-gn' : {'english' : 'French (Guinea)'},
'fr-gp' : {'english' : 'French (Guadeloupe)'},
'fr-ht' : {'english' : 'French (Haiti)'},
'fr-it' : {'english' : 'French (Italy)'},
'fr-km' : {'english' : 'French (Comoros Islands)'},
'fr-lb' : {'english' : 'French (Lebanon)'},
'fr-lu' : {'english' : 'French (Luxembourg)'},
'fr-mc' : {'english' : 'French (Monaco)'},
'fr-mg' : {'english' : 'French (Madagascar)'},
'fr-ml' : {'english' : 'French (Mali)'},
'fr-mq' : {'english' : 'French (Martinique)'},
'fr-nc' : {'english' : 'French (New Caledonia)'},
'fr-pf' : {'english' : 'French (French Polynesia)'},
'fr-pm' : {'english' : 'French (St. Pierre and Miquelon)'},
'fr-re' : {'english' : 'French (Reunion)'},
'fr-rw' : {'english' : 'French (Rwanda)'},
'fr-sc' : {'english' : 'French (Seychelles)'},
'fr-td' : {'english' : 'French (Chad)'},
'fr-tg' : {'english' : 'French (Togo)'},
'fr-vu' : {'english' : 'French (Vanuatu)'},
'fr-wf' : {'english' : 'French (Wallis and Futuna)'},
'fr-yt' : {'english' : 'French (Mayotte)'},
'hr-ba' : {'english' : 'Croatian (Bosnia-Herzegovina)'},
'hr-hr' : {'english' : 'Croatian (Croatia)'},
'hu-hu' : {'english' : 'Hungarian (Hungary)'},
'hu-si' : {'english' : 'Hungarian (Slovenia)'},
'it-ch' : {'english' : 'Italian (Switzerland)'},
'it-hr' : {'english' : 'Italian (Croatia)'},
'it-it' : {'english' : 'Italian (Italy)'},
'it-si' : {'english' : 'Italian (Slovenia)'},
'it-sm' : {'english' : 'Italian (San Marino)'},
'ko-kp' : {'english' : 'Korean (Korea, North)'},
'ko-kr' : {'english' : 'Korean (Korea, South)'},
'ln-cd' : {'english' : 'Lingala (Democratic Republic of Congo)'},
'ln-cg' : {'english' : 'Lingala (Congo)'},
'ms-bn' : {'english' : 'Malay (Brunei)'},
'ms-my' : {'english' : 'Malay (Malaysia)'},
'ms-sg' : {'english' : 'Malay (Singapore)'},
'nl-an' : {'english' : 'Dutch (Netherlands Antilles)'},
'nl-aw' : {'english' : 'Dutch (Aruba)'},
'nl-be' : {'english' : 'Dutch (Belgium)'},
'nl-nl' : {'english' : 'Dutch (Netherlands)'},
'nl-sr' : {'english' : 'Dutch (Suriname)'},
'pt-ao' : {'english' : 'Português (Angola)'},
'pt-br' : {'native'  : 'Português (Brasil)', 'english' : 'Brazilian Portuguese', 'flag' : 'flag-br.gif'},
'pt-cv' : {'english' : 'Português (Ilhas Cabo Verde)'},
'pt-gw' : {'english' : 'Português (Guiné-Bissau)'},
'pt-mz' : {'english' : 'Português (Moçambique)'},
'pt-pt' : {'english' : 'Português (Portugal)'},
'pt-st' : {'english' : 'Português (São Tomé e Príncipe)'},
'sd-in' : {'english' : 'Sindhi (India)'},
'sd-pk' : {'english' : 'Sindhi (Pakistan)'},
'sr-ba' : {'english' : 'Serbian (Bosnia-Herzegovina)'},
'sr-yu' : {'english' : 'Serbian (Yugoslavia)'},
'ss-sz' : {'english' : 'Swati (Swaziland)'},
'ss-za' : {'english' : 'Swati (South Africa)'},
'sv-fi' : {'english' : 'Swedish (Finland)'},
'sv-se' : {'english' : 'Swedish (Sweden)'},
'sw-ke' : {'english' : 'Swahili (Kenya)'},
'sw-tz' : {'english' : 'Swahili (Tanzania)'},
'ta-in' : {'english' : 'Tamil (India)'},
'ta-sg' : {'english' : 'Tamil (Singapore)'},
'tn-bw' : {'english' : 'Tswana (Botswana)'},
'tn-za' : {'english' : 'Tswana (South Africa)'},
'tr-bg' : {'english' : 'Turkish (Bulgaria)'},
'tr-cy' : {'english' : 'Turkish (Cyprus)'},
'tr-tr' : {'english' : 'Turkish (Turkey)'},
'ur-in' : {'english' : 'Urdu (India)'},
'ur-pk' : {'english' : 'Urdu (Pakistan)'},
'zh-cn' : {'english' : 'Mandarin+Chinese (China)'},
'zh-hk' : {'english' : 'Mandarin+Chinese (Hongkong)'},
'zh-sg' : {'english' : 'Mandarin+Chinese (Singapore)'},
'zh-tw' : {'english' : 'Mandarin+Chinese (Taiwan)'}
}

# countries list from http://alioth.debian.org/projects/pkg-isocodes/
countries = {
'AD':'Andorra',
'AE':'United Arab Emirates',
'AF':'Afghanistan',
'AG':'Antigua and Barbuda',
'AI':'Anguilla',
'AL':'Albania',
'AM':'Armenia',
'AN':'Netherlands Antilles',
'AO':'Angola',
'AQ':'Antarctica',
'AR':'Argentina',
'AS':'American Samoa',
'AT':'Austria',
'AU':'Australia',
'AW':'Aruba',
'AX':'Åland Islands',
'AZ':'Azerbaijan',
'BA':'Bosnia and Herzegovina',
'BB':'Barbados',
'BD':'Bangladesh',
'BE':'Belgium',
'BF':'Burkina Faso',
'BG':'Bulgaria',
'BH':'Bahrain',
'BI':'Burundi',
'BJ':'Benin',
'BM':'Bermuda',
'BN':'Brunei Darussalam',
'BO':'Bolivia',
'BR':'Brazil',
'BS':'Bahamas',
'BT':'Bhutan',
'BV':'Bouvet Island',
'BW':'Botswana',
'BY':'Belarus',
'BZ':'Belize',
'CA':'Canada',
'CC':'Cocos (Keeling) Islands',
'CD':'Congo, The Democratic Republic of',
'CF':'Central African Republic',
'CG':'Congo',
'CH':'Switzerland',
'CI':"Cote d'Ivoire",
'CK':'Cook Islands',
'CL':'Chile',
'CM':'Cameroon',
'CN':'China',
'CO':'Colombia',
'CR':'Costa Rica',
'CS':'Serbia and Montenegro',
'CU':'Cuba',
'CV':'Cape Verde',
'CX':'Christmas Island',
'CY':'Cyprus',
'CZ':'Czech Republic',
'DE':'Germany',
'DJ':'Djibouti',
'DK':'Denmark',
'DM':'Dominica',
'DO':'Dominican Republic',
'DZ':'Algeria',
'EC':'Ecuador',
'EE':'Estonia',
'EG':'Egypt',
'EH':'Western Sahara',
'ER':'Eritrea',
'ES':'Spain',
'ET':'Ethiopia',
'FI':'Finland',
'FJ':'Fiji',
'FK':'Falkland Islands (Malvinas)',
'FM':'Micronesia, Federated States of',
'FO':'Faroe Islands',
'FR':'France',
'GA':'Gabon',
'GB':'United Kingdom',
'GD':'Grenada',
'GE':'Georgia',
'GF':'French Guiana',
'GH':'Ghana',
'GI':'Gibraltar',
'GL':'Greenland',
'GM':'Gambia',
'GN':'Guinea',
'GP':'Guadeloupe',
'GQ':'Equatorial Guinea',
'GR':'Greece',
'GS':'South Georgia and the South Sandwich Islands',
'GT':'Guatemala',
'GU':'Guam',
'GW':'Guinea-Bissau',
'GY':'Guyana',
'HK':'Hong Kong',
'HM':'Heard Island and McDonald Islands',
'HN':'Honduras',
'HR':'Croatia',
'HT':'Haiti',
'HU':'Hungary',
'ID':'Indonesia',
'IE':'Ireland',
'IL':'Israel',
'IN':'India',
'IO':'British Indian Ocean Territory',
'IQ':'Iraq',
'IR':'Iran, Islamic Republic of',
'IS':'Iceland',
'IT':'Italy',
'JM':'Jamaica',
'JO':'Jordan',
'JP':'Japan',
'KE':'Kenya',
'KG':'Kyrgyzstan',
'KH':'Cambodia',
'KI':'Kiribati',
'KM':'Comoros',
'KN':'Saint Kitts and Nevis',
'KP':"Korea, Democratic People's Republic of",
'KR':'Korea, Republic of',
'KW':'Kuwait',
'KY':'Cayman Islands',
'KZ':'Kazakhstan',
'LA':"Lao People's Democratic Republic",
'LB':'Lebanon',
'LC':'Saint Lucia',
'LI':'Liechtenstein',
'LK':'Sri Lanka',
'LR':'Liberia',
'LS':'Lesotho',
'LT':'Lithuania',
'LU':'Luxembourg',
'LV':'Latvia',
'LY':'Libyan Arab Jamahiriya',
'MA':'Morocco',
'MC':'Monaco',
'MD':'Moldova, Republic of',
'MG':'Madagascar',
'MH':'Marshall Islands',
'MK':'Macedonia, the former Yugoslavian Republic of',
'ML':'Mali',
'MM':'Myanmar',
'MN':'Mongolia',
'MO':'Macao',
'MP':'Northern Mariana Islands',
'MQ':'Martinique',
'MR':'Mauritania',
'MS':'Montserrat',
'MT':'Malta',
'MU':'Mauritius',
'MV':'Maldives',
'MW':'Malawi',
'MX':'Mexico',
'MY':'Malaysia',
'MZ':'Mozambique',
'NA':'Namibia',
'NC':'New Caledonia',
'NE':'Niger',
'NF':'Norfolk Island',
'NG':'Nigeria',
'NI':'Nicaragua',
'NL':'Netherlands',
'NO':'Norway',
'NP':'Nepal',
'NR':'Nauru',
'NU':'Niue',
'NZ':'New Zealand',
'OM':'Oman',
'PA':'Panama',
'PE':'Peru',
'PF':'French Polynesia',
'PG':'Papua New Guinea',
'PH':'Philippines',
'PK':'Pakistan',
'PL':'Poland',
'PM':'Saint Pierre and Miquelon',
'PN':'Pitcairn',
'PR':'Puerto Rico',
'PS':'Palestinian Territory, occupied',
'PT':'Portugal',
'PW':'Palau',
'PY':'Paraguay',
'QA':'Qatar',
'RE':'Reunion',
'RO':'Romania',
'RU':'Russian Federation',
'RW':'Rwanda',
'SA':'Saudi Arabia',
'SB':'Solomon Islands',
'SC':'Seychelles',
'SD':'Sudan',
'SE':'Sweden',
'SG':'Singapore',
'SH':'Saint Helena',
'SI':'Slovenia',
'SJ':'Svalbard and Jan Mayen',
'SK':'Slovakia',
'SL':'Sierra Leone',
'SM':'San Marino',
'SN':'Senegal',
'SO':'Somalia',
'SR':'Suriname',
'ST':'Sao Tome and Principe',
'SV':'El Salvador',
'SY':'Syrian Arab Republic',
'SZ':'Swaziland',
'TC':'Turks and Caicos Islands',
'TD':'Chad',
'TF':'French Southern Territories',
'TG':'Togo',
'TH':'Thailand',
'TJ':'Tajikistan',
'TK':'Tokelau',
'TL':'Timor-Leste',
'TM':'Turkmenistan',
'TN':'Tunisia',
'TO':'Tonga',
'TR':'Turkey',
'TT':'Trinidad and Tobago',
'TV':'Tuvalu',
'TW':'Taiwan, Province of China',
'TZ':'Tanzania, United Republic of',
'UA':'Ukraine',
'UG':'Uganda',
'UM':'United States Minor Outlying Islands',
'US':'United States',
'UY':'Uruguay',
'UZ':'Uzbekistan',
'VA':'Holy See (Vatican City State)',
'VC':'Saint Vincent and the Grenadines',
'VE':'Venezuela',
'VG':'Virgin Islands, British',
'VI':'Virgin Islands, U.S.',
'VN':'Viet Nam',
'VU':'Vanuatu',
'WF':'Wallis and Futuna',
'WS':'Samoa',
'YE':'Yemen',
'YT':'Mayotte',
'ZA':'South Africa',
'ZM':'Zambia',
'ZW':'Zimbabwe',
}

