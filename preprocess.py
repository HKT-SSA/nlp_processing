import abc
from typing import List, Tuple
class ClassificationCorpusPreprocessor(abc.ABC):
    '''
    input: path to input file
    return: list of tuples (class_no, class_name, text)
    '''

    @abc.abstractmethod
    def preprocess(self, file_path:str)->List[Tuple[str, str, str]]:
        pass

class TouTiaoNewsPreprocessor(ClassificationCorpusPreprocessor):
    '''
    https://github.com/skdjfla/toutiao-text-classfication-dataset.git
    example of toutiaonews docs
    _!_101_!_news_culture_!_林徽因什么理由拒绝了徐志摩而选择梁思 > 成为终身伴侣？_!_
    6552475601595269390
    _!_101_!_news_culture_!_黄杨木是什么树？_!_
    6552387648126714125
    _!_101_!_news_culture_!_上联：草根登上星光道，怎么对下联？_!_
    6552271725814350087
    _!_101_!_news_culture_!_什么是超写实绘画？_!_
    6552452982015787268
    _!_101_!_news_culture_!_松涛听雨莺婉转，下联？_!_
    '''
    def __init__(self):
        self.delimeter = '_!_'

    def preprocess(self, file_path:str) ->List[Tuple[str, str, str]]:
        file = open(file_path, 'r')
        res = []
        for l in file.readlines():
            toks = l.split(self.delimeter)
            classno = toks[1]
            classname = toks[2]
            title = toks[3]
            res.append((classno, classname, title))
        return res

