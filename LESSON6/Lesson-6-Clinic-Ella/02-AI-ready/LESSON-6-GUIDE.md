# Lesson 6 - Business Archive for Skills Development

## 📚 Overview

This archive contains a complete, real-world business dataset (Clinic Ella) organized for use in Lesson 6 skills development. You will use this data to build two downstream skills:

1. **financial-dashboard** - Analyze and visualize financial data
2. **landing-page** - Create a professional landing page with branding

---

## 🎯 Lesson Objectives

### What You'll Learn

**Skill 1: Financial Dashboard Builder**
- Extract financial data from business records
- Analyze revenue patterns and trends
- Create interactive financial visualizations
- Build key performance indicators (KPIs)
- Present financial health to stakeholders

**Skill 2: Landing Page Designer**
- Understand brand identity and visual guidelines
- Incorporate marketing assets (logos, photos)
- Write compelling service descriptions
- Showcase customer testimonials
- Create professional web presence

---

## 📁 Archive Structure for Skills

```
קליניקת-אלה-ארכיון/
├── 00-מקור-גולמי/           (Read-only backup - DO NOT TOUCH)
├── 01-מאורגן/                (Organized by category)
│   ├── הנהלת-חשבונות/       ← Use for financial-dashboard
│   │   ├── חשבוניות/        (Invoice PDFs)
│   │   ├── מחירון טיפולים/  (Service pricing)
│   │   ├── הנהלת חשבונות*.xlsx (Accounting records)
│   │   └── קבלות ספקים/     (Supplier receipts)
│   │
│   ├── שיווק-ומותג/          ← Use for landing-page
│   │   ├── לוגו/             (Logo files)
│   │   ├── מיתוג/            (Branding materials)
│   │   ├── תמונות קליניקה/   (Clinic photos)
│   │   ├── מצגות/            (Service presentations)
│   │   └── מדריך מיתוג*.pdf  (Brand guidelines)
│   │
│   ├── בנקאות-ואשראי/        (Financial context)
│   ├── משפטי-וחוזים/         (Legal context)
│   ├── תקשורת-וביקורות/     (Customer testimonials)
│   └── לא-מסווג/             (Additional resources)
│
└── 02-AI-ready/              (For skill consumption)
    ├── BUSINESS-PROFILE.md   (Complete business analysis)
    ├── LESSON-6-GUIDE.md     (This file)
    └── [Skills will add outputs here]
```

---

## 💰 FINANCIAL DASHBOARD SKILL

### Source Data Location
**Primary:** `01-מאורגן/הנהלת-חשבונות/`

### Available Financial Data

#### 1. **Accounting Records** (Multi-year)
- `הנהלת חשבונות 2023.xlsx` - Full year 2023
- `הנהלת חשבונות 2024.xlsx` - Full year 2024
- `הנהלת חשבונות 2025.xlsx` - Full year 2025
- `הנהלת חשבונות 2026 (חלקי).xlsx` - 2026 YTD (through May)

**What to Extract:**
- Monthly revenue figures
- Monthly expenses
- Profit/loss calculations
- Cost of goods/services
- Overhead costs (rent, utilities, salaries)
- Year-over-year growth trends

#### 2. **Service Pricing** (Revenue Model)
- `מחירון טיפולים 2025.xlsx` - Current pricing structure
- Lists all services and their current prices
- Basis for understanding service mix and revenue potential

**What to Extract:**
- Service catalog
- Price points for each treatment
- Package bundles and discounts
- Service categories
- Product/service hierarchy

#### 3. **Invoice Records** (Customer Transactions)
- 34 invoice PDFs (חשבונית #1040-#1073)
- Recent transaction records from 2026
- Details on per-transaction revenue

**What to Extract:**
- Transaction dates and amounts
- Service/item breakdown per invoice
- Customer transaction frequency
- Average invoice value
- Sales trends (if dates available)

#### 4. **Banking Records** (Cash Flow Context)
- `דפי בנק/` - 13+ months of bank statements
- Bank: Bank Poalim
- Shows actual cash flow and payment patterns

**What to Extract:**
- Deposit patterns (showing customer payments)
- Cash outflows (expenses)
- Account balances over time
- Payment timing and frequency
- Seasonal patterns

#### 5. **Supplier Receipts** (Cost Data)
- 4 documented supplier receipts (קבלות ספקים)
- Shows costs of goods/materials
- Supplier relationships

**What to Extract:**
- Cost of materials/products
- Supplier names and pricing
- Purchase frequency
- Bulk pricing patterns

### Suggested Dashboard Sections

#### 📊 Revenue Analysis
- **Total Revenue Trend** - Line chart showing monthly/yearly revenue
- **Revenue by Service** - Bar or pie chart breakdown
- **Monthly Revenue Comparison** - Year-over-year comparison (2024 vs 2025 vs 2026)
- **Average Transaction Value** - Trend over time

#### 📈 Profitability Metrics
- **Gross Profit Margin** - Revenue minus COGS
- **Operating Profit** - After all expenses
- **Profit Trend** - Monthly profitability line chart
- **Key Ratios** - Gross margin %, net profit %

#### 💸 Expense Analysis
- **Monthly Expenses** - Breakdown by category
- **Expense vs Revenue** - Percentage of revenue consumed
- **Expense Trends** - Growing or shrinking?
- **Fixed vs Variable Costs** - What's truly variable?

#### 👥 Customer Insights (From Invoices)
- **Customer Count** - Number of unique customers per month
- **Repeat Customer Rate** - % of returning customers
- **Customer Lifetime Value** - Total per customer over available data
- **Acquisition Trends** - New vs returning customers

#### 🎯 Key Performance Indicators (KPIs)
- **Monthly Recurring Revenue (MRR)** - Predictable revenue
- **Customer Acquisition Cost (CAC)** - From marketing data if available
- **Payback Period** - How long to recover CAC
- **Breakeven Analysis** - Fixed costs / contribution margin
- **Growth Rate** - Month-over-month or year-over-year

### Data Challenges & Solutions

**Challenge:** Excel files are binary  
**Solution:** Ask the user to provide CSV exports, or manually transcribe key figures

**Challenge:** 2026 data is incomplete  
**Solution:** Show as "YTD" and note the timeframe explicitly

**Challenge:** May be missing detailed P&L breakdown  
**Solution:** Use invoice totals + expense records to estimate

### Success Metrics for This Skill
- ✅ Clear visualization of revenue trends
- ✅ Profitability picture (or path to profitability)
- ✅ Identified top revenue services
- ✅ Understood expense structure
- ✅ Highlighted any concerning trends
- ✅ Provided actionable insights for business growth

---

## 🎨 LANDING PAGE SKILL

### Source Data Location
**Primary:** `01-מאורגן/שיווק-ומותג/`  
**Secondary:** `תקשורת-וביקורות/` for testimonials

### Available Brand & Marketing Data

#### 1. **Visual Identity**
- `מיתוג - צבעים ופונטים.pdf` - Brand guidelines
  - Colors: Rose-Gold (primary), Cream (background), Charcoal (text)
  - Tone: Warm, professional, personal, premium
  - Typography rules and usage guidelines

#### 2. **Logo Assets** (3 versions)
- `logo_final.jpg` - Current/primary logo
- `logo_final2.jpg` - Alternative version
- `לוגו ישן.jpg` - Legacy logo (reference only)

**Usage:** Logo in header, hero section, footer

#### 3. **Professional Photography** (11 images)
- **Team Photos:**
  - `אלה ברנע.png` - Owner Ella (key for personal branding)
  - `הצוות.png` - Staff team shot

- **Facility/Ambiance:**
  - `חזית הקליניקה.png` - Clinic exterior/entrance
  - `חלל הקליניקה.png` - Interior space/waiting area
  - `חדר טיפולים.png` - Treatment room

- **Before/After/Results:**
  - `טיפול פנים.png` - Facial treatment in progress
  - `עור לפני.png` - Before skin condition
  - `עור אחרי.png` - After treatment results
  - `אווירה.png` - Ambiance/atmosphere

- **Products:**
  - `מוצר.png` - Treatment product
  - `מוצרי טיפוח.png` - Care product line

**Usage:** Hero section, service showcase, gallery, testimonial section

#### 4. **Branding Materials**
- `favicon.jpg` - Small icon for browser tab
- `באנר אביב.jpg` - Spring campaign banner
- `באנר ייעוץ.jpg` - Consultation banner
- `כרטיס ביקור.jpg` - Business card design (visual reference)

#### 5. **Marketing Content Documents**
- Service descriptions (from presentations)
- FAQ (שאלות נפוצות) - Common questions and answers
- Customer testimonials theme/messaging

### Service Information

From **מחירון טיפולים 2025.xlsx** (not directly readable, but inferred):
- Botox treatments (prominent in reviews)
- Deep facial treatments (פנים עמוק)
- Beauty consultations
- Packages and bundles

### Customer Testimonials** (45+ reviews)

**Source:** `תקשורת-וביקורות/ביקורות ודירוגים/Google ביקורות - ייצוא.csv`

**Key Themes to Highlight:**
- ✅ Natural-looking results
- ✅ Professional + warm atmosphere  
- ✅ Personalized treatment plans
- ✅ Ella's personal expertise
- ✅ Excellent customer service
- ✅ Visible, satisfying results

**Sample Quotes to Use:**
- *"Botox came out completely natural, exactly what I wanted!"*
- *"Ella really listens and builds a customized plan. Doesn't push sales."*
- *"Professional yet warm. Home-like ambiance. 5 stars!"*
- *"After years of trying other places, I saw real difference quickly."*

### Suggested Landing Page Sections

#### 1. **Hero Section**
- Logo (top left/center)
- Main headline: "Welcome to Clinic Ella - Natural Beauty, Professional Care"
- Subheadline: "Personalized aesthetic treatments with natural-looking results"
- Call-to-action: "Schedule Your Consultation"
- Background: Clinic ambiance photo or warm gradient in brand colors

#### 2. **About Section**
- Ella's photo + short bio
- Clinic mission/philosophy
- "Why Clinic Ella?" - Competitive advantages
- Warm, personal tone
- Trust-building messaging

#### 3. **Services Section**
- Botox Treatments
  - Description
  - Key benefits
  - Before/after image
  - Price range

- Deep Facial Treatments
  - Description
  - Skin types served
  - Benefits
  - Treatment duration

- Consultations
  - Free or paid?
  - What to expect
  - How to book

#### 4. **Gallery**
- Team photo
- Clinic facilities
- Treatment in progress
- Before/after results
- Product showcase
- Ambiance/atmosphere

#### 5. **Testimonials**
- Customer review carousel/cards
- Star rating system
- Name and date
- Thematic grouping (e.g., "Natural Results", "Great Experience")
- Link to full Google reviews

#### 6. **Pricing/Packages** (Optional)
- Service pricing table
- Package options
- Value proposition
- CTA: "Get Pricing Details"

#### 7. **Contact/CTA**
- Schedule button (prominent)
- Phone number
- Hours
- Location (with parking info if available)
- Contact form

#### 8. **Footer**
- Logo
- Quick links
- Contact info
- Social/Google reviews link
- Copyright

### Design Requirements

**Color Palette:**
- Primary: Rose-Gold (#D4AF9F or similar)
- Background: Cream/Ivory (#FFF8F0 or similar)
- Text: Charcoal Gray (#333333 or similar)
- Accent: White, subtle shadows

**Tone & Voice:**
- Professional but warm
- Personal (emphasize Ella)
- Premium positioning
- Trustworthy and expert
- Non-pushy

**Key Brand Attributes to Convey:**
- ✅ Professional expertise
- ✅ Natural results
- ✅ Warm, personal service
- ✅ Premium experience
- ✅ Results-driven
- ✅ Trustworthy

### Assets Provided

- Logos (3 versions) - Use primary
- 11 professional photos - Use strategically
- Brand guidelines (colors, tone) - Follow guidelines
- Customer testimonials (45+) - Curate best ones
- Service descriptions (from materials)

### Success Metrics for This Skill
- ✅ Professional appearance
- ✅ Brand consistency (colors, tone, imagery)
- ✅ Clear service/offering communication
- ✅ Strong social proof (testimonials)
- ✅ Clear calls-to-action
- ✅ Mobile-responsive design
- ✅ Emotional connection (warm, personal)
- ✅ Conversion-focused (scheduling CTA)

---

## 🚀 How to Use This Archive

### Step 1: Explore the Data
Start with reading:
1. `BUSINESS-PROFILE.md` - Understand the business
2. This guide - Understand what you're building
3. Browse the organized files - Get familiar with assets

### Step 2: Extract Key Data
- **For financial-dashboard:** List out financial figures from Excel files
- **For landing-page:** Collect testimonials, decide which photos to feature

### Step 3: Build Financial Dashboard
- Run the financial-dashboard skill
- Point it to `01-מאורגן/הנהלת-חשבונות/`
- Output: Interactive dashboard showing financial health

### Step 4: Build Landing Page
- Run the landing-page skill
- Point it to `01-מאורגן/שיווק-ומותג/`
- Output: Professional landing page with branding and testimonials

### Step 5: Review & Iterate
- Check outputs against business reality
- Refine visualizations or design
- Validate metrics and messaging

---

## 📊 Key Numbers for Reference

From the archive analysis:
- **Company Age:** Operating since at least 2023 (4 years of records)
- **Invoice Volume:** 34+ invoices in 2026 YTD (5 months)
- **Customer Base:** 45+ documented reviews (Google)
- **Review Ratings:** Predominantly 4-5 stars
- **Assets:** 11 professional photos, 3 logo versions
- **Services:** Botox, facials, consultations
- **Target Market:** Adult women, premium aesthetic services
- **Geographic:** Israel-based, location-aware customers

---

## 💡 Tips for Success

### For Financial Dashboard
1. **Start with annual totals** - Get the big picture first
2. **Then break down to months** - See seasonal patterns
3. **Compare years** - Understand growth trajectory
4. **Identify trends** - What's growing/declining?
5. **Calculate ratios** - Margin %, growth %, efficiency metrics
6. **Highlight insights** - What surprised you?

### For Landing Page
1. **Lead with the owner** - Ella is the brand
2. **Use natural language** - Avoid corporate jargon
3. **Show social proof early** - Testimonials are powerful
4. **Make it scannable** - Short paragraphs, clear sections
5. **Mobile first** - Most visitors on phone
6. **Strong CTA** - Make booking easy
7. **Color consistency** - Use the brand palette throughout

---

## 📝 Exercises for Lesson 6

### Exercise 1: Financial Dashboard
**Goal:** Build an interactive dashboard showing Clinic Ella's financial health

**Deliverables:**
- [ ] Revenue trend chart (monthly, last 24 months)
- [ ] Service breakdown (which services generate most revenue?)
- [ ] Expense analysis (where does money go?)
- [ ] Profitability metrics (margins, growth rate)
- [ ] KPI summary (top 5 metrics to watch)
- [ ] Actionable insights (3 recommendations based on data)

### Exercise 2: Landing Page
**Goal:** Create a professional landing page that drives clinic bookings

**Deliverables:**
- [ ] Hero section (compelling, shows professionalism)
- [ ] About/Owner section (personal connection)
- [ ] Services clearly explained with pricing
- [ ] Gallery with clinic and before/after photos
- [ ] Testimonials section (social proof)
- [ ] Clear CTA for booking appointments
- [ ] Mobile responsive design
- [ ] Brand-consistent styling

---

## 🎓 Learning Outcomes

After completing these exercises, you will understand:

✅ How to extract and analyze real business data  
✅ How to visualize financial data for decision-making  
✅ How to tell a story with data  
✅ How to build professional brand presence online  
✅ How to use customer feedback in marketing  
✅ How to design for conversion (booking/sales)  
✅ How business data, marketing, and operations interconnect  

---

## 📞 Questions?

If data is unclear:
- Check `BUSINESS-PROFILE.md` for context
- Review files in original folders (`01-מאורגן/`)
- Look for backup copies (files often have duplicates with different names)

Remember: **The goal is to build skills**, not to perfectly replicate every number. Use the data to tell Clinic Ella's story and demonstrate your understanding of financial analysis and marketing design.

---

*Archive prepared for Lesson 6 - Business Skills Development*  
*Real data from Clinic Ella, organized for learning purposes*  
*Date: 2026-09-18*
