import argparse

from drop_reference import dropreference_components


def main():
    parser = argparse.ArgumentParser(description="Scrape drop reference data")
    parser.add_argument('--model', type=str, required=True, help="Component model to scrape")
    parser.add_argument('--type', type=str, required=True, help="Component type to scrape")
    args = parser.parse_args()
    dropreference_components(args.type, args.model)


if __name__ == "__main__":
    main()
