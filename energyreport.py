import matplotlib.pyplot as plt
import numpy as np


data = {
    'Country': ['India', 'USA', 'China', 'Germany', 'Japan', 'Canada'],
    'Renewable (%)': [24, 21, 44, 60, 22.7, 70],
    'Non-Renewable (%)': [76, 79, 56, 40, 77.3, 30]
}

colors = ['#4CAF50', '#F44336'] 

# Create the figure
fig = plt.figure(figsize=(18, 16))
fig.suptitle('Renewable vs Non-Renewable Energy Mix (2023-2024)', fontsize=20, y=0.94)

# Pie Charts (2 rows, 3 columns)
for i, country in enumerate(data['Country']):
    ax = fig.add_subplot(3, 3, i+1)
    sizes = [data['Renewable (%)'][i], data['Non-Renewable (%)'][i]]
    labels = [f'Renewable\n{sizes[0]}%', f'Non-Renewable\n{sizes[1]}%']
    explode = (0.05, 0)
    
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
           startangle=90, explode=explode, shadow=True)
    ax.set_title(country, pad=20)

# Bar Graph (bottom full row)
ax_bar = fig.add_subplot(3, 1, 3)
x = np.arange(len(data['Country']))
bar_width = 0.35

ax_bar.bar(x - bar_width/2, data['Renewable (%)'], width=bar_width, label='Renewable (%)', color=colors[0])
ax_bar.bar(x + bar_width/2, data['Non-Renewable (%)'], width=bar_width, label='Non-Renewable (%)', color=colors[1])

ax_bar.set_xlabel('Country')
ax_bar.set_ylabel('Percentage (%)')
ax_bar.set_title('Bar Graph: Renewable vs Non-Renewable Energy by Country')
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(data['Country'])
ax_bar.legend()
ax_bar.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
