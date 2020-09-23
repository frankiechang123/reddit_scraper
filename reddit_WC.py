import spider
import argparse

parser = argparse.ArgumentParser(description='Subreddit word cloud generator')

parser.add_argument('subreddit', nargs='?', type=str,
                    help='name of the subreddit')
parser.add_argument('--mode', '-m', default='hot', help='choose one of the three modes',
                    const='hot', nargs='?', type=str, choices=['hot', 'new', 'top'],)
parser.add_argument('--count', '-c', default=25, help='num of posts to be processed',
                    const=25, nargs='?', type=int)
parser.add_argument('--expandMoreChildren', '-e', action='store_true',
                    help='whether to trace through MoreChildren links. May cause long execution time.')
parser.add_argument('--width', '-W', nargs='?', help='width of the word cloud, default=1200',
                    default=1200, const=1200, type=int)
parser.add_argument('--height', '-H', nargs='?', help='height of the word cloud, default = 600',
                    default=600, const=600, type=int)
parser.add_argument('--max_words', nargs='?', default=100,
                    const=100, type=int, help='maximum num of words in word cloud')
parser.add_argument('--background_color', '-C', nargs='?', help='background color',
                    default='black', const='black', type=str)
parser.add_argument('--min_word_length', nargs='?', help='minimum word length to be considered',
                    default=3, const=3, type=int)
parser.add_argument('--include_numbers', action='store_true')
parser.add_argument('--include_pinned',
                    action='store_true', dest="includePinned", help='whether to include pinned posts in subreddit')
parser.add_argument('--normalize_plurals', action='store_true')
parser.add_argument('--debug', action='store_true', help='show more detail')


if __name__ == "__main__":
    args = parser.parse_args()
    Rspider = spider.reddit_spider()
    # Rspider.get_reddit_wordCloud(args.subreddit, debug=args.debug,mode=args.mode,count=args.count,
    # width=args.width,height=args.height,max_words=args.max_words,background_color=args)
    Rspider.get_reddit_wordCloud(**vars(args))
