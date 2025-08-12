import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df = pd.read_csv('C:/Users/fysh4/OneDrive/桌面/De novo/KEGG.csv')

# Set up the figure and axis
plt.figure(figsize=(10, 12))  # 調整尺寸適應橫向圖

# Create a horizontal barplot
sns.barplot(y='b_level', x='Number of gene', data=df, hue='a_level', 
            palette='Set2', width=0.8, linewidth=1.5, dodge=False)

# Customize labels and title
plt.title('Gene Distribution by Category and Pathway Type', fontsize=16)
plt.xlabel('Number of Genes', fontsize=14)
plt.ylabel('KEGG Pathway Categories (b_level)', fontsize=14)

# Adjust y-axis labels for better readability
plt.yticks(fontsize=10)

# Adjust layout
plt.tight_layout()

# Modify legend (move to bottom right, adjust size)
plt.legend(title=None, prop={'size': 10}, loc='lower right', bbox_to_anchor=(1, 0))  

# Save the figure
plt.savefig("C:/Users/fysh4/OneDrive/桌面/De novo/KEGG.jpg", dpi=600, bbox_inches='tight')

# Show the plot
plt.show()
