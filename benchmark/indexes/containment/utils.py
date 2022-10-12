import numpy as np


def get_precision_recall(found, reference):
    reference = set(reference)
    intersect = sum(i in reference for i in found)
    precision = 0.0 if len(found) == 0 else float(intersect) / float(len(found))
    recall = float(intersect) / float(len(reference)) if reference else 1.0
    if len(found) == len(reference) == 0:
        precision = 1.0
        recall = 1.0
    return [precision, recall]


def fscore(precision, recall):
    if precision == 0.0 and recall == 0.0:
        return 0.0
    return 2.0 / (1.0 / precision + 1.0 / recall)


def average_fscore(founds, references):
    return np.mean([fscore(*get_precision_recall(found, reference))
                    for found, reference in zip(founds, references)])
