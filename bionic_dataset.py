import pandas as pd
import numpy as np

# Create a list of potential vulnerabilities
vulnerabilities = ['Weak Password Policy', 'Software Vulnerabilities', 'Communication Vulnerabilities', 'Hardware Vulnerabilities']

# Create a dictionary with the bionic chip data
bionic_chip_data = {
    'Sl. No': [],
    'Body Part': [],
    'Type of Bionic Chip': [],
    'Average Cost (INR)': [],
    'Country of Origin': [],
    'Vulnerability Identified': [],
    'Impact Score': []
}

# Generate 2000 sample entries
for i in range(2000):
    # Choose a random body part and type of bionic chip
    body_parts = ['Brain', 'Ear', 'Eye', 'Limbs (Arm/Leg)', 'Heart', 'Pancreas', 'Arm', 'Hand', 'Leg', 'Spine', 'Bladder', 'Cochlea', 'Knee', 'Hip', 'Shoulder', 'Ankle', 'Foot']
    chip_types = ['Neuroprosthetic Chips', 'Cochlear Implant Chips', 'Retinal Implant Chips', 'Myoelectric Control Chips', 'Cardiac Implant Chips', 'Artificial Pancreas Control Chips', 'Modular Prosthetic Limb Control System', 'i-Limb Ultra Prosthetic Hand Control System', 'POWER KNEE by Össur', 'Neurostimulator Implants for Chronic Pain', 'Artificial Urinary Sphincter Control System', 'Advanced Bionics HiRes Ultra Cochlear Implant', 'GENUTECH Genutrain OA Prosthetic Knee Implant', 'DePuy Synthes ATTUNE® Primary Total Hip System', 'Zimmer Biomet Comprehensive Reverse Shoulder System', 'Integra LifeSciences Cadence Total Ankle System', 'Össur Proprio Foot Prosthetic Foot']
    country_of_origin = ['USA', 'Switzerland', 'Germany', 'USA', 'USA', 'USA', 'USA', 'UK', 'Iceland', 'USA', 'USA', 'USA', 'Germany', 'USA', 'USA', 'USA', 'Iceland', 'China']
    
    body_part_type = np.random.choice(body_parts) + ", " + np.random.choice(chip_types) + ", " + np.random.choice(country_of_origin)
    
    # Choose a random cost
    if body_part_type.endswith('China'):
        cost = np.random.randint(50000, 300000)
    else:
        cost = np.random.randint(800000, 7000000)
        
    # If Chinese manufacturer is selected, make it more vulnerable
    if body_part_type.endswith('China'):
        vuln = np.random.choice([0, 1], p=[0.4, 0.6])
        if vuln:
            vulnerability = np.random.choice(vulnerabilities)
            impact_score = np.random.randint(7, 10)
        else:
            vulnerability = ''
            impact_score = ''
    else:
        vuln = np.random.choice([0, 1], p=[0.85, 0.15])
        if vuln:
            vulnerability = np.random.choice(vulnerabilities)
            impact_score = np.random.randint(1, 10)
        else:
            vulnerability = ''
            impact_score = ''
        
    # Append the data to the bionic chip dictionary
    bionic_chip_data['Sl. No'].append(i + 1)
    bionic_chip_data['Body Part'].append(body_part_type.split(", ")[0])
    bionic_chip_data['Type of Bionic Chip'].append(body_part_type.split(", ")[1])
    bionic_chip_data['Average Cost (INR)'].append(cost)
    bionic_chip_data['Country of Origin'].append(body_part_type.split(", ")[2])
    bionic_chip_data['Vulnerability Identified'].append(vulnerability)
    bionic_chip_data['Impact Score'].append(impact_score)
    
# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(bionic_chip_data)

# Export the data to a CSV file
df.to_csv('bionic_chips_data.csv', index=False)

# Print a message confirming export
print("Data exported to CSV file successfully!")

