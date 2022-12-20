import sklearn
import os
import pathlib
import enum

current_path = pathlib.Path(__file__).parent.resolve()
POS_COUNT = 29848
NEG_COUNT = 28901


class Tag(enum.Enum):
    Neutral = "NEUTRAL"
    Positive = "POSITIVE"
    Negative = "NEGATIVE"
    Not_defined = "NOT_DEFINED"


class Tweet:
    def __init__(self, text, real_tag=Tag.Not_defined, given_tag=Tag.Not_defined):
        self.text = text
        self.real_tag = real_tag
        self.given_tag = given_tag


tweets = []


def import_data():
    for i in range(POS_COUNT):
        text = ""
        with open("./data/" + str(i) + '.txt') as f:
            for line in f:
                text += line
        tweets.append(Tweet(text), Tag.Positive)
    for i in range(NEG_COUNT):
        text = ""
        with open("./data/" + str(i) + '.txt') as f:
            for line in f:
                text += line
        tweets.append(Tweet(text), Tag.Negative)


def main():
    import_data()


if __name__ == "__main__":
    main()
