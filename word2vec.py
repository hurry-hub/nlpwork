# coding=utf-8
from itertools import islice
import jieba
from gensim.models import word2vec
import gensim
import time
import csv
import format_edit

def segment_depart(data_path, result_path):
    '''
    :param data_path: 实验一数据集.txt
    :param result_path: 分词结果.txt
    '''
    with open(data_path) as csvfile:
        csv_reader = list(csv.reader(csvfile))  # 使用csv.reader读取csvfile中的文件
        content = []
        result = ''
        count = 0

        for line in islice(csv_reader, 1, None):
            content.append(line[2])
            count = count + 1
            if count >= 2000:
                break

        for i in range(len(content)):
            # seg_list = jieba.cut(content[i])                                     # 使用jieba将实验文本分词
            for j in range(len(content[i])):
                seg_list = ''.join(content[i])
            res = ' O\n'.join(seg_list)                                             # 用space进行划分
            result = result + '\n' + res
        with open(result_path, 'w', encoding='utf-8') as f1:
            f1.write(result)

def train(segment_path, model_path):
    '''
    :param segment_path: 分词结果.txt
    :param model_path:  word2vec.model
    '''
    contain = segment_path
    sentences = word2vec.LineSentence(contain)
    model = word2vec.Word2Vec(sentences, window=20, min_count=1, workers=4, epochs=20)     # 利用word2vec训练词向量
    model.save(model_path)                                                      # 保存训练好的模型


if __name__ == "__main__":
    # 步骤1: jieba分词===============================================================================================
    time1 = time.time()
    segment_depart(r'./data/lxt.csv', r'./data/lxt_BME2.txt')
    time2 = time.time()
    print('Time for cut sentences: ' + str(time2 - time1) + 's')  # 计算得出分词时间

    # 步骤2: 训练词向量===============================================================================================
    # train(r'分词结果.txt', r'word2vec.model')
    time3 = time.time()
    print('Time for train: ' + str(time3 - time2) + 's')                        # 计算得出模型训练时间

    # 步骤3: 相关性对比===============================================================================================
    # model = gensim.models.Word2Vec.load(r'./data/word2vec.model')                       # 提取训练好的模型
    # model.wv.save_word2vec_format(r'w2v.txt', write_header=False)                                  # 保存词汇对应向量

    # format_edit.txt2json()


