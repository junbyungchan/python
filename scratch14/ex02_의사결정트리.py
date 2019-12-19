import math
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple, Counter, defaultdict
from typing import NamedTuple


# Candidate = namedtuple('Candidate',
#                        ('level', 'lang', 'tweets', 'phd', 'result'))
class Candidate(NamedTuple):  # NamedTuple을 상속받는 클래스 선언
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool = None  # 클래스 선언 방식의 NamedTuple은 field의 기본값을 설정할 수 있음.


def uncertainty(p):
    """ 0 <= p <= 1
    확률 p=0이면, 사건이 "항상" 발생하지 않는다 -> 불확실성 0
    확률 p=1이면, 사건이 "항상" 발생한다. -> 불확실성 0
    확률 0<p<1이면, 사건이 발생할 수도, 발생하지 않을 수도 있다. -> 불확실성이 있다.
    """
    return -p * math.log(p, 2)  # 2를 밑수로 하는 로그 함수


def entropy(class_probabilities):
    """ 엔트로피: 각 클래스의 불확실성의 정도를 모두 더한 값.
    주어진 확률들의 리스트에 대해서 엔트로피를 계산
    E = sum(i) [uncertainty(p_i)] = -p_1 * log(p_1) - p_2 * log(p_2) - ...
    """
    ent = 0
    for p in class_probabilities:
        if p != 0:
            ent += uncertainty(p)
            # 만약 p=0이면 log(p)를 계산할 때 Error가 발생하기 때문에
    return ent


def binary_entropy(p):
    """사건이 일어날 확률 p, 사건이 일어나지 않을 확률 (1-p)
    Entropy = -p * log(p) - (1-p) * log(1-p)
    """
    return uncertainty(p) + uncertainty(1-p)


def class_probabilities(labels):
    total_count = len(labels)
    counts = Counter(labels)  # {label_1: cnt_1, label_2: cnt_2, ...}
    print(counts)
    # probabilities = []
    # for count in counts.values():
    #     p = count / total_count  # 각 레이블의 확률
    #     probabilities.append(p)
    probabilities = [count/total_count for count in counts.values()]
    return probabilities


def partition_by(dataset, attr_name):
    """NamedTuple들의 리스트로 이루어진 dataset를
    NamedTuple의 특정 attribute로 partitioning"""
    partitions = defaultdict(list)  # list를 value로 갖는 dict
    for sample in dataset:
        # 해당 attr_name의 값을 찾아서
        key = getattr(sample, attr_name)
        # dict의 키로 사용해서 sample을 저장.
        partitions[key].append(sample)
    return partitions


def partition_entropy_by(dataset, by_partition, by_entropy):
    """by_partition(attr_name)으로 분리된 각 파티션에서
    by_entropy(label_name)의 엔트로피를 각각 계산하고,
    파티션 내에서의 엔트로피 * 파티션의 비율 들의 합을 리턴.
    """
    # 파티션을 나눔
    partitions = partition_by(dataset, by_partition)

    # 클래스(레이블) 별 확률을 계산하기 위해서 레이블들의 리스트를 생성
    labels = []
    for partition in partitions.values():  # 파티션 개수만큼 반복
        values = []
        for sample in partition:  # 파티션의 원소 개수만큼 반복
            values.append(getattr(sample, by_entropy))
        labels.append(values)
    print(labels)
    # 각 파티션이 차지하는 비율을 계산하고,
    # 각 파티션에서의 엔트로피에 그 비율을 곱해주기 위해서
    total_count = sum(len(label) for label in labels)
    ent = 0
    for label in labels:
        # 파티션이 가지고 있는 클래스들의 확률 리스트
        cls_prob = class_probabilities(label)  # [2/5, 3/5]
        part_ent = entropy(cls_prob)  # 파티션의 엔트로피
        # 파티션 엔트로피 * 파티션의 비율
        ent += part_ent * len(label) / total_count
    return ent






if __name__ == '__main__':
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]

    # uncertainty 함수 그래프
    x_pts = np.linspace(0.0001, 1, 100)
    y_pts = [uncertainty(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('y = -p * log(p)')
    plt.xlim(0.0)  # 0 <= x
    plt.ylim(0.0)  # 0 <= y
    plt.show()

    # binary_entropy 함수 그래프
    x_pts = np.linspace(0.0001, 0.9999, 100)
    y_pts = [binary_entropy(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('binary entropy')
    plt.axvline(x=0.5, color='0.75')
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

    # entropy 함수 테스트
    rain_prob = [1, 0]  # 비가 올 확률 100%
    ent = entropy(rain_prob)
    print('entropy =', ent)  # 엔트로피 = 0 (최소 엔트로피/불확실성)

    rain_prob = [0.5, 0.5]  # 비가 올 확률 50%
    print('entropy =', entropy(rain_prob))  # 엔트로피 = 1.0 (최대 엔트로피/불확실성)

    rain_prob = [0.9, 0.1]  # 비가 올 확률 90%
    print('entropy =', entropy(rain_prob))  # 엔트로피 = 0.47

    # class_probabilities 함수 테스트
    level = ['junior', 'senior', 'mid', 'junior']
    # P(junior) = 2/4, P(senior) = 1/4, P(mid) = 1/4
    cls_prob = class_probabilities(level)
    print(cls_prob)

    # partition_by 함수 테스트
    partition_by_level = partition_by(candidates, 'level')
    print('partition_by_level:', partition_by_level)
    partition_by_tweet = partition_by(candidates, 'tweets')
    print('partition_by_tweets:', partition_by_tweet)

    # partition_entropy_by 함수 테스트
    # 전체 지원자들을 level로 파티션을 나눠서 result의 엔트로피를 계산
    ent_level = partition_entropy_by(candidates, 'level', 'result')
    print('entropy partitioned by level:', ent_level)
    ent_lang = partition_entropy_by(candidates, 'lang', 'result')
    print('entropy partitioned by lang', ent_lang)

