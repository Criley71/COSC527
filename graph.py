import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_assignment_graphs(csv_filename):
    # 1. Custom Parser to handle multi-experiment structure
    data = []
    current_exp = None
    headers = None
    
    with open(csv_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(","): continue

            if line.startswith("Experiment #:"):
                current_exp = line.split(',')[1].strip()
                continue
                

            if line.startswith("Step,"):
                headers = [h.strip() for h in line.split(',')]
                continue
                
            parts = line.split(',')
            if parts[0].isdigit() and headers:
                row = {headers[i]: parts[i].strip() for i in range(len(headers))}
                row['ExperimentID'] = current_exp
                data.append(row)

    df = pd.DataFrame(data)

    metrics = ['Lambda', 'Lambda_t', 'H', 'H_t', 'Lempel-Ziv Complexity']
    for col in metrics:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    def map_behavior(c):
        c = str(c).upper().strip()
        if c in ['1', '2']: return 0
        if c in ['4']: return 1
        if c in ['3']: return 2
        return np.nan

    df['Behavior'] = df['Class'].apply(map_behavior)

    for param in metrics:
        plt.figure(figsize=(10, 6))
        experiments = df['ExperimentID'].unique()
        colors = plt.cm.get_cmap('tab20', len(experiments))
        
        for i, exp_id in enumerate(experiments):
            exp_data = df[df['ExperimentID'] == exp_id].dropna(subset=[param, 'Behavior'])
            exp_data = exp_data.sort_values(by=param)
            

            plt.scatter(exp_data[param], exp_data['Behavior'], label=f'Exp {exp_id}', 
                        color=colors(i), alpha=0.6, s=40)
            plt.plot(exp_data[param], exp_data['Behavior'], color=colors(i), alpha=0.5)

        plt.title(f"Behavioral Class vs {param}")
        plt.xlabel(param)
        plt.ylabel("Wolfram Classification\n (0=I/II, 1=IV, 2=III)")
        plt.yticks([0, 1, 2], ['I / II (0)', 'IV (1)', 'III (2)'])
        plt.grid(True, linestyle='--', alpha=0.4)
        
        if len(experiments) <= 15:
            plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        plt.savefig(f"graph_behavior_vs_{param.replace(' ', '_')}.png")
        plt.show()


plot_assignment_graphs("MasterExperimentGraphs.csv")