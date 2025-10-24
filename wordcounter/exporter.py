import os
import pandas as pd
import matplotlib.pyplot as plt

def export_to_excel(dataframe, filename):
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    dataframe.to_excel(filename, index=False)

def create_scatter_plot(data, title, style='dark_background'):
    try:
        plt.style.use(style) 
    except:
        print(f"Warning: Could not load style '{style}'. Using default.")
        plt.style.use('default') 

    fig, ax = plt.subplots(figsize=(17, 6))
    
    ax.plot(range(len(data)), data['Frequency'], marker='o', linestyle=':', markersize=6, label='Frequency')
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(data['Words'], rotation=90, fontsize=8)
    ax.set_title(title)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.legend()
    plt.tight_layout()
    
    return fig