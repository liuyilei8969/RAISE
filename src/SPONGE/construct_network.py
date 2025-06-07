import os
import pandas as pd
import networkx as nx
import argparse

def build_splicing_network(CRAB_dir, threshold, DE_dir, output_file):
    G = nx.DiGraph()

    for file_name in os.listdir(CRAB_dir):
        print(file_name)
        cell_line, rbp = file_name.split('_')[:2]
        print(cell_line, rbp)

        target_path = os.path.join(CRAB_dir, file_name, file_name + '_target.txt')
        target_data = pd.read_csv(target_path, sep='\t', low_memory=False, header=0)
        target_data['P(T|S, M, C)'] = pd.to_numeric(target_data['P(T|S, M, C)'])

        expr_file = os.path.join(DE_dir, f"{cell_line}_{rbp}_expr.txt")
        rbp_change_factor = 1  # Default value if no expression file

        if os.path.exists(expr_file):
            expr_data = pd.read_csv(expr_file, sep='\t', header=None)
            rbp_row = expr_data[expr_data.iloc[:, 1] == rbp]

            if not rbp_row.empty:
                try:
                    before = pd.to_numeric(rbp_row.iloc[0, 6], errors='coerce')
                    after = pd.to_numeric(rbp_row.iloc[0, 7], errors='coerce')
                    rbp_change_factor = before / after
                    if pd.isna(rbp_change_factor) or rbp_change_factor == 0:
                        rbp_change_factor = 1
                except Exception as e:
                    print(f"Error processing expression change for {rbp} in {cell_line}: {e}")
                    rbp_change_factor = 1
        else:
            print(f"Warning: Expression file {expr_file} not found. Using default rbp_change_factor = 1 for {rbp} in {cell_line}.")

        if 'P(T|S, M, C)' not in target_data.columns:
            print(f"Warning: Column 'P(T|S, M, C)' missing in {file_name}. Skipping.")
            continue

        for _, row in target_data.iterrows():
            event_id = row['event_id']

            if row['P(T|S, M, C)'] >= threshold:
                rbp_node = rbp
                event_node = event_id

                if rbp_node not in G:
                    G.add_node(rbp_node, type='RBP', role='source')
                if event_node not in G:
                    G.add_node(event_node, type='SplicingEvent', role='target', event_id=event_id)

                adjusted_dpsi = -row['IncLevelDifference'] / rbp_change_factor

                if G.has_edge(rbp_node, event_node):
                    current_impact = G[rbp_node][event_node]['weight']
                    if abs(adjusted_dpsi) > abs(current_impact):
                        G[rbp_node][event_node]['weight'] = adjusted_dpsi
                else:
                    G.add_edge(rbp_node, event_node, weight=adjusted_dpsi)

    nx.write_gexf(G, output_file)
    print(f"Graph saved as {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a splicing regulatory network from CRAB outputs and differential expression data.")
    parser.add_argument("--TargetResult", type=str, required=True, help="Path to the target identification results directory")
    parser.add_argument("--threshold", type=float, default=0.6, help="Threshold for conditional probability P(T|S, M, C) (default: 0.6)")
    parser.add_argument("--DE", type=str, required=True, help="Path to the differential expression data directory")
    parser.add_argument("--output", type=str, required=True, help="Output file path for the network graph (GEXF format)")

    args = parser.parse_args()
    build_splicing_network(args.CRAB, args.threshold, args.DE, args.output)
