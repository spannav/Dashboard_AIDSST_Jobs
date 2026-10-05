# Business Requirements Document (BRD) & Handoff
**Project:** AI & Data Science Supply vs Demand Dashboard
**Target Agent:** Antigravity (Python/Plotly Dashboard Developer)
**Version:** 1.0

## 1. Project Overview
**Objective:** พัฒนา Interactive Dashboard เพื่อเปรียบเทียบข้อมูล "ฝั่งการผลิตบุคลากร (Supply)" และ "ฝั่งความต้องการของตลาดงาน (Demand)" ในสายงาน AI, Data Science และ Statistics พร้อมวิเคราะห์ช่องว่างของทักษะ (Skill Mismatch)
**Tech Stack:**
*   **Backend:** Python
*   **Frontend/Dashboard:** Plotly Dash (`dash`, `dash-bootstrap-components` สำหรับ Layout)
*   **Data Processing:** Pandas

## 2. Core Functional Requirements
*   **Tab System:** Dashboard ต้องแบ่งออกเป็น 3 Tabs หลัก
*   **Interactivity (Cross-filtering):** ภายใน Tab เดียวกัน กราฟทุกตัวจะต้องเชื่อมโยงกัน (Linked/Cross-filtered) หากผู้ใช้คลิกเลือกข้อมูลในกราฟหนึ่ง (เช่น เลือกหลักสูตร A) กราฟอื่นๆ ใน Tab เดียวกันจะต้องอัปเดตเพื่อแสดงเฉพาะข้อมูลของหลักสูตร A (ใช้ Dash Callbacks: `Input`, `Output`, `State`)

---

## 3. Dashboard Architecture & UI Layout

### TAB 1: ปริมาณคนที่จบ และ Skill ที่เรียนมา (Supply Side)
**Concept:** วิเคราะห์ภาพรวมของสถาบันการศึกษา การผลิตบัณฑิต และหลักสูตรการสอน
*   **Chart 1.1: ปริมาณการผลิตบัณฑิต (Graduates per Year)**
    *   **Type:** Stacked Bar Chart หรือ Line Chart
    *   **X-axis:** ปีการศึกษา (Year)
    *   **Y-axis:** จำนวนบัณฑิต (Number of Graduates)
    *   **Color/Group:** ชื่อหลักสูตร (Program Name เช่น B.Sc. Data Science, M.Sc. AI)
    *   **Action:** เมื่อคลิกที่แท่งกราฟหลักสูตรใด กราฟ 1.2, 1.3, 1.4 จะถูกฟิลเตอร์ตาม
*   **Chart 1.2: รายวิชาบังคับที่ตรงสาย (Mandatory Core Subjects)**
    *   **Type:** Horizontal Bar Chart หรือ Sunburst Chart (แบ่งตามหลักสูตร -> หมวดวิชา -> ชื่อวิชา)
    *   **Data:** รายวิชา (เช่น Machine Learning, Deep Learning, Statistical Modeling)
*   **Chart 1.3: อัตราการได้งานทำหลังเรียนจบ (Employment Timeline)**
    *   **Type:** Grouped Bar Chart
    *   **X-axis:** ชื่อหลักสูตร
    *   **Y-axis:** จำนวนบัณฑิต / อัตราส่วน (%)
    *   **Group:** ปีที่ 1, ปีที่ 2, ปีที่ 3 หลังเรียนจบ (Year 1, Year 2, Year 3)
*   **Chart 1.4: ค่าเทอม (Tuition Fees)**
    *   **Type:** Scatter Plot หรือ Box Plot (เพื่อดูช่วงราคา) หรือ Bar Chart เรียงตามหลักสูตร
    *   **X-axis:** ชื่อหลักสูตร
    *   **Y-axis:** ค่าเทอม (หน่วย: บาท/USD)

### TAB 2: ปริมาณงานที่จ้าง และ Skill ที่ต้องการ (Demand Side)
**Concept:** วิเคราะห์ความต้องการของตลาดแรงงาน ทักษะที่บริษัทมองหา และผลตอบแทน
*   **Chart 2.1: ตำแหน่งงานที่เปิดรับ (Open Job Positions/Vacancies)**
    *   **Type:** Bar Chart (เรียงลำดับจากมากไปน้อย)
    *   **X-axis:** จำนวนตำแหน่งที่ว่าง
    *   **Y-axis:** ชื่อตำแหน่ง (Job Title เช่น Data Scientist, AI Engineer, Data Analyst)
    *   **Action:** เมื่อคลิกที่ตำแหน่งใด กราฟ 2.2, 2.3, 2.4 จะถูกฟิลเตอร์เพื่อแสดงข้อมูลเฉพาะตำแหน่งนั้น
*   **Chart 2.2: ทักษะที่ต้องการ (Required Skills)**
    *   **Type:** Treemap หรือ Horizontal Bar Chart
    *   **Data:** ทักษะที่ดึงมาจาก Job Description (เช่น Python, SQL, AWS, NLP) พร้อม Frequency (จำนวนครั้งที่พบ)
*   **Chart 2.3: บริษัทที่เปิดรับ (Hiring Companies)**
    *   **Type:** Bubble Chart หรือ Donut Chart
    *   **Data:** ชื่อบริษัท (Company Name) ขนาดของ Bubble/Slice ขึ้นอยู่กับจำนวนตำแหน่งที่เปิดรับ
*   **Chart 2.4: เงินเดือนตามระดับประสบการณ์ (Salary by Experience Level)**
    *   **Type:** Box Plot หรือ Grouped Bar Chart
    *   **X-axis:** ระดับการทำงาน (Entry-level, Mid-level, Senior/Expert)
    *   **Y-axis:** ช่วงเงินเดือน (Salary Range)

### TAB 3: วิเคราะห์ช่องว่างทางทักษะ (Skill Mismatch Analysis)
**Concept:** นำข้อมูลทักษะที่สอน (Tab 1) มาชนกับ ทักษะที่ตลาดต้องการ (Tab 2) เพื่อดูว่าสถาบันการศึกษาผลิตคนตรงความต้องการหรือไม่
*   **Chart 3.1: Skill Gap & Overlap (Radar Chart หรือ Diverging Bar Chart)**
    *   **Type:** Radar Chart เปรียบเทียบ 2 เส้น (Supply - ทักษะที่เรียน vs Demand - ทักษะที่ตลาดต้องการ)
    *   **Logic:** แปลงรายวิชาใน Tab 1 เป็น Skill (เช่น วิชา ML = Skill Machine Learning) นำมาเปรียบเทียบสัดส่วน (Normalize) กับ Skill Frequency ใน Tab 2
*   **Chart 3.2: Shortage vs Surplus Matrix (Scatter Plot)**
    *   **Type:** Scatter Plot แบ่งเป็น 4 Quadrants
    *   **X-axis:** ความถี่ของทักษะที่ตลาดต้องการ (Market Demand)
    *   **Y-axis:** ความถี่ของทักษะที่บัณฑิตมี/ได้เรียน (Graduate Supply)
    *   **Insight:** ทักษะที่ตกในฝั่งขวาล่าง (High Demand, Low Supply) คือจุดที่เป็น Skill Mismatch อย่างรุนแรง (โอกาสพัฒนาหลักสูตร)

---

## 4. Antigravity System Instructions (Developer Prompt)
To the Antigravity Agent: 
1. Use `dash` core components (`dcc`), `dash.html_components` (`html`), and `dash_bootstrap_components` (`dbc`) for styling.
2. Please generate a Python script containing a fully functional Dash app based on the requirements above.
3. **MOCK DATA:** Generate synthetic Pandas DataFrames for both Supply and Demand sides to make the app runnable out of the box. Ensure the data allows for cross-filtering.
4. **CALLBACKS:** This is critical. Implement `@app.callback` decorators for Tab 1 and Tab 2. If a user clicks data in Chart 1.1 (`clickData` property), filter the DataFrame and update Charts 1.2, 1.3, 1.4 accordingly.
5. **UI/UX:** Provide a clean layout. Put the Tabs at the top. Use Bootstrap Grid (Rows and Columns) to place the charts nicely on a desktop screen.

**End of BRD**