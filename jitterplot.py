import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
threads = ['Thread 0', 'Thread 1', 'Thread 2', 'Thread 3']
average_latency = [37, 32, 38, 31]  # Average latencies from provided data
jitter = [273, 166, 157, 191]  # Calculated jitter for each thread

x = np.arange(len(threads))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars for jitter and average latency
bars1 = ax.bar(x - width/2, jitter, width, label='Jitter (us)', color='b')
bars2 = ax.bar(x + width/2, average_latency, width, label='Average Latency (us)', color='g')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Threads', fontsize=14, weight='bold')
ax.set_ylabel('Latency (microseconds)', fontsize=14, weight='bold')
ax.set_title('Jitter and Average Latency for Each Thread (Stress, 20 min)', fontsize=16, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(threads, fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Annotate bars
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text above bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

annotate_bars(bars1)
annotate_bars(bars2)

fig.tight_layout()
plt.savefig('C:/Users/preca/OneDrive - Singapore Institute Of Technology/Desktop/osgraph/jitter_average_latency_stress.png')
plt.show()
