# Analysis of Weekly Influenza (Type A and B) Cases in the US (2023-24)

## Overview
This project analyzes the weekly data on Influenza Type A and Type B cases in the US for the period 2023-24. Using rolling mean and standard deviation, it aims to reveal trends, patterns, and variability to understand the seasonal behavior and potential outbreaks of influenza.

## Introduction
Influenza, commonly known as the flu, is a contagious respiratory illness caused by viruses that infect the nose, throat, and sometimes the lungs. There are four types of the influenza virus:
- **Influenza A** viruses cause seasonal flu epidemics nearly every year in the United States and can infect both humans and animals. It is the only type that can cause a pandemic, as seen in bird flu and swine flu pandemics.
- **Influenza B** viruses also lead to seasonal epidemics, typically affecting only humans. Compared to Influenza A, Influenza B viruses mutate more slowly.
- **Influenza C** viruses cause mild illnesses and do not seem to cause epidemics.
- **Influenza D** viruses mainly affect cattle and do not infect humans.
  
Monitoring and analyzing influenza case data is essential for public health as it helps identify seasonal trends, track potential outbreaks, and guide effective intervention strategies.

## Data Source
The dataset used in this project is titled **“Influenza Positive Tests Reported to CDC by Clinical Laboratories, National Summary, 2023-24 Season”**, covering the period up to the week ending June 29, 2024. This is sourced from the [CDC Flu Weekly Reports](https://www.cdc.gov/flu/weekly/index.htm).

For this project, the dataset was processed to focus on the number of positive cases for Influenza Type A and Type B each week.

## Tools and Libraries
**Programming Language:** Python
- Pandas: Utilized for data manipulation and preparation.
- Matplotlib: Employed for creating visualizations - line plots and rolling mean/standard deviation plots.

## Program Code
The program was written in PyCharm. You can access the [Program](Program) file here on GitHub or run the code on Google Colab by clicking on the colab badge below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ngtyjvaxjVPGCdPp1-BmUKRg6b4Lrhzp)
## Program Output
**1. LINE PLOT**
![Line Plot](https://github.com/user-attachments/assets/f7e16ca2-4a9d-48cc-a84a-99b379533118)

**2. ROLLING MEAN-STD PLOT**
![Rolling Mean-Std](https://github.com/user-attachments/assets/f4cd599f-38e7-4596-8d84-6756e2edf75b)

## Methodology
A line plot is created to represent the weekly reported cases of Influenza Type A and Type B in the US from 2023 to 2024. This plot serves as the foundational visualization, allowing for the observation of both short-term variations and long-term trends.

Following the line plot, we apply rolling statistical techniques to further analyze the data. The rolling mean is computed to smooth out short-term fluctuations and to highlight underlying trends in the case counts. By using a rolling window, the mean provides a clearer view of the general trend in influenza cases over time.

The rolling standard deviation is calculated to measure the variability of the influenza case counts. This statistic helps to identify periods of increased fluctuation and potential outliers, providing insights into the stability of the case counts and the presence of significant deviations from the trend.

## Observation
For the purpose of this analysis, we will focus exclusively on Graph 2 to have a more detailed understanding of the trends and variability over time.

### Graph 2: Rolling Mean and Standard Deviation

- **Influenza Type A:**
  - The rolling mean and standard deviation indicate a clear peak around Week 50, with a higher level of variability around the peak.
  - Variability decreases significantly after the peak, indicating a more consistent decline.
  - Influenza Type A cases peak earlier (Week 50) and are more numerous compared to Type B.
    
- **Influenza Type B:**
  - The rolling mean shows a gradual increase until the peak around Week 4, with variability increasing towards the peak.
  - After the peak, the number of cases declines steadily, with less variability compared to the rising phase.
  - Influenza Type B cases peak later (Week 4) and have fewer cases overall.

## Inference
- Influenza Type A spreads more rapidly and affects more individuals compared to Type B, possibly due to differences in virulence or transmissibility.
- Influenza Type B, although less virulent, has a longer duration of spread.

## Conclusion
- The data suggests the need for early interventions for Type A to mitigate its rapid spread.
- For Type B, prolonged surveillance and continuous intervention may be necessary due to its extended spread period.

### Implications for Health Care Professionals
Health care professionals can use this data to predict and prepare for peak influenza seasons.

- **Intervention:**
  - Vaccination campaigns should start before Week 40 to ensure immunity before the peak periods.
  - Public health advisories should be issued earlier for Type A, considering its rapid rise.
    
- **Resource Allocation:**
  - Hospitals and clinics should prepare for higher patient volumes around Week 50 for Type A and Week 4 for Type B.
  - Stockpiling antivirals and other necessary medical supplies ahead of the peak periods can help manage the surge in cases.

## Author
Pragya Ghosh
