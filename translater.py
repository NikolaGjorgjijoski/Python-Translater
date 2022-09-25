from googletrans import Translator

translator = Translator()

class Translate:

    def AutoSrcLanguage(Text, Dest):
        return translator.translate(Text, dest=Dest)
    
    def Translate(Text, Src, Dest):
        return translator.translate(Text, src=Src, dest=Dest)

class OtherTools():

    def LanguageDetection(Text):
        return translator.detect(Text)
    
    # Example = Words = ['The quick brown fox', 'jumps over', 'the lazy dog']
    def BulkTranslate(Words, Src, Dest):
        TranslatedWords = []
        for text in Words:
            TranslatedWords.append(Translate.Translate(text, Src, Dest))
        return TranslatedWords
