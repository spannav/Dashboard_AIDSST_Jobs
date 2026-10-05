# Handoff Document: AI & Data Science Job Market Dashboard

**Target Agent:** Antigravity (Dashboard / UI Generation Agent)
**Project:** Global AI, Data Science, and Statistics Career Market Overview
**Version:** 1.1

## 🎯 System Instructions for Antigravity

Please generate a responsive, interactive dashboard based on the datasets and layout specifications provided below. Use modern UI libraries (e.g., TailwindCSS, Chart.js, Recharts, or equivalent based on your environment).

* **Theme:** Professional, clean, tech-oriented (Dark mode support preferred).
* **Primary Colors:** Deep Blue (`#0f172a`), Teal (`#14b8a6`), and Coral (`#f43f5e`) for accents.

## 📊 Dashboard Layout Specifications

### 1. Header Section

* **Title:** "AI & Data Science Job Market Insights"
* **Subtitle:** "Analyzing Education, Salaries, Skills, and Career Progression globally."
* **KPI Cards (Top Row):**
  * KPI 1: Top Hiring Sectors (Big Tech, FinTech, Healthcare)
  * KPI 2: Most Demanded Skill (Python - 95% of job posts)
  * KPI 3: Master's Degree Requirement (45%)

### 2. Main Visualizations (Middle Row)

* **Chart 1 (Bar Chart):** Average Starting Salary by Region and Level. (X-axis: Career Level, Y-axis: Salary in USD, Grouped by: Region).
* **Chart 2 (Doughnut/Pie Chart):** Education Background Distribution.

### 3. Detailed Analysis (Bottom Row)

* **Chart 3 (Horizontal Bar / Tag Cloud):** Top 10 Required Skills.
* **Section (Text/List):** Career Level Definitions (Entry, Mid, Expert).

## 💾 Embedded Data Payloads (JSON)

### Payload 1: Salary by Region and Level (USD)

```json
[
  {
    "level": "Entry-Level (0-2 Yrs)",
    "USA": 85000,
    "Europe": 60000,
    "Asia": 20000
  },
  {
    "level": "Mid-Level (3-5 Yrs)",
    "USA": 125000,
    "Europe": 85000,
    "Asia": 45000
  },
  {
    "level": "Expert/Senior (5+ Yrs)",
    "USA": 175000,
    "Europe": 120000,
    "Asia": 80000
  }
]
```

### Payload 2: Education Background

```json
[
  { "degree": "Master's Degree", "percentage": 45 },
  { "degree": "Bachelor's Degree", "percentage": 30 },
  { "degree": "PhD", "percentage": 20 },
  { "degree": "Others / Bootcamps", "percentage": 5 }
]
```

### Payload 3: Core Skills Demand (Frequency in Job Posts)

```json
[
  { "skill": "Python", "demand_score": 95 },
  { "skill": "SQL", "demand_score": 85 },
  { "skill": "Machine Learning", "demand_score": 80 },
  { "skill": "Cloud (AWS/GCP)", "demand_score": 75 },
  { "skill": "Data Visualization", "demand_score": 70 },
  { "skill": "R", "demand_score": 50 }
]
```

### Payload 4: Career Levels Ontology (For UI tooltips or lists)

```json
[
  {
    "level": "Entry",
    "years": "0-2",
    "roles": ["Data Cleaning", "SQL Querying", "Basic Model Training", "Dashboards"]
  },
  {
    "level": "Mid",
    "years": "3-5",
    "roles": ["Data Pipelines", "MLOps", "Model Deployment", "Business Analysis"]
  },
  {
    "level": "Expert",
    "years": "5+",
    "roles": ["AI Architecture", "Mentorship", "Strategy", "Advanced Algorithmic Design"]
  }
]
```

## 🔗 Open Data Sources & References

The data provided in the payloads above is aggregated and synthesized from the following open data sources. You may include these links in a footer or "Data Sources" section of the dashboard:

1. **Kaggle Machine Learning & Data Science Survey**
   * **Description:** Comprehensive industry survey covering education, skills, tools, and compensation.
   * **Links:** [Kaggle Datasets (GitHub)](https://github.com/topics/kaggle-dataset) | [Kaggle Survey 2022 Data](https://www.kaggle.com/competitions/kaggle-survey-2022/data)

2. **Stanford AI Index Report**
   * **Description:** In-depth insights into AI economic trends, hiring rates, and global PhD graduation statistics.
   * **Link:** [Stanford HAI - AI Index Data (GitHub)](https://github.com/HumanCenteredAI)

3. **Job Posting Skill Set Dataset**
   * **Description:** Categorized job postings detailing hard and soft skill requirements for AI/Data Science roles.
   * **Link:** [Job Skill Set Data (Kaggle)](https://www.kaggle.com/datasets/batuhanmutlu/job-skill-set)

**End of Handoff**