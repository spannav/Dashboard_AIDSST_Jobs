import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. Generate Synthetic Data
# Supply Data
np.random.seed(42)
programs = ['B.Sc. Data Science', 'M.Sc. AI', 'Ph.D. Statistics', 'B.Sc. Computer Science']
years = [2020, 2021, 2022, 2023]
supply_graduates = pd.DataFrame([
    {'Year': y, 'Program': p, 'Graduates': np.random.randint(50, 300)}
    for y in years for p in programs
])

subjects_data = [
    {'Program': 'B.Sc. Data Science', 'Category': 'Core', 'Subject': 'Machine Learning'},
    {'Program': 'B.Sc. Data Science', 'Category': 'Core', 'Subject': 'Statistics'},
    {'Program': 'M.Sc. AI', 'Category': 'Core', 'Subject': 'Deep Learning'},
    {'Program': 'M.Sc. AI', 'Category': 'Elective', 'Subject': 'NLP'},
    {'Program': 'Ph.D. Statistics', 'Category': 'Core', 'Subject': 'Statistical Modeling'},
    {'Program': 'B.Sc. Computer Science', 'Category': 'Core', 'Subject': 'Data Structures'}
]
supply_subjects = pd.DataFrame(subjects_data)

employment_data = [
    {'Program': p, 'YearAfterGrad': f'Year {y}', 'Employed_Pct': np.random.uniform(60, 95)}
    for p in programs for y in [1, 2, 3]
]
supply_employment = pd.DataFrame(employment_data)

tuition_data = [
    {'Program': p, 'Tuition_USD': np.random.randint(10000, 50000)}
    for p in programs for _ in range(50)  # 50 students per program
]
supply_tuition = pd.DataFrame(tuition_data)

# Demand Data
job_titles = ['Data Scientist', 'AI Engineer', 'Data Analyst', 'Machine Learning Engineer', 'Statistician']
demand_jobs = pd.DataFrame([
    {'Job Title': j, 'Vacancies': np.random.randint(100, 1000)}
    for j in job_titles
])

skills = ['Python', 'SQL', 'Machine Learning', 'AWS', 'NLP', 'Deep Learning', 'Statistics', 'Data Visualization']
demand_skills_data = []
for j in job_titles:
    for s in np.random.choice(skills, size=np.random.randint(3, 6), replace=False):
        demand_skills_data.append({'Job Title': j, 'Skill': s, 'Frequency': np.random.randint(10, 100)})
demand_skills = pd.DataFrame(demand_skills_data)

companies = ['Google', 'Amazon', 'Facebook', 'Local Startup A', 'Bank B', 'HealthCorp']
demand_companies_data = []
for j in job_titles:
    for c in np.random.choice(companies, size=np.random.randint(2, 5), replace=False):
        demand_companies_data.append({'Job Title': j, 'Company': c, 'Vacancies': np.random.randint(5, 50)})
demand_companies = pd.DataFrame(demand_companies_data)

experience_levels = ['Entry-level', 'Mid-level', 'Senior/Expert']
demand_salary_data = []
for j in job_titles:
    for e in experience_levels:
        base_sal = 50000 if e == 'Entry-level' else (90000 if e == 'Mid-level' else 140000)
        demand_salary_data.extend([{'Job Title': j, 'Experience': e, 'Salary': np.random.normal(base_sal, base_sal*0.1)} for _ in range(50)])
demand_salary = pd.DataFrame(demand_salary_data)


# Skill Mismatch Data (Aggregated for Tab 3)
supply_skills_agg = pd.DataFrame({'Skill': skills, 'Supply_Score': np.random.uniform(0.2, 1.0, len(skills))})
demand_skills_agg = demand_skills.groupby('Skill')['Frequency'].sum().reset_index()
demand_skills_agg['Demand_Score'] = demand_skills_agg['Frequency'] / demand_skills_agg['Frequency'].max()

mismatch_df = pd.merge(supply_skills_agg, demand_skills_agg, on='Skill', how='inner')

# 2. App Setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "AI & Data Science Job Market Insights"

# 3. Layout Definitions
header = dbc.Row([
    dbc.Col([
        html.H1("AI & Data Science Job Market Insights", className="text-center mt-4"),
        html.P("Analyzing Education (Supply), Market Demand, and Skill Mismatches globally.", className="text-center text-muted mb-4")
    ])
])

tab1_content = dbc.Card(
    dbc.CardBody([
        html.H4("Supply Side: Education & Graduates", className="card-title"),
        html.P("Click on a program in the Graduates chart to filter the other charts.", className="text-muted"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='chart-1-1-graduates'), md=6),
            dbc.Col(dcc.Graph(id='chart-1-2-subjects'), md=6)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='chart-1-3-employment'), md=6),
            dbc.Col(dcc.Graph(id='chart-1-4-tuition'), md=6)
        ])
    ]),
    className="mt-3"
)

tab2_content = dbc.Card(
    dbc.CardBody([
        html.H4("Demand Side: Jobs & Requirements", className="card-title"),
        html.P("Click on a Job Title in the Vacancies chart to filter the other charts.", className="text-muted"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='chart-2-1-jobs'), md=6),
            dbc.Col(dcc.Graph(id='chart-2-2-skills'), md=6)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='chart-2-3-companies'), md=6),
            dbc.Col(dcc.Graph(id='chart-2-4-salary'), md=6)
        ])
    ]),
    className="mt-3"
)

tab3_content = dbc.Card(
    dbc.CardBody([
        html.H4("Skill Mismatch Analysis", className="card-title"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='chart-3-1-radar'), md=6),
            dbc.Col(dcc.Graph(id='chart-3-2-scatter'), md=6)
        ])
    ]),
    className="mt-3"
)

app.layout = dbc.Container([
    header,
    dbc.Tabs([
        dbc.Tab(tab1_content, label="1. Supply (Education)"),
        dbc.Tab(tab2_content, label="2. Demand (Jobs)"),
        dbc.Tab(tab3_content, label="3. Skill Mismatch")
    ])
], fluid=True)

# 4. Callbacks

# Tab 1 Callbacks
@app.callback(
    [Output('chart-1-1-graduates', 'figure'),
     Output('chart-1-2-subjects', 'figure'),
     Output('chart-1-3-employment', 'figure'),
     Output('chart-1-4-tuition', 'figure')],
    [Input('chart-1-1-graduates', 'clickData')]
)
def update_tab1(clickData):
    selected_program = None
    if clickData:
        selected_program = clickData['points'][0]['x']  # For bar chart where X is Program

    # 1.1 Graduates
    fig_grad = px.bar(supply_graduates, x='Program', y='Graduates', color='Year', barmode='stack', title='Graduates per Year')
    
    # Filter DataFrames based on selection
    df_sub = supply_subjects
    df_emp = supply_employment
    df_tui = supply_tuition
    
    if selected_program:
        df_sub = df_sub[df_sub['Program'] == selected_program]
        df_emp = df_emp[df_emp['Program'] == selected_program]
        df_tui = df_tui[df_tui['Program'] == selected_program]

    # 1.2 Subjects
    if not df_sub.empty:
        fig_sub = px.sunburst(df_sub, path=['Program', 'Category', 'Subject'], title='Core Subjects')
    else:
        fig_sub = px.bar(title="No data available")
        
    # 1.3 Employment
    fig_emp = px.bar(df_emp, x='Program', y='Employed_Pct', color='YearAfterGrad', barmode='group', title='Employment Rate (%)')
    
    # 1.4 Tuition
    fig_tui = px.box(df_tui, x='Program', y='Tuition_USD', title='Tuition Fees (USD)')
    
    return fig_grad, fig_sub, fig_emp, fig_tui

# Tab 2 Callbacks
@app.callback(
    [Output('chart-2-1-jobs', 'figure'),
     Output('chart-2-2-skills', 'figure'),
     Output('chart-2-3-companies', 'figure'),
     Output('chart-2-4-salary', 'figure')],
    [Input('chart-2-1-jobs', 'clickData')]
)
def update_tab2(clickData):
    selected_job = None
    if clickData:
        selected_job = clickData['points'][0]['y']  # For horizontal bar chart

    # 2.1 Jobs
    df_jobs_sorted = demand_jobs.sort_values(by='Vacancies', ascending=True)
    fig_jobs = px.bar(df_jobs_sorted, x='Vacancies', y='Job Title', orientation='h', title='Open Job Positions')
    
    # Filter DataFrames
    df_skills = demand_skills
    df_comps = demand_companies
    df_sal = demand_salary
    
    if selected_job:
        df_skills = df_skills[df_skills['Job Title'] == selected_job]
        df_comps = df_comps[df_comps['Job Title'] == selected_job]
        df_sal = df_sal[df_sal['Job Title'] == selected_job]
        
    # 2.2 Skills
    fig_skills = px.treemap(df_skills, path=[px.Constant('all'), 'Skill'], values='Frequency', title='Required Skills')
    
    # 2.3 Companies
    fig_comps = px.pie(df_comps, names='Company', values='Vacancies', hole=0.4, title='Hiring Companies')
    
    # 2.4 Salary
    fig_sal = px.box(df_sal, x='Experience', y='Salary', color='Experience', title='Salary by Experience Level')
    fig_sal.update_xaxes(categoryorder='array', categoryarray=['Entry-level', 'Mid-level', 'Senior/Expert'])
    
    return fig_jobs, fig_skills, fig_comps, fig_sal

# Tab 3 Callbacks
@app.callback(
    [Output('chart-3-1-radar', 'figure'),
     Output('chart-3-2-scatter', 'figure')],
    [Input('chart-1-1-graduates', 'id')] # Dummy input to trigger on load
)
def update_tab3(_):
    # 3.1 Radar Chart
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Supply_Score'],
        theta=mismatch_df['Skill'],
        fill='toself',
        name='Supply (Education)'
    ))
    fig_radar.add_trace(go.Scatterpolar(
        r=mismatch_df['Demand_Score'],
        theta=mismatch_df['Skill'],
        fill='toself',
        name='Demand (Market)'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        title="Skill Gap & Overlap"
    )
    
    # 3.2 Scatter
    fig_scatter = px.scatter(
        mismatch_df, x='Demand_Score', y='Supply_Score', text='Skill', 
        title='Shortage vs Surplus Matrix',
        labels={'Demand_Score': 'Market Demand (Frequency)', 'Supply_Score': 'Graduate Supply (Score)'}
    )
    fig_scatter.update_traces(textposition='top center')
    fig_scatter.add_hline(y=0.5, line_dash="dash", line_color="gray")
    fig_scatter.add_vline(x=0.5, line_dash="dash", line_color="gray")
    
    # Add quadrant annotations
    fig_scatter.add_annotation(x=0.75, y=0.25, text="High Demand, Low Supply (Shortage)", showarrow=False, opacity=0.5)
    fig_scatter.add_annotation(x=0.25, y=0.75, text="Low Demand, High Supply (Surplus)", showarrow=False, opacity=0.5)
    fig_scatter.update_layout(xaxis_range=[0, 1.2], yaxis_range=[0, 1.2])
    
    return fig_radar, fig_scatter

if __name__ == '__main__':
    app.run(debug=True, port=8050)
