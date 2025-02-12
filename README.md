# Microbiome-Seasons-Dirichlet
A simplified simulation of microbial community dynamics across seasonal changes

🌱 Seasonal Microbial Dynamics using Dirichlet Distribution

📖 Overview

This repository contains a simplified simulation of microbial community dynamics across seasonal changes. The model tracks three microbial species as they undergo:
✔ Horizontal Mixing – Microbes transfer between environments.

✔ Microbial Growth – Population grows following a logistic model.

✔ Seasonal Selection – Different seasons favor different microbes based on fitness.

The simulation uses a Dirichlet distribution to model microbial proportions, ensuring valid probability distributions across time.

📌 Features

✅ Seasonal Microbial Simulation – Tracks microbial composition across Spring, Summer, Fall, and Winter.

✅ Probabilistic Modeling – Uses a Dirichlet distribution to maintain proportional microbial abundances.

✅ Seasonal Fitness Impact – Microbial selection varies based on seasonal conditions.

✅ Dynamic Bar Plots – Generates yearly visualizations of microbial changes.

📊 How It Works

1️⃣ Microbial populations start with random proportions (using a Dirichlet distribution).

2️⃣ Each year consists of four seasons: Spring, Summer, Fall, and Winter.

3️⃣ At each time step (year), microbes:

 •	Mix horizontally (redistribution across environment).

 •	Grow according to a logistic function.

 •	Experience selection based on seasonal fitness conditions.

4️⃣ The process repeats for 10 years, visualizing microbial evolution.

🔬 Scientific Relevance

✔ Microbial Ecology – Models seasonal microbial adaptation in different environments.

✔ Probabilistic Simulations – Uses Dirichlet distributions to ensure realistic community compositions.

✔ Environmental Science – Helps study how microbial populations respond to seasonal shifts.

🛠 Future Improvements

🔹 Add additional environmental factors (e.g., pH, temperature shifts).

🔹 Introduce external disturbances (e.g., antibiotics, nutrient spikes).

🔹 Extend to real-world metagenomic datasets for comparison.

📜 License

This project is open-source under the MIT License. Feel free to use and modify!
