import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.lines import Line2D

# Function to read data from CSV
def read_csv(csv_file):
    categories = []
    pathways = []
    num_genes = []
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            categories.append(row['Category'])
            pathways.append(row['Pathway'])
            num_genes.append(int(row['Number of Genes']))
    
    return categories, pathways, num_genes

# Function to plot the graph and save as JPG
def plot_data(categories, pathways, num_genes, output_file):
    # Split data into groups
    groups = {}
    for category, pathway, num in zip(categories, pathways, num_genes):
        if category not in groups:
            groups[category] = []
        groups[category].append((pathway, num))
    
    # Create a list for plotting
    pathway_labels = []
    values = []
    colors = []
    group_starts = []
    group_labels = list(groups.keys())
    
    # Prepare the categories and values
    group_start = 0
    color_map = plt.cm.Pastel1  # Use the pastel colormap for gentle pastel colors
    for group_index, (group, pathways) in enumerate(groups.items()):
        for pathway, num in pathways:
            pathway_labels.append(pathway)
            values.append(num)
            colors.append(color_map(group_index / len(groups)))  # Use color palette for each group
        group_starts.append(group_start)
        group_start += len(pathways)

    # Create the plot with 3600x4200 size (in inches, DPI will handle the pixel resolution)
    fig, ax = plt.subplots(figsize=(12, 14))  # Adjust size for better appearance
    bars = ax.barh(pathway_labels, values, color=colors, height=0.8)  # Add some bar height spacing

    # Add labels and title with improved fonts and sizes
    ax.set_xlabel('Number of Genes', fontsize=14, fontweight='bold', color='black')
    ax.set_ylabel('Pathway', fontsize=14, fontweight='bold', color='black')
    ax.set_title('Genes in Pathways by Group', fontsize=16, fontweight='bold', color='black')

    # Customize ticks and labels
    ax.tick_params(axis='y', labelsize=12, rotation=0, labelcolor='black', pad=15)  # Increase padding to separate the labels more
    ax.tick_params(axis='x', labelsize=12, labelcolor='black')
    
    # Remove gridlines and background lines
    ax.grid(False)  # Disable all gridlines

    # Add legend with improved styling and consistent colors
    handles = [Line2D([0], [0], color=color_map(i / len(groups)), lw=4) for i in range(len(groups))]
    ax.legend(handles, group_labels, title='Group', fontsize=12, title_fontsize=13, loc='upper right')

    # Remove bar borders
    for bar in bars:
        bar.set_edgecolor('none')  # Remove bar borders for a cleaner look

    # Add better spacing and layout
    plt.tight_layout()

    # Save the plot as a JPG file with higher resolution (dpi=300)
    plt.savefig(output_file, format='jpg', dpi=300)
    print(f"Plot saved as {output_file}")

# Main function
def main(csv_file, output_file):
    categories, pathways, num_genes = read_csv(csv_file)
    plot_data(categories, pathways, num_genes, output_file)



# Example usage
csv_file = 'c:/Users/fysh4/OneDrive/桌面/top20_each_group_GO.csv'  # Replace with the path to your CSV file
output_file = 'c:/Users/fysh4/OneDrive/桌面/top20_each_group_GO.jpg'  # The path where the JPG file will be saved
main(csv_file, output_file)
