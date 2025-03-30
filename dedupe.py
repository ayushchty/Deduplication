from fuzzywuzzy import fuzz

class Dedupe: 
    def __init__(self, df):
        if df is None:
            raise ValueError("DataFrame cannot be None")
        self.original_df = df 
        self.df = df.copy()
        self.b=0
    
    def word_match_ayush(self):
        for i in self.df.select_dtypes(include=['object']).columns:
            a=self.df[i].str.lower().unique()
            d={}
            for j in range(len(a)):
                for k in range(j+1,len(a)):
                    score=fuzz.ratio(a[j],a[k])
                    if score>=80:
                        d[a[k]]=a[j]
                        self.b+=1
            self.df[i]=self.df[i].str.lower().replace(d)
        # print(self.b)
        return self.df,self.b

    def duplicate_count(self):
        return self.b if self.b>0 else 0
    
    def remove(self):
        self.df=self.df.drop_duplicates()
        return self.df
    def save(self):
        self.df.to_csv("cleaned.csv", index=False)
        print("File saved successfully")

    def word_match(self):
        for i in self.df.select_dtypes(include=['object']).columns:
            words = self.df[i].str.lower().unique()
            d={}
            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    score=fuzz.ratio(words[i], words[j])
                    if score>=80:
                        d[words[j]]=words[i]
            self.df[i] = self.df[i].str.lower().replace(d)
        return self.df
            
