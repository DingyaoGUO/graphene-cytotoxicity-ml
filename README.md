# Data-Driven Analysis of Graphene Biocompatibility

This project explores the key physicochemical factors influencing the cytotoxicity of graphene-based materials using a machine learning approach.

By analyzing literature-derived experimental data, the study aims to identify which material properties most strongly affect cell viability and provide insights for the design of biocompatible graphene materials for biomedical applications.

---

## Background

Graphene and its derivatives (including graphene oxide (GO), reduced graphene oxide (rGO), and graphene quantum dots (GQDs)) have attracted significant attention in biomedical applications such as:

- drug delivery
- biosensing
- tissue engineering
- biomedical imaging

However, previous studies have reported **inconsistent cytotoxicity results**. Even graphene materials with similar physical properties may show different biological responses.

Key questions include:

- Which physicochemical properties most strongly influence graphene cytotoxicity?
- How do **size**, **layer number**, and **oxygen functional groups** affect cell viability?
- Can **data-driven analysis** help identify the dominant factors governing biocompatibility?

This project addresses these questions by combining literature data mining with machine learning analysis.

---

## Dataset

A dataset was constructed by extracting cytotoxicity data from approximately **40 peer-reviewed publications** on graphene-based materials.

### Input Features

The following physicochemical parameters were collected:

- **Size (μm)** — lateral dimension of graphene sheets
- **Number of Layers** — thickness of graphene structures
- **C/O Ratio** — carbon-to-oxygen ratio indicating oxidation level

### Target Variable

- **Cell Viability (%)**

When ranges were reported in the literature (e.g., 0.1–0.5 μm), the midpoint value was used as an approximate numerical representation.

---

## Methodology

A **Random Forest regression model** was used to investigate the relationship between graphene material properties and biological responses.

### Workflow

1. Literature data collection and extraction
2. Data cleaning and preprocessing
3. Conversion of range values into mean values
4. Train–test split of dataset
5. Random Forest regression modeling
6. Feature importance analysis

### Tools and Libraries

The analysis was implemented in Python using:

- pandas
- numpy
- scikit-learn
- matplotlib

---

## Results

The Random Forest model achieved the following performance:

**R² ≈ 0.82**

Feature importance analysis suggests the following ranking of influence on cell viability:

1. **Number of layers** — strongest influence
2. **Size**
3. **C/O ratio**

This result suggests that **graphene thickness (layer number)** may play a dominant role in determining cytotoxicity, potentially affecting cellular interactions and aggregation behavior.

---

## Repository Structure

graphene-cytotoxicity-ml/

data/
literature-derived dataset

code/
Python scripts for machine learning analysis

figures/
generated plots and visualizations

poster/
research poster presented at university research event

---

## Example Output

Feature importance visualization produced by the Random Forest model:

- Layers: strongest predictor of cytotoxicity
- Size: moderate influence
- C/O ratio: secondary influence

These results support the hypothesis that **structural thickness of graphene materials strongly affects biological interactions**.

---

## Author

**Dingyao**  
Chemical Engineering Undergraduate  
University of Nottingham Ningbo China

---

## Project Type

Undergraduate Research Project  
Materials Informatics  
Graphene Biocompatibility Analysis

---

## Future Work

Possible extensions of this research include:

- Expanding the dataset with additional literature sources
- Including additional parameters such as **dose**, **exposure time**, and **cell type**
- Comparing different machine learning models
- Applying cross-validation to improve model robustness
- Experimental validation of predicted cytotoxicity trends

---

## License

This project is released under the **MIT License**.
