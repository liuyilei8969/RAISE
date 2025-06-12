import argparse
from SPONGE import find_target, construct_network, calculate_activity

def main():
    parser = argparse.ArgumentParser(description="SPONGE: Splicing-factor activity prediction framework")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subcommand: find_target
    parser_find = subparsers.add_parser("find_target", help="Identify splicing targets of an RBP")
    parser_find.add_argument('--rmats', required=True)
    parser_find.add_argument('--clip_peaks', required=True)
    parser_find.add_argument('--ref_genome', required=True)
    parser_find.add_argument('--rbp_motif', required=True)
    parser_find.add_argument('--rbp_name', required=True)
    parser_find.add_argument('--output', required=True)
    parser_find.add_argument('--cell_line', required=True)

    # Subcommand: construct_network
    parser_net = subparsers.add_parser("construct_network", help="Construct splicing regulatory network")
    parser_net.add_argument('--CRAB', required=True)
    parser_net.add_argument('--threshold', type=float, default=0.6)
    parser_net.add_argument('--DE', required=True)
    parser_net.add_argument('--output', required=True)

    # Subcommand: calculate_activity
    parser_act = subparsers.add_parser("calculate_activity", help="Estimate RBP activity")
    parser_act.add_argument('--diffAS', required=True)
    parser_act.add_argument('--gexf', required=True)
    parser_act.add_argument('--out', required=True)

    args = parser.parse_args()

    if args.command == "find_target":
        find_target.main(args)
    elif args.command == "construct_network":
        construct_network.build_splicing_network(args.CRAB, args.threshold, args.DE, args.output)
    elif args.command == "calculate_activity":
        calculate_activity.main(args.diffAS, args.gexf, args.out)

if __name__ == "__main__":
    main()
