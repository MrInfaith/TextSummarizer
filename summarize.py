from nltk.corpus import stopwords
from heapq import nlargest
stopwords=stopwords.words('english')
class  preprocess:
    def formatting(self,text):
        text=text.split("\n")
        text = [s.replace(' ', '') for s in text]
        return text
    def Remove_Punctuation(self,text):
        import string 
        punc=string.punctuation
        def remove_punc(text):
            return text.translate(str.maketrans('','',punc))
        text=list(map(lambda s:remove_punc(s),text))
        return text
    def convert_lower(self,text):
        text=list(map(lambda s:s.lower(),text))
        return text
    def remove_stopwords(self,text):
        text = [word for word in text if word not in stopwords]
        return text
class summarization:
    def summarize(self,text,sentences):
        word_frequencies={}
        for word in text:
            if word not in word_frequencies.keys():
                word_frequencies[word]=1
            else:
                word_frequencies[word]+=1
        max_frequency=max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word]=word_frequencies[word]/max_frequency
        sentences_scores={}
        for sent in sentences:
            for word in sent:
                if word.lower() in word_frequencies.keys():
                    if sent not in sentences_scores.keys():
                        sentences_scores[sent]=word_frequencies[word.lower()]
                    else:
                        sentences_scores[sent]+=word_frequencies[word.lower()]
        
        select_length=int(len(sentences)*0.35)
        summary=nlargest(select_length,sentences_scores,key=sentences_scores.get)
        final_summary=[word for word in summary]
        final_summary='.'.join(final_summary)
        return final_summary




