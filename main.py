from preprocess import TouTiaoNewsPreprocessor
from segmenter import CKIPSegmenter
from transformer import BlazingTextInputDataTransformer

preprocessor = TouTiaoNewsPreprocessor()
res = preprocessor.preprocess('/Users/yianc/workspace/toutiao-text-classfication-dataset/toutiao_cat_data.txt')
segmenter = CKIPSegmenter()
transformer = BlazingTextInputDataTransformer()
for r in res:
    toks = segmenter.segment(r[2])
    input = transformer.transform((r[0], r[1], toks))
    print(input)