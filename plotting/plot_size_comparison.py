import matplotlib.pyplot as plt

# Points
x = [13, 33, 70]

strictly_correct = [0.125, 0.3, 0.525]
correct_but_nonatomic = [0.275, 0.475, 0.75]
correct_but_nonatomic_and_skips = [0.35, 0.475, 0.775]
incorrect_proofs_useless_branch = [0.61538, 0.7142, 0.6666]

labels = ["llama-2-chat-13b", "wizardlm-33b-v1.0-uncensored", "platypus2-70b-instruct"]

# Plotting the points without the label argument and adding annotations
plt.plot(x, y, '-o')
for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i] + 0.01), fontsize=8, ha='center')

plt.title('3-hop: proportion of proofs that are strictly correct')
plt.xlabel('Model Parameters (B)')
plt.ylabel('Proportion')

# Display the plot without legend
plt.grid(True)
plt.tight_layout()  # Adjust layout for better visualization
plt.show()