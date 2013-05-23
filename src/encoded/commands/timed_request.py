import requests
import timeit


def run(url, obj, n):
    def getit():
        requests.get(url+obj+'/?format=json')

    T = timeit.Timer(getit)
    t2run = T.timeit(number=n)
    print "Ran %s %d times in %f seconds" % (url+obj, n, t2run)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Time a URL')
    parser.add_argument('url')
    parser.add_argument('obj')
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    run(args.url, args.obj, args.n)

if __name__ == '__main__':
    main()
