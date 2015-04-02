from langdetect import detect_langs
from gtts import gTTS


class Speaker:
    def __init__(self, preferred_language):
        self.preferred_language = preferred_language

    def discover_language(self, *sentences):
        text =  '. '.join(sentences)
        candidates = {candidate.lang: candidate.prob 
                      for candidate in  detect_langs(text)}

        lang = max(candidates, key=candidates.get)

        delta = candidates.get(lang) - (candidates.get(self.preferred_language) or 0)
        if delta < 0.1:
            return self.preferred_language

        return lang

    def record(self, text, language = None):
        try:
            return gTTS(text=text, lang=language or self.preferred_language) 
        except:
            return gTTS(text=text, lang=self.preferred_language) 
