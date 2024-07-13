import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
conditions = ['Idle', 'Stress']
max_latency_preempt_rt = [77, 310]       # Max under stress
max_latency_xenomai_20min = [33.023, 44.644]
max_latency_xenomai_overnight = [82, 82]  # Assuming same overnight latency for both conditions for illustration

# Width of the bars
width = 0.2

# X locations for the groups
x = np.arange(len(conditions))

fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars
bars1 = ax.bar(x - width, max_latency_preempt_rt, width, label='Max Latency (PREEMPT_RT)', color='b')
bars2 = ax.bar(x, max_latency_xenomai_20min, width, label='Max Latency (Xenomai 3 - 20 min)', color='g')
bars3 = ax.bar(x + width, max_latency_xenomai_overnight, width, label='Max Latency (Xenomai 3 - Overnight)', color='r')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Conditions', fontsize=14, weight='bold')
ax.set_ylabel('Latency (microseconds)', fontsize=14, weight='bold')
ax.set_title('Maximum Latency under Idle and Stress Conditions', fontsize=16, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(conditions, fontsize=12)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Annotate bars
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset text above bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

annotate_bars(bars1)
annotate_bars(bars2)
annotate_bars(bars3)

fig.tight_layout()
plt.savefig('max_latency_comparison.png')
plt.show()
