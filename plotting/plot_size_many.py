import matplotlib.pyplot as plt

# Data
x = [13, 33, 70]
labels = ["llama-2-chat-13b", "wizardlm-33b-v1.0-uncensored", "platypus2-70b-instruct"]
strictly_correct = [0.125, 0.3, 0.525]
correct_allowing_nonatomic = [0.275, 0.475, 0.75]
correct_allowing_nonatomic_and_skips = [0.35, 0.475, 0.775]
incorrect_proofs_useless_branch = [0.61538, 0.7142, 0.6666]

y_values_list = [strictly_correct, correct_allowing_nonatomic]
titles = ["Strictly Correct", "Correct Allowing Skipped Steps"]

fig, axs = plt.subplots(1, len(y_values_list), figsize=(15, 5))  # 1 row, multiple columns

for ax, y_values, title in zip(axs, y_values_list, titles):
    ax.plot(x, y_values, '-o')
    ax.grid()
    ax.set_title(title)
    ax.set_xlabel('Model Parameters (B)')
    ax.set_ylim(0, 1)  # To ensure consistent y-axis scaling
    for i, label in enumerate(labels):
        ax.annotate(label, (x[i], y_values[i] + 0.01), fontsize=8, ha='center')

# Set a common ylabel for all subplots
axs[0].set_ylabel('Proportion')
fig.suptitle('3-hop: Proof Correctness Across Model Sizes')

# Display the plots side by side
plt.tight_layout()
plt.show()
