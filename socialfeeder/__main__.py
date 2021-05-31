import argparse, sys
from socialfeeder import feeder

def main():
    parser = argparse.ArgumentParser(prog='feeder')
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0.0')

    parser.add_argument('--social',            help='Social network name', type=str, default='facebook')
    parser.add_argument('--config',            help='Configuration file', type=str, default='facebook')

    args = parser.parse_args()
    feeder.run( social      = args.social,
                config      = args.config)

if __name__ == '__main__':
    main()