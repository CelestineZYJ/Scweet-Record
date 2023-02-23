import nltk
# nltk.download()
nltk.download('omw-1.4')
from nltk import word_tokenize
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


from nltk.corpus import stopwords
words = stopwords.words('english')


f = open('../../irTempAdapt/tasks/stance/data/hugformat/train.csv', 'r')
lines = f.readlines()

top_words = {}

interpunctions = ['<','>','"',',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','🥴', '😂', '😔', '😭', '🤓', '😎', '😍', '🥰', '🤔', '🤣', '❗']
words = [word for word in words if word not in interpunctions]
stoplus = ['im', 'u','\'s','us', 'n\'t','..']
for i in range(ord('a'),ord('z')+1):
    stoplus.append(chr(i))
stops = list(stopwords.words("english"))+stoplus
stops = set(stops)

for line in lines:
    line = line.replace('<user>', '').lower()
    
    # hatespeech stance fakenews
    # sentence = line.strip('\n').split('\t')[2]
    
    # hash
    sentence = line.strip('\n').split('\t')[1]
    
    words = word_tokenize(sentence)
    #words = [porter_stemmer.stem(word) for word in words]
    words = [lemmatizer.lemmatize(word) for word in words]

    
    words = [word for word in words if word not in stops]
    
    for word in words:
        if len(word)>=5:
            try:
                top_words[word] += 1
            except:
                top_words[word] = 1


top_words = sorted(top_words.items(), key = lambda kv:(kv[1], kv[0]))
print(list(dict(top_words[-100:]).keys()))
