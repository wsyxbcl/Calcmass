from __future__ import print_function
import argparse

from calcmass import mass


def main():
    parser = argparse.ArgumentParser(description='Calculate molar mass of a chemical compound.', prog='calcmass')
    parser.add_argument('compounds', metavar='C', nargs='+',
                        help='a compound to find the mass of')
    args = parser.parse_args()
    for a in args.compounds:
        val = mass.add_markers(a)
        elements = mass.strip_coeff(val)
        if len(elements) == 0:
            raise argparse.ArgumentParser.error(parser, 'Not a compound')
        if len(args.compounds) > 1:
            print(a + ':', end=' ')
        if type(mass.calculate(elements)) != str:
            print("%0.5f" % mass.calculate(elements))
        else:
            raise argparse.ArgumentParser.error(parser, 'Not a compound: ' +
                                                mass.calculate(elements))
        mass.multiples.clear()

if __name__ == "__main__":
    main()
