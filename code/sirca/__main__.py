#!/usr/bin/env python
import logging
import statistics

import server
import model
import cell

print("HELLLO GOODBYE")

if __name__ == '__main__':
    import argparse
    print("HELLLO GOODBYE MAIN")

    parser = argparse.ArgumentParser(description='Run model', epilog='live long and prosper!')
    parser.add_argument('-i', action='store', type=float, default=2.0, help='Provide infectiousness (2.0 by default)')
    parser.add_argument('-d', action='store', type=int, default=5, help='Provide infectiousness_duration (5 by default)')
    parser.add_argument('-r', action='store', type=int, default=10, help='Provide h_infectiousness (10 by default)')
    parser.add_argument('-v', action='store', type=int, default=10, help='Provide h_infectiousness (10 by default)')
    args = parser.parse_args()
    if args.v == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.v == 2:
        logging.basicConfig(level=logging.WARNING)
    elif args.v == 3:
        logging.basicConfig(level=logging.DEBUG)
    logging.info(args)

    # TODO this dirty trick sadly did not work: find another way or abandon.
    try:
        s = server.make_server(args.i, args.d, args.r)
        s.launch()
    except statistics.StatisticsError:
        print("THERE ARE NO MORE INFECTED CELLS")
    finally:
        print("TERMINATING!")
else:
    s = server.make_server()