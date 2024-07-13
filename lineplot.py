import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the file
file_path = 'C:/Users/preca/OneDrive - Singapore Institute Of Technology/Desktop/osgraph/rt-preempt-cyclictest-10minutes.txt'

# Parse the file and extract histogram data
histogram_data = []

with open(file_path, 'r') as file:
    histogram_section = False
    for line in file:
        if line.startswith('# Histogram'):
            histogram_section = True 
            continue
        if histogram_section:
            if line.startswith('#') or not line.strip():
                break
            histogram_data.append([int(value) for value in line.split()])

# Convert to DataFrame for easier manipulation
df = pd.DataFrame(histogram_data, columns=['Latency', 'Thread0', 'Thread1', 'Thread2', 'Thread3'])

# Plot line plots for each thread with a logarithmic y-axis
plt.figure(figsize=(14, 10))
sns.lineplot(data=df, x='Latency', y='Thread0', label='Thread 0')
sns.lineplot(data=df, x='Latency', y='Thread1', label='Thread 1')
sns.lineplot(data=df, x='Latency', y='Thread2', label='Thread 2')
sns.lineplot(data=df, x='Latency', y='Thread3', label='Thread 3')
plt.title('Latency Line Plot for Each Thread (10-minutes)', fontsize=16)
plt.xlabel('Latency (us)', fontsize=14)
plt.ylabel('Frequency (Count of Occurrences)', fontsize=14)
plt.legend(title='Threads', title_fontsize='13', fontsize='11', loc='upper right')
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0, 60)  # Adjusted x-axis limit to zoom in on the 0-60 microseconds range
plt.ylim(1, 1e7)  # Adjusted y-axis limit based on data range
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Save and show the plot
plt.savefig('C:/Users/preca/OneDrive - Singapore Institute Of Technology/Desktop/osgraph/latency_lineplot_zoomed.png')
plt.show()
