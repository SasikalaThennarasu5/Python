import argparse
import calc.basic as basic
import calc.advanced as advanced

def parse_args():
    parser = argparse.ArgumentParser(description="CLI Calculator")
    subparsers = parser.add_subparsers(dest="operation")

    for op in ['add', 'subtract', 'multiply', 'divide']:
        p = subparsers.add_parser(op)
        p.add_argument('a', type=str)
        p.add_argument('b', type=str)

    sqrt_parser = subparsers.add_parser('sqrt')
    sqrt_parser.add_argument('a', type=str)

    power_parser = subparsers.add_parser('power')
    power_parser.add_argument('a', type=str)
    power_parser.add_argument('b', type=str)

    return parser.parse_args()

def run():
    args = parse_args()
    op = args.operation

    if op == 'add':
        result = basic.add(args.a, args.b)
    elif op == 'subtract':
        result = basic.subtract(args.a, args.b)
    elif op == 'multiply':
        result = basic.multiply(args.a, args.b)
    elif op == 'divide':
        result = basic.divide(args.a, args.b)
    elif op == 'sqrt':
        result = advanced.sqrt(args.a)
    elif op == 'power':
        result = advanced.power(args.a, args.b)
    else:
        raise ValueError("Unknown operation")

    print(f"Result: {result}")
