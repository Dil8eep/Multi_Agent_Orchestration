import matplotlib.pyplot as plt
import numpy as np

# Sample performance metrics for the Multi-Agent System
agents = ['Summary Agent', 'Action Extraction Agent', 'Risk Analysis Agent']
accuracy = [0.85, 0.78, 0.82]  # Sample accuracy scores
processing_time = [5.2, 4.8, 6.1]  # Sample processing times in seconds

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Accuracy bar chart
ax1.bar(agents, accuracy, color=['blue', 'green', 'red'])
ax1.set_title('Agent Accuracy')
ax1.set_ylabel('Accuracy')
ax1.set_ylim(0, 1)
for i, v in enumerate(accuracy):
    ax1.text(i, v + 0.01, f'{v:.2f}', ha='center', va='bottom')

# Processing time bar chart
ax2.bar(agents, processing_time, color=['cyan', 'magenta', 'yellow'])
ax2.set_title('Processing Time per Agent')
ax2.set_ylabel('Time (seconds)')
for i, v in enumerate(processing_time):
    ax2.text(i, v + 0.1, f'{v:.1f}s', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('performance_metrics.png', dpi=300, bbox_inches='tight')
plt.show()
