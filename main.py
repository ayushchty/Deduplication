'''
$ docker build -t dedupe .
$ docker run -it --rm --name my-running-app dedupe
'''


from load import FileChecker
from dedupe import Dedupe

def main():
    path = input("Enter the file path: ")
    file = FileChecker(path)
    print("Checking deduplication records!")
    df=file.get_dataframe()
    dd = Dedupe(df)
    f=dd.word_match_ayush()
    print("Number of duplicate records: ", dd.duplicate_count())
    print("Duplicate Entries: ", f)

    if input("Do you want to remove the duplicate records? (y/n)") in ["y", "Y"]:
        dd.remove()
        print("File modified successfully!")

    if input("Do you want to save the modified file? (y/n)") in ["y", "Y"]:
        dd.save()
        # print("File saved successfully!")

# if __name__=="__main__":
#     main()

