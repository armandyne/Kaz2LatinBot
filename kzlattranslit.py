# -*- coding: utf-8 -*-
class kzlattranslit:
    __available_options = ['official-1', 'official-2', 'kazakgrammar']
            
    def __init__(self, cyrillic_text):
        self.cyrillic_text = cyrillic_text.lower()        
    
    def get_available_options(self):
        return self.__available_options
    
    def __do_official1(self):
        letters_mapping = { "а":"a", "ә":"ae", "б":"b", "в":"v", "д":"d", "е":"e", "ф":"f", "г":"g",
                            "ғ":"gh", "х":"h", "һ":"h", "і":"i", "и":"i", "й":"j", "ж":"zh", "к":"k",
                            "л":"l", "м":"m", "н":"n", "ң":"ng", "о":"o", "ө":"oe", "п":"p", "қ":"q",
                            "р":"r", "с":"s", "ш":"sh", "ч":"ch", "т":"t", "ұ":"u", "ү":"ue", "ы":"y",
                            "у":"w", "з":"z", "ц":"c"}                
        
        rep_slavic_letters_mapping = {"ь":"", "ъ":"", "щ":"шш", "э":"е",
                                      "ё":"е", "ию":"иу", "аю":"аиу",
                                      "ия":"иа", "ая":"аиа", "оя":"оиа"}                
        
        tmpstr = self.cyrillic_text
        
        for k, v in rep_slavic_letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
        
        for k, v in letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
                         
        return tmpstr
    
    def __do_official2(self):
        letters_mapping = { "а":"a", "ә":"a'", "б":"b", "в":"v", "д":"d", "е":"e", "ф":"f", "г":"g",
                            "ғ":"g'", "х":"h", "һ":"h", "і":"i", "и":"i'", "й":"i'", "ж":"j", "к":"k",
                            "л":"l", "м":"m", "н":"n", "ң":"n'", "о":"o", "ө":"o'", "п":"p", "қ":"q",
                            "р":"r", "с":"s", "ш":"s'", "ч":"c'", "т":"t", "ұ":"u", "ү":"u'", "ы":"y",
                            "у":"y'", "з":"z"}                
        
        rep_slavic_letters_mapping = {"ь":"", "ъ":"", "щ":"шш", "э":"е",
                                      "ё":"е", "ц":"тс", "ию":"иу", "аю":"аиу",
                                      "ия":"иа", "ая":"аиа", "оя":"оиа"}                
        
        tmpstr = self.cyrillic_text
        
        for k, v in rep_slavic_letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
        
        for k, v in letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
                         
        return tmpstr
      
    def __do_kazakgrammar(self):
        import re
        letters_mapping = {"а":"a", "ә":"ä", "б":"b", "ш":"c", "д":"d", "й":"y", "и":"y",
                           "e":"е", "г":"g", "ғ":"g", "ы":"ı", "і":"i", "ж":"j", "қ":"k",
                           "к":"k", "л":"l", "м":"m", "н":"n", "ң":"ŋ", "о":"o", "ө":"ö",
                           "п":"p", "р":"r", "с":"s", "т":"t", "ұ":"u", "ү":"ü", "у":"w",
                           "з":"z", "һ":"h", "х":"h", "ф":"f", "в":"v"}
        
        rep_slavic_letters_mapping = {"ь":"", "ъ":"", "ч":"ш", "щ":"ш", "э":"е", "ё":"е", "ию":"иу", "аю":"аиу", "ою":"оиу", 
                                      "үю":"үиу", "ұю":"ұиу", "ыю":"ыиу", "ію":"іиу", "ия":"иа", "ая":"аиа", "оя":"оиа"} 
        
        tmpstr = self.cyrillic_text
        for k, v in rep_slavic_letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
            
        words = re.findall("\w+|[^\w\s]", tmpstr)
        lst = []
        for word in words:    
            if word.isalpha():                                        
                word = re.sub(r"(^[^әүіеөаұыо]{0,}[әүіеөаұыо]{1})(и)", r"\1й", word)
                word = re.sub(r"([^қк]{0,})(и)([әүіеө]{1,})", r"\1ій\3", word)
                word = re.sub(r"([^қк]{0,})(и)([аұыо]{1,})", r"\1ый\3", word)
                
                word = re.sub(r"(\w{0,}қ)(и)", r"\1ый", word)
                word = re.sub(r"(\w{0,}к)(и)", r"\1ій", word)
                
                word = re.sub(r"([^қк]{0,})(и)([аұыо]{1,})", r"\1ый\3", word)
                
                word = re.sub(r"(^[^әүіеөаұыоу]{1,})(у)(\w{0,})", r"\1ұ\2\3", word)
                
                word = re.sub(r"^(у)(\w{0,}[әүіеө]{1,})", r"ү\1\2", word)
                word = re.sub(r"^(у)(\w{0,}[аұыо]{1,})", r"ұ\1\2", word)
                    
                word = re.sub(r"(^[^у][әүіеө]{1,}[^әүіеөаұыо]{1})(у)", r"\1і\2", word)
                word = re.sub(r"(^[^у][аұыо]{1,}[^әүіеөаұыо]{1})(у)", r"\1ы\2", word)   
                word = re.sub(r"(^[^әүіеөаұыо]{0,}[әүіеө]{1}[^әүіеөаұыо]{1,})(у)", r"\1і\2", word) 
                word = re.sub(r"(^[^әүіеөаұыо]{0,}[аұыо]{1}[^әүіеөаұыо]{1,})(у)", r"\1ы\2", word)
            lst.append(word)
        
        tmpstr = " ".join(lst)
        for k, v in letters_mapping.items():
            tmpstr = tmpstr.replace(k, v)
        
        tmpstr = re.sub(r"(\s{1,})([\.,;\:\)\]\!\?]{1,}\s{1,})", r"\2", tmpstr)
        tmpstr = re.sub(r"(\s{1,}[\(\[]{1,})(\s{1,})", r"\1", tmpstr)
        tmpstr = re.sub(r"(\s{1,})([\.,;\:]{1,}\s{1,})", r"\2", tmpstr)
        return tmpstr    
    
    def transliterate(self, option='kazakgrammar'):
        if option not in self.__available_options:
            raise ValueError("Invalid option. Call get_available_options() method")
        
        if option == self.__available_options[2]:            
            return self.__do_kazakgrammar()
        elif option == self.__available_options[0]:            
            return self.__do_official1()
        elif option == self.__available_options[1]:            
            return self.__do_official2()
