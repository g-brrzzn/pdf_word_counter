import os
import pandas as pd
import matplotlib.pyplot as plt

def export_to_excel(dataframe, filename):
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    dataframe.to_excel(filename, index=False)

def create_scatter_plot(data, title, style=None):
    if style:
        try:
            plt.style.use(style)
        except:
            print(f"Warning: Could not load style '{style}'. Using default.")

    plt.figure(figsize=(17, 6))
    plt.plot(range(len(data)), data['Frequency'], marker='o', linestyle=':', markersize=6, label='Frequency')
    plt.xticks(range(len(data)), data['Words'], rotation=90, fontsize=8)
    plt.title(title)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()