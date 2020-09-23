import spider
import argparse

parser = argparse.ArgumentParser(description='Subreddit word cloud generator')

parser.add_argument('subreddit', nargs='?', type=str)
parser.add_argument('--mode', '-m', default='hot',
                    const='hot', nargs='?', type=str, choices=['hot', 'new', 'top'],)
parser.add_argument('--count', '-c', default=25,
                    const=25, nargs='?', type=int)
parser.add_argument('--width', '-W', nargs='?',
                    default=1200, const=1200, type=int)
parser.add_argument('--height', '-H', nargs='?',
                    default=600, const=600, type=int)
parser.add_argument('--max_words', nargs='?', default=100, const=100, type=int)
parser.add_argument('--background_color', '-C', nargs='?',
                    default='black', const='black', type=str)
parser.add_argument('--min_word_length', nargs='?',
                    default=3, const=3, type=int)
parser.add_argument('--include_numbers', action='store_true',)
parser.add_argument('--include_pinned',
                    action='store_true', dest="includePinned")
parser.add_argument('--normalize_plurals', action='store_true')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--expandMoreChildren', action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()
    Rspider = spider.reddit_spider()
    # Rspider.get_reddit_wordCloud(args.subreddit, debug=args.debug,mode=args.mode,count=args.count,
    # width=args.width,height=args.height,max_words=args.max_words,background_color=args)
    Rspider.get_reddit_wordCloud(**vars(args))
