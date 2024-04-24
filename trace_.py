import networkx as nx
import matplotlib.pyplot as plt
import csv

def extract_column_data(filename, column_name):
    column_data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            column_data.append(row[column_name])
    return column_data

def process_data(from_column, to_column, amount_column):
    transactions = []
    for i in range(len(from_column)):
        transaction = {
            "from": from_column[i],
            "to": to_column[i],
            "amount": float(amount_column[i])  
        }
        transactions.append(transaction)
    return transactions

def main():
    filename = 'Transaction.csv'  
    from_column = extract_column_data(filename, 'From') 
    to_column = extract_column_data(filename, 'To')  
    amount_column = extract_column_data(filename, 'Amount')  
    
    transactions = process_data(from_column, to_column, amount_column)
    
    print("Transactions:")
    for transaction in transactions:
        print(transaction)

    # Create a directed graph
    G = nx.DiGraph()

    # transactions as edges
    for tx in transactions:
        G.add_edge(tx["from"], tx["to"], amount=tx["amount"])

    # Visualize the graph
    pos = nx.spring_layout(G)  # Define the layout of the nodes
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=5, font_weight="bold")

    # Set edge width based on transaction amount
    edge_widths = [tx["amount"] / 10 for tx in transactions]  # Scaling down for better visualization
    edges = nx.draw_networkx_edges(G, pos, width=edge_widths)

    # Show the plot
    plt.show()

    # Basic graph analysis
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())
    print("Nodes:", G.nodes())
    print("Edges:", G.edges())

    # Calculate centrality measures
    centrality = nx.degree_centrality(G)
    print("Node centrality:", centrality)

if __name__ == "__main__":
    main()
