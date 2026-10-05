# AI & Data Science Supply vs Demand Dashboard

An interactive dashboard built to analyze the global AI, Data Science, and Statistics career market. The application provides insights by comparing the "Supply" (academic programs and graduates) with the "Demand" (market job requirements, vacancies, and salaries) and visualizes the resulting skill mismatches.

## Features
- **Interactive UI**: Clean, professional, and tech-oriented layout.
- **Cross-Filtering**: Charts within the same tab are linked, allowing users to drill down into specific educational programs or job titles.
- **Three Core Analysis Tabs**:
  1. **Supply Side**: Analyzes graduate volumes, mandatory core subjects, post-graduation employment timelines, and tuition fees.
  2. **Demand Side**: Details open positions, required skills, hiring companies, and salary by experience level.
  3. **Skill Mismatch**: Identifies gaps between what is taught and what the market demands, helping shape curriculum development.

## Tech Stack
- **Backend/Frontend UI**: Python, Plotly Dash (`dash`, `dash-bootstrap-components`)
- **Data Processing**: Pandas

## Getting Started

1. Install the required dependencies:
   ```bash
   pip install dash dash-bootstrap-components pandas plotly
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to the address shown in your console (usually `http://127.0.0.1:8050/`).
