import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. REALISTIC / HANDOFF DATA
# ==========================================

# Colors from Handoff
COLOR_CYAN = "#00F0FF"
COLOR_MAGENTA = "#B537F2"
COLOR_TEXT_SEC = "#8DA3C7"
COLOR_GRID = "rgba(255,255,255,0.05)"

# Palette for charts
SCI_FI_PALETTE = [COLOR_CYAN, COLOR_MAGENTA, "#38bdf8", "#818cf8"]

# Payload 1: Salary by Region and Level (USD)
salary_data = [
  { "Level": "Entry-Level (0-2 Yrs)", "USA": 85000, "Europe": 60000, "Asia": 20000, "Job Title": "Data Scientist" },
  { "Level": "Mid-Level (3-5 Yrs)", "USA": 125000, "Europe": 85000, "Asia": 45000, "Job Title": "Data Scientist" },
  { "Level": "Expert/Senior (5+ Yrs)", "USA": 175000, "Europe": 120000, "Asia": 80000, "Job Title": "Data Scientist" },
  { "Level": "Entry-Level (0-2 Yrs)", "USA": 90000, "Europe": 65000, "Asia": 25000, "Job Title": "AI Engineer" },
  { "Level": "Mid-Level (3-5 Yrs)", "USA": 135000, "Europe": 90000, "Asia": 50000, "Job Title": "AI Engineer" },
  { "Level": "Expert/Senior (5+ Yrs)", "USA": 185000, "Europe": 130000, "Asia": 90000, "Job Title": "AI Engineer" },
  { "Level": "Entry-Level (0-2 Yrs)", "USA": 70000, "Europe": 50000, "Asia": 15000, "Job Title": "Data Analyst" },
  { "Level": "Mid-Level (3-5 Yrs)", "USA": 95000, "Europe": 70000, "Asia": 30000, "Job Title": "Data Analyst" },
  { "Level": "Expert/Senior (5+ Yrs)", "USA": 125000, "Europe": 90000, "Asia": 55000, "Job Title": "Data Analyst" },
  { "Level": "Entry-Level (0-2 Yrs)", "USA": 95000, "Europe": 75000, "Asia": 30000, "Job Title": "Machine Learning Engineer" },
  { "Level": "Mid-Level (3-5 Yrs)", "USA": 140000, "Europe": 100000, "Asia": 60000, "Job Title": "Machine Learning Engineer" },
  { "Level": "Expert/Senior (5+ Yrs)", "USA": 190000, "Europe": 140000, "Asia": 100000, "Job Title": "Machine Learning Engineer" },
  { "Level": "Entry-Level (0-2 Yrs)", "USA": 65000, "Europe": 45000, "Asia": 15000, "Job Title": "Statistician" },
  { "Level": "Mid-Level (3-5 Yrs)", "USA": 85000, "Europe": 65000, "Asia": 25000, "Job Title": "Statistician" },
  { "Level": "Expert/Senior (5+ Yrs)", "USA": 110000, "Europe": 85000, "Asia": 45000, "Job Title": "Statistician" },
]
df_salary_wide = pd.DataFrame(salary_data)
demand_salary = df_salary_wide.melt(id_vars=["Level", "Job Title"], var_name="Region", value_name="Salary_USD")

# Payload 2: Education Background (By Program)
edu_bg_data = [
  { "degree": "Master's Degree", "percentage": 45 },
  { "degree": "Bachelor's Degree", "percentage": 30 },
  { "degree": "PhD", "percentage": 20 },
  { "degree": "Others / Bootcamps", "percentage": 5 }
]
df_edu_bg = pd.DataFrame(edu_bg_data)

# Supply Data Generation
years = [2020, 2021, 2022, 2023]
supply_graduates_data = []
for y in years:
    base = 10000 + (y - 2020) * 3500
    supply_graduates_data.extend([
        {'Year': y, 'Program': "Master's Degree", 'Graduates': int(base * 0.45)},
        {'Year': y, 'Program': "Bachelor's Degree", 'Graduates': int(base * 0.30)},
        {'Year': y, 'Program': "PhD", 'Graduates': int(base * 0.20)},
        {'Year': y, 'Program': "Others / Bootcamps", 'Graduates': int(base * 0.05)},
    ])
supply_graduates = pd.DataFrame(supply_graduates_data)

# Payload 3: Core Skills Demand
demand_skills_data = [
  { "skill": "Python", "demand_score": 95, "Job Title": "Data Scientist" },
  { "skill": "Machine Learning", "demand_score": 85, "Job Title": "Data Scientist" },
  { "skill": "Data Visualization", "demand_score": 75, "Job Title": "Data Scientist" },
  { "skill": "Python", "demand_score": 90, "Job Title": "AI Engineer" },
  { "skill": "Deep Learning", "demand_score": 85, "Job Title": "AI Engineer" },
  { "skill": "Cloud (AWS/GCP)", "demand_score": 80, "Job Title": "AI Engineer" },
  { "skill": "SQL", "demand_score": 95, "Job Title": "Data Analyst" },
  { "skill": "Data Visualization", "demand_score": 85, "Job Title": "Data Analyst" },
  { "skill": "Python", "demand_score": 60, "Job Title": "Data Analyst" },
  { "skill": "Python", "demand_score": 95, "Job Title": "Machine Learning Engineer" },
  { "skill": "Machine Learning", "demand_score": 90, "Job Title": "Machine Learning Engineer" },
  { "skill": "Cloud (AWS/GCP)", "demand_score": 85, "Job Title": "Machine Learning Engineer" },
  { "skill": "R", "demand_score": 85, "Job Title": "Statistician" },
  { "skill": "Python", "demand_score": 70, "Job Title": "Statistician" },
  { "skill": "SQL", "demand_score": 60, "Job Title": "Statistician" },
]
demand_skills = pd.DataFrame(demand_skills_data)

demand_skills_global = pd.DataFrame([
  { "skill": "Python", "demand_score": 95 },
  { "skill": "SQL", "demand_score": 85 },
  { "skill": "Machine Learning", "demand_score": 80 },
  { "skill": "Cloud (AWS/GCP)", "demand_score": 75 },
  { "skill": "Data Visualization", "demand_score": 70 },
  { "skill": "R", "demand_score": 50 }
])

# Demand Jobs (Realistic Vacancies)
demand_jobs = pd.DataFrame([
    {'Job Title': 'Data Analyst', 'Vacancies': 15000},
    {'Job Title': 'Data Scientist', 'Vacancies': 12500},
    {'Job Title': 'Machine Learning Engineer', 'Vacancies': 8500},
    {'Job Title': 'AI Engineer', 'Vacancies': 6000},
    {'Job Title': 'Statistician', 'Vacancies': 2500},
])

# Supply Skills
supply_skills_data = [
  { "skill": "Python", "supply_score": 90 }, 
  { "skill": "SQL", "supply_score": 60 }, 
  { "skill": "Machine Learning", "supply_score": 85 }, 
  { "skill": "Cloud (AWS/GCP)", "supply_score": 30 }, 
  { "skill": "Data Visualization", "supply_score": 50 }, 
  { "skill": "R", "supply_score": 80 } 
]
supply_skills = pd.DataFrame(supply_skills_data)

# Mismatch 
mismatch_df = pd.merge(supply_skills, demand_skills_global, on='skill')
mismatch_df['Supply_Norm'] = mismatch_df['supply_score'] / 100
mismatch_df['Demand_Norm'] = mismatch_df['demand_score'] / 100

tuition_data = [
    {'Program': "Master's Degree", 'Tuition_USD': 45000},
    {'Program': "Bachelor's Degree", 'Tuition_USD': 30000},
    {'Program': "PhD", 'Tuition_USD': 15000}, 
    {'Program': "Others / Bootcamps", 'Tuition_USD': 12000},
]
supply_tuition = pd.DataFrame(tuition_data)


def apply_sci_fi_layout(fig):
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLOR_TEXT_SEC, family='Inter, sans-serif'),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor=COLOR_GRID, zeroline=False),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig


# ==========================================
# 2. APP SETUP & LAYOUT
# ==========================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) # Let our CSS handle the dark mode
app.title = "AI & Data Science Job Market Insights"

# Header
header = dbc.Row([
    dbc.Col([
        html.H1("AI & Data Science Job Market Insights", className="text-center mt-4 text-cyan"),
        html.P("Analyzing Education, Salaries, Skills, and Career Progression globally.", className="text-center mb-4 text-muted")
    ])
])

# KPI Cards
kpi_cards = dbc.Row([
    dbc.Col(dbc.Card(dbc.CardBody([
        html.H5("Top Hiring Sectors", className="card-title"),
        html.H3("Big Tech, FinTech", className="text-magenta")
    ]), className="glass-card mb-3"), md=4),
    dbc.Col(dbc.Card(dbc.CardBody([
        html.H5("Most Demanded Skill", className="card-title"),
        html.H3("Python (95%)", className="text-cyan")
    ]), className="glass-card mb-3"), md=4),
    dbc.Col(dbc.Card(dbc.CardBody([
        html.H5("Master's Degree Req.", className="card-title"),
        html.H3("45%", className="text-magenta")
    ]), className="glass-card mb-3"), md=4)
], className="mb-4")

# Footer (References)
footer = dbc.Container([
    html.Hr(style={"borderColor": COLOR_GRID}),
    html.H5("🔗 Open Data Sources & References", className="mt-4 text-cyan"),
    html.Ul([
        html.Li([html.A("Kaggle Survey Data", href="#"), ": Industry survey covering education, skills, tools."]),
        html.Li([html.A("Stanford AI Index", href="#"), ": Insights into AI economic trends, hiring rates."]),
        html.Li([html.A("Job Posting Data", href="#"), ": Categorized job postings detailing requirements."])
    ], className="text-muted"),
], className="mt-5 pb-5")

# Tabs Content
tab1_content = dbc.Card(dbc.CardBody([
    html.H4("Supply Side: Education & Graduates", className="card-title mb-3 text-cyan"),
    html.P("🖱️ Click a Program in the 'Graduates' chart to cross-filter the Tuition and Education charts below.", className="text-muted"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-1-1-graduates', config={'displayModeBar': False}), md=6),
        dbc.Col(dcc.Graph(id='chart-1-2-edu', config={'displayModeBar': False}), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-1-4-tuition', config={'displayModeBar': False}), md=12)
    ])
]), className="glass-card mt-3")

tab2_content = dbc.Card(dbc.CardBody([
    html.H4("Demand Side: Jobs & Requirements", className="card-title mb-3 text-cyan"),
    html.P("🖱️ Click a Job Title in the 'Vacancies' chart to cross-filter Skills and Salary.", className="text-muted"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-2-1-jobs', config={'displayModeBar': False}), md=6),
        dbc.Col(dcc.Graph(id='chart-2-2-skills', config={'displayModeBar': False}), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-2-4-salary', config={'displayModeBar': False}), md=12)
    ])
]), className="glass-card mt-3")

tab3_content = dbc.Card(dbc.CardBody([
    html.H4("Skill Mismatch Analysis", className="card-title mb-3 text-cyan"),
    dbc.Row([
        dbc.Col(dcc.Graph(id='chart-3-1-radar', config={'displayModeBar': False}), md=6),
        dbc.Col(dcc.Graph(id='chart-3-2-scatter', config={'displayModeBar': False}), md=6)
    ])
]), className="glass-card mt-3")

app.layout = dbc.Container([
    header,
    kpi_cards,
    dbc.Tabs([
        dbc.Tab(tab1_content, label="1. Supply (Education)"),
        dbc.Tab(tab2_content, label="2. Demand (Jobs)"),
        dbc.Tab(tab3_content, label="3. Skill Mismatch")
    ], className="nav-tabs"),
    footer
], fluid=True)

# ==========================================
# 3. CALLBACKS
# ==========================================

@app.callback(
    [Output('chart-1-1-graduates', 'figure'),
     Output('chart-1-2-edu', 'figure'),
     Output('chart-1-4-tuition', 'figure')],
    [Input('chart-1-1-graduates', 'clickData')]
)
def update_tab1(clickData):
    selected_program = None
    if clickData:
        selected_program = clickData['points'][0]['x']

    fig_grad = px.line(supply_graduates, x='Year', y='Graduates', color='Program', 
                      title='Graduates per Year by Program (Trend)', 
                      color_discrete_sequence=SCI_FI_PALETTE, markers=True)
    # Area fill
    fig_grad.update_traces(fill='tozeroy', mode='lines+markers', line_shape='spline')
    fig_grad = apply_sci_fi_layout(fig_grad)
    
    df_e = df_edu_bg
    df_t = supply_tuition
    if selected_program:
        df_e = df_edu_bg[df_edu_bg['degree'] == selected_program]
        df_t = supply_tuition[supply_tuition['Program'] == selected_program]

    fig_edu = px.pie(df_e, names='degree', values='percentage', title='Education Background Distribution', 
                     hole=0.75, color_discrete_sequence=SCI_FI_PALETTE)
    fig_edu = apply_sci_fi_layout(fig_edu)
    
    fig_tui = px.bar(df_t, x='Program', y='Tuition_USD', title='Average Tuition Fees (USD)', text_auto=True, 
                     color_discrete_sequence=[COLOR_MAGENTA])
    fig_tui = apply_sci_fi_layout(fig_tui)
    
    return fig_grad, fig_edu, fig_tui

@app.callback(
    [Output('chart-2-1-jobs', 'figure'),
     Output('chart-2-2-skills', 'figure'),
     Output('chart-2-4-salary', 'figure')],
    [Input('chart-2-1-jobs', 'clickData')]
)
def update_tab2(clickData):
    selected_job = None
    if clickData:
        selected_job = clickData['points'][0]['y']

    df_jobs_sorted = demand_jobs.sort_values(by='Vacancies', ascending=True)
    fig_jobs = px.bar(df_jobs_sorted, x='Vacancies', y='Job Title', orientation='h', 
                      title='Open Job Positions', color_discrete_sequence=[COLOR_CYAN])
    fig_jobs = apply_sci_fi_layout(fig_jobs)
    
    df_s = demand_skills
    df_sal = demand_salary
    title_suffix = ""
    
    if selected_job:
        df_s = demand_skills[demand_skills['Job Title'] == selected_job]
        df_sal = demand_salary[demand_salary['Job Title'] == selected_job]
        title_suffix = f" for {selected_job}"
    else:
        df_s = demand_skills_global
        df_sal = df_sal.groupby(['Level', 'Region'])['Salary_USD'].mean().reset_index()
        
    df_s_sorted = df_s.sort_values(by='demand_score', ascending=True)
    fig_skills = px.bar(df_s_sorted, x='demand_score', y='skill', orientation='h', 
                        title=f'Top Required Skills (%){title_suffix}', text_auto=True,
                        color_discrete_sequence=[COLOR_MAGENTA])
    fig_skills = apply_sci_fi_layout(fig_skills)
    
    fig_sal = px.bar(df_sal, x='Level', y='Salary_USD', color='Region', barmode='group', 
                     title=f'Average Starting Salary{title_suffix}',
                     color_discrete_sequence=SCI_FI_PALETTE)
    fig_sal = apply_sci_fi_layout(fig_sal)
    fig_sal.update_layout(xaxis={'categoryorder':'array', 'categoryarray':['Entry-Level (0-2 Yrs)','Mid-Level (3-5 Yrs)','Expert/Senior (5+ Yrs)']})
    
    return fig_jobs, fig_skills, fig_sal

@app.callback(
    [Output('chart-3-1-radar', 'figure'),
     Output('chart-3-2-scatter', 'figure')],
    [Input('chart-3-1-radar', 'id')]
)
def update_tab3(_):
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Supply_Norm'].tolist() + [mismatch_df['Supply_Norm'].tolist()[0]],
        theta=mismatch_df['skill'].tolist() + [mismatch_df['skill'].tolist()[0]],
        fill='toself',
        name='Supply (Taught)',
        line_color=COLOR_CYAN,
        fillcolor='rgba(0, 240, 255, 0.2)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Demand_Norm'].tolist() + [mismatch_df['Demand_Norm'].tolist()[0]],
        theta=mismatch_df['skill'].tolist() + [mismatch_df['skill'].tolist()[0]],
        fill='toself',
        name='Demand (Required)',
        line_color=COLOR_MAGENTA,
        fillcolor='rgba(181, 55, 242, 0.2)'
    ))
    fig_radar = apply_sci_fi_layout(fig_radar)
    fig_radar.update_layout(polar=dict(
        radialaxis=dict(visible=True, range=[0, 1], gridcolor=COLOR_GRID),
        angularaxis=dict(gridcolor=COLOR_GRID, linecolor=COLOR_GRID),
        bgcolor='rgba(0,0,0,0)'
    ), showlegend=True, title="Skill Gap & Overlap")
    
    fig_scatter = px.scatter(
        mismatch_df, x='demand_score', y='supply_score', text='skill', 
        title='Shortage vs Surplus Matrix',
        labels={'demand_score': 'Market Demand (%)', 'supply_score': 'Graduate Supply (%)'}
    )
    fig_scatter.update_traces(textposition='top center', marker=dict(size=14, color=COLOR_CYAN, line=dict(width=2, color=COLOR_MAGENTA)))
    fig_scatter = apply_sci_fi_layout(fig_scatter)
    
    fig_scatter.add_hline(y=50, line_dash="dash", line_color=COLOR_TEXT_SEC)
    fig_scatter.add_vline(x=50, line_dash="dash", line_color=COLOR_TEXT_SEC)
    
    fig_scatter.add_annotation(x=75, y=25, text="High Demand, Low Supply<br>(Shortage)", showarrow=False, opacity=0.8, font=dict(color=COLOR_MAGENTA))
    fig_scatter.add_annotation(x=25, y=75, text="Low Demand, High Supply<br>(Surplus)", showarrow=False, opacity=0.8, font=dict(color=COLOR_CYAN))
    fig_scatter.update_layout(xaxis_range=[0, 100], yaxis_range=[0, 100])
    
    return fig_radar, fig_scatter

if __name__ == '__main__':
    app.run(debug=True, port=8050)
