from config import *
from analytics import Research


if __name__ == '__main__':
    research = Research(data_path)
    data = research.file_reader()
    counts = research.calc.counts()
    fractions = research.calc.fractions(counts[0], counts[1])
    predict_random = research.analytics.predict_random(num_of_step)
    random_tails = sum([el[0] for el in predict_random])
    random_heads = sum([el[1] for el in predict_random])
    predict_last = research.analytics.predict_last()
    text_report = report.format(len(data), counts[0], counts[1], fractions[0], fractions[1], num_of_step, random_heads, random_tails)
    research.analytics.save_file(text_report, save_file)
