import matplotlib.pyplot as plt

# Data for 2023-2024
data = {
    'Country': ['India', 'USA', 'China', 'Germany', 'Japan', 'Canada'],
    'Renewable (%)': [24, 21, 44, 60, 22.7, 70],
    'Non-Renewable (%)': [76, 79, 56, 40, 77.3, 30]
}

# Create pie charts
plt.figure(figsize=(18, 12))
plt.suptitle('Renewable vs Non-Renewable Energy Mix (2023-2024)', fontsize=16, y=1.02)

colors = ['#4CAF50', '#F44336']  

for i, country in enumerate(data['Country']):
    plt.subplot(2, 3, i+1)
    
    sizes = [data['Renewable (%)'][i], data['Non-Renewable (%)'][i]]
    labels = [f'Renewable\n{data["Renewable (%)"][i]}%', 
              f'Non-Renewable\n{data["Non-Renewable (%)"][i]}%']
    
    # Explode the renewable portion slightly
    explode = (0.05, 0)
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            startangle=90, explode=explode, shadow=True)
    plt.title(country, pad=20)

plt.tight_layout()
plt.show()