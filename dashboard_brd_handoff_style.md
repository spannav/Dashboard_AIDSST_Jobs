# Business Requirements Document (BRD) & Handoff

**Project:** AI & Data Science Supply vs Demand Dashboard
**Target Agent:** Antigravity (Python/Plotly Dashboard Developer)
**Version:** 2.0 (Updated with UI/UX Style Requirements)

## 1. Project Overview

**Objective:** พัฒนา Interactive Dashboard เพื่อเปรียบเทียบข้อมูล "ฝั่งการผลิตบุคลากร (Supply)" และ "ฝั่งความต้องการของตลาดงาน (Demand)" ในสายงาน AI, Data Science และ Statistics พร้อมวิเคราะห์ช่องว่างของทักษะ (Skill Mismatch)
**Tech Stack:**
* **Backend:** Python
* **Frontend/Dashboard:** Plotly Dash (`dash`, `dash-bootstrap-components` สำหรับ Layout)
* **Data Processing:** Pandas

## 2. Core Functional Requirements

* **Tab System:** Dashboard ต้องแบ่งออกเป็น 3 Tabs หลัก
* **Interactivity (Cross-filtering):** ภายใน Tab เดียวกัน กราฟทุกตัวจะต้องเชื่อมโยงกัน (Linked/Cross-filtered) หากผู้ใช้คลิกเลือกข้อมูลในกราฟหนึ่ง กราฟอื่นๆ ใน Tab เดียวกันจะต้องอัปเดตเพื่อแสดงเฉพาะข้อมูลที่เกี่ยวข้อง

## 3. Dashboard Architecture & UI Layout

### TAB 1: ปริมาณคนที่จบ และ Skill ที่เรียนมา (Supply Side)
* **Chart 1.1: ปริมาณการผลิตบัณฑิต** (Stacked Bar Chart / Line Chart)
* **Chart 1.2: รายวิชาบังคับที่ตรงสาย** (Horizontal Bar Chart)
* **Chart 1.3: อัตราการได้งานทำหลังเรียนจบ** (Grouped Bar Chart)
* **Chart 1.4: ค่าเทอม** (Scatter Plot / Box Plot)

### TAB 2: ปริมาณงานที่จ้าง และ Skill ที่ต้องการ (Demand Side)
* **Chart 2.1: ตำแหน่งงานที่เปิดรับ** (Bar Chart)
* **Chart 2.2: ทักษะที่ต้องการ** (Treemap / Horizontal Bar Chart)
* **Chart 2.3: บริษัทที่เปิดรับ** (Bubble Chart / Donut Chart)
* **Chart 2.4: เงินเดือนตามระดับประสบการณ์** (Box Plot / Grouped Bar Chart)

### TAB 3: วิเคราะห์ช่องว่างทางทักษะ (Skill Mismatch Analysis)
* **Chart 3.1: Skill Gap & Overlap** (Radar Chart)
* **Chart 3.2: Shortage vs Surplus Matrix** (Scatter Plot 4 Quadrants)

---

## 4. 🎨 UI/UX Style Requirements (Reference: `image_d14607.png`)

**To the Antigravity Agent:** 
The user has requested a complete stylistic overhaul of the dashboard to match the aesthetic of the provided reference image (`image_d14607.png`). The target style is a **"Futuristic / Sci-Fi Dark Mode"** with subtle glassmorphism and neon accents. 

Please implement the following CSS and Plotly layout configurations:

### 4.1 Global Color Palette
* **Main Background:** Deep Navy/Space Blue (`#0B1021` to `#101835` radial or linear gradient).
* **Card/Panel Background:** Semi-transparent dark blue (`rgba(16, 24, 53, 0.6)`) to create a subtle glass effect against the main background.
* **Text Primary (Values/Titles):** Pure White (`#FFFFFF`).
* **Text Secondary (Labels/Subtitles):** Light Slate/Cyan-grey (`#8DA3C7` or `#94A3B8`).
* **Accent Color 1 (Cyan):** `#00F0FF` (Used for active states, primary data lines, small icons).
* **Accent Color 2 (Purple/Magenta):** `#B537F2` (Used as a gradient pair with Cyan for buttons, progress bars, and donut charts).

### 4.2 Component Styling (CSS / Dash Bootstrap)
* **Cards/Containers:** 
  * Apply `border-radius: 12px` or `16px`.
  * Add a subtle, thin border: `1px solid rgba(255, 255, 255, 0.05)`.
  * Use a soft drop shadow: `box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3)`.
* **Sidebar / Navigation:**
  * Left-aligned with the same card styling.
  * Active Tab/Menu Item should have a rounded pill background (semi-transparent cyan) and an accent dot or line.
* **Buttons:**
  * Must feature a vibrant gradient background (Cyan to Purple/Magenta).
  * Rounded pill shape (`border-radius: 50px`).
  * Glow effect on hover (`box-shadow: 0 0 10px rgba(181, 55, 242, 0.5)`).
* **Typography:** 
  * Use a modern, clean sans-serif font (e.g., `'Inter', 'Roboto', 'Segoe UI', sans-serif`).
  * KPI values must be large and bold.

### 4.3 Plotly Graph Styling Constraints
All Plotly figures (`fig.update_layout()`) **MUST** follow these rules to blend seamlessly into the UI:
1. **Transparent Backgrounds:** 
   * `plot_bgcolor='rgba(0,0,0,0)'`
   * `paper_bgcolor='rgba(0,0,0,0)'`
2. **Gridlines:**
   * Remove vertical gridlines entirely.
   * Horizontal gridlines must be very faint: `gridcolor='rgba(255,255,255,0.05)'` or `#1E293B`.
3. **Fonts:**
   * Set global font color to the secondary text color (`#8DA3C7`).
4. **Data Colors (Traces):**
   * Use the Cyan (`#00F0FF`) to Purple (`#B537F2`) gradient colorway for charts.
   * For Line charts: Add a smooth line shape (`shape='spline'`) with markers enabled. Add a subtle area fill below the line with low opacity.
   * For Donut charts: Make the ring thick (`hole=0.75`), hide legends if taking up too much space, and put the total value in the center annotation.

## 5. Implementation Instructions for Antigravity
1. Create an `assets/style.css` file containing the classes for the dark theme, neon buttons, and glassmorphism cards.
2. Structure the Dash layout using `dbc.Row` and `dbc.Col`, applying the custom CSS classes to `dbc.Card`.
3. Apply a custom Plotly template or use `update_layout` aggressively on every generated chart to ensure no default white backgrounds or bright axes lines remain.