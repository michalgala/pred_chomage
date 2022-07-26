import pandas as pd


def create_dataframe(start_nb:int):
    list1 = [x for x in range(start_nb, start_nb+5)]
    list2 = ["a","b","d","j","j"]

    df = pd.DataFrame(zip(list1,list2), columns = ['firstcol','secondcol'])
    
    return df