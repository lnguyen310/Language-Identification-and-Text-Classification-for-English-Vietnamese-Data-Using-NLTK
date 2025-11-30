#libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#downloading nltk resources 
#tokenizing text into words
nltk.download('punkt')
nltk.download('punkt_tab')
#getting the list of common stopwords
nltk.download('stopwords')

#preprocessing function
def preprocess_text(text):
    #converting to lowercase & splitting the text into a list of words 
    tokens = word_tokenize(text.lower())
    
    #common stopwords (ex: 'like', 'the', 'is', etc.)
    stop_words = set(stopwords.words('english'))
    
    #removing stopwords from list 
    cleaned_tokens = [word for word in tokens if word not in stop_words]
    
    #return the cleaned list of words
    return cleaned_tokens

#detecting language function
def detect_language(tokens):
    #Vietnamese accent marks characters
    vietnamese_diacritics = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủửừũôồốộổỗơờớợởỡ"
    
    #flags for language detection
    contains_vietnamese = False
    contains_english = False
    
    #storing words that is identified as Vietnamese or English 
    vietnamese_words = []
    english_words = []
    
    #checking each word to see if it has accent marks or not to determine which language it is
    for word in tokens:
        #if the word contains Vietnamese accent marks
        if any(char in vietnamese_diacritics for char in word):
            contains_vietnamese = True
            vietnamese_words.append(word)
        #for english words and only taking alphabetic words 
        elif word.isalpha():
            contains_english = True
            english_words.append(word)
    
    #return detected language and identified words
    if contains_vietnamese and contains_english:
        return "Mixed", vietnamese_words, english_words
    elif contains_vietnamese:
        return "Vietnamese", vietnamese_words, []
    elif contains_english:
        return "English", [], english_words
    else:
        return "Unknown", [], []

#classifying categories function 
#function will classify text to see which category the text belongs to either news, sports, entertainment
def classify_text(tokens):
    #define keywords list for each category
    news_keywords = ["government", "election", "president", "news", "politics", "chính phủ", "cuộc bầu cử", "chủ tịch", "tin tức", "chính trị"]
    sports_keywords = ["football", "basketball", "tennis", "athlete", "match", "bóng đá", "bóng rổ", "quần vợt", "vận động viên"]
    entertainment_keywords = ["movie", "actor", "celebrity", "music", "concert", "bộ phim", "diễn viên", "người nổi tiếng", "âm nhạc", "buổi hòa nhạc"]
    
    #counting how many times each category's keywords appear in text
    news_count = sum(1 for word in tokens if word in news_keywords)
    sports_count = sum(1 for word in tokens if word in sports_keywords)
    entertainment_count = sum(1 for word in tokens if word in entertainment_keywords)

    #finding category with highest match of keywords
    if news_count > sports_count and news_count > entertainment_count:
        return "News"
    elif sports_count > news_count and sports_count > entertainment_count:
        return "Sports"
    elif entertainment_count > news_count and entertainment_count > sports_count:
        return "Entertainment"
    else:
        return "Un-categorized"

#combining everything into 1 function to analyze the text
def analyze_text(text):
        #preprocess text into words
        tokens = preprocess_text(text)
        
        #detecting language
        language, vietnamese_words, english_words = detect_language(tokens)
        
        #classifying text
        category = classify_text(tokens)
        
        #determining if the text is fully Vietnamese, English, or Mixed
        if language == "Mixed":
            text_category = "Mixed"
        elif language == "Vietnamese" and not english_words:
            text_category = "Fully Vietnamese"
        elif language == "English" and not vietnamese_words:
            text_category = "Fully English"
        else:
            text_category = "Mixed"
        
        return language, vietnamese_words, english_words, category, text_category

#test text
text_1 = "The actor from my favorite movie says she loves eating Bún bò Huế."
text_2 = "Vào năm 2019, chính phủ và thế giới đóng cửa vì đại dịch." 
text_3 = "The football team won their final match of the season!"

#analyzing text
result_1 = analyze_text(text_1)
result_2 = analyze_text(text_2)
result_3 = analyze_text(text_3)

#print out results 
print("\n########## Results ##########")
print(f"\nText 1 Analysis: Language: {result_1[0]}, Vietnamese Words: {result_1[1]}, English Words: {result_1[2]}, Category: {result_1[3]}, Text Category: {result_1[4]}")
print(f"\nText 2 Analysis: Language: {result_2[0]}, Vietnamese Words: {result_2[1]}, English Words: {result_2[2]}, Category: {result_2[3]}, Text Category: {result_2[4]}")
print(f"\nText 3 Analysis: Language: {result_3[0]}, Vietnamese Words: {result_3[1]}, English Words: {result_3[2]}, Category: {result_3[3]}, Text Category: {result_3[4]}")