# Designing Financial Models Notes

My personal study notes for MBA 236G, Designing Financial Models that Work (DFMW), taught by Jenny Herbert-Creek at Berkeley Haas, Fall 2026. Written from the Class 1 and Class 2 slides, the DFMW Style Guide (Parts 1 and 2), the Formulas and Frameworks Reference Guide, and the Estimation and Mental Math Reference Guide. These notes paraphrase the course material in my own structure; they are not a copy of it.

## 1. What a financial model is

The course defines a financial model in three layers:

1. A representation of reality.
2. A calculator.
3. A tool to build shared conceptual understanding and create business impact.

The third layer is the point of the course. A model that calculates correctly but that nobody understands or trusts does not change a decision.

Why the course exists: newcomers get exposure to modeling, experienced modelers learn to build models that are easier to understand, and everyone practices best practices, reasoning by analogy, mental math and ballparking, Excel and AI spreadsheet tools, listening and empathy, and communicating to decision makers.

## 2. The four DFMW core concepts (the "what")

Every model should answer four questions:

1. **Audience and question:** who is this for, and what question are we examining?
2. **Business story:** what is the underlying business story?
3. **Tools:** how do our tools bring our thinking to life?
4. **Quality:** is our model accurate, transparent, and empowering?

## 3. The DFMW design process (the "how")

The intersections between the four core concepts form a four step design process:

| Step | Name | Key activities |
|---|---|---|
| 1 | Frame and Sketch | Who is the audience? What is my intention? Use simplifying formulas. |
| 2 | Estimate and Build | Estimate and ballpark, choose your tools, follow best practices. |
| 3 | Stress Test and Iterate | Consider scenarios, test the model, build sensitivity analysis. |
| 4 | Validate, Socialize and Communicate | Check for accuracy, solicit feedback, deliver with impact. |

Class 1 covered Frame and Sketch plus Estimate. Class 2 focused on Build: the style guide, visual hierarchy, and fast formatting tools.

## 4. Step 1: Frame and Sketch

### Framing questions

* **Audience:** who needs this model, and what decision are they making?
* **Scope:** what do we need in order to evaluate the decision? Be cautious of overbuilding.
* **Simplifying formula:** what are we actually calculating? The default starting point is Profit = Revenue − Variable Costs − Fixed Costs.

### The model brief

The output of the Frame stage is a short model brief of three or four sentences that captures the question, the audience, the decision, and the timing. The brief launches the Sketch and Estimate work, whether I do that work myself or with AI.

### Where AI helps and where it fails in framing

AI does well at pressure testing a brief I already drafted, surfacing stakeholder perspectives I missed, suggesting sub questions a thoughtful colleague would ask, and tightening vague language.

AI falls short because it accepts whatever question I give it. If I ask for a model that answers the wrong question, I get a presentable, well organized model that answers the wrong question. AI also tends to over scope, suggesting extra sub models the decision does not need, and it usually does not know my audience as well as I do.

Useful framing prompts, to AI or to myself:

* Pressure test my brief: is the question well formed, is it the right question for this audience and decision, is anything missing or over scoped?
* What do I actually need to know about this audience before I build?
* Imagine you are the CFO, founder, or loan officer receiving this model: what do you want to see first, what makes you trust it, what makes you stop reading?
* What decision is actually being made, who has authority, what are the realistic options, and what information would tip the decision?

## 5. Case example: The Kitchen at Clark Street

The running case in Class 1.

* The restaurant has 46 seats and serves two dinner turns (seatings) each night.
* A separate takeout window runs from morning prep through late lunch and serves long lunch lines.
* The dining room is booked weeks out, but after a year of doing nearly everything right the P&L is barely breaking even.
* **Players:** Carmine ("Carm") Russo, co owner and head chef; his sister Natalie ("Nat"), co owner running front of house; Uncle Jimmy, the lead investor, who is patient but wants "a line of sight to returns."
* The window crew believes the daytime concept could scale beyond Clark Street if it were unbundled and launched at a second location.

### Revenue assumptions Nat provided

| Assumption | Value |
|---|---|
| Dinner seats | 46, turned twice per night |
| Dinner spend per cover | $24 drinks + $64 food = $88 |
| Dinner days per week | 4 |
| Lunch counter orders per day | 135 |
| Lunch average check | $16.50 |
| Lunch days per week | 5 |
| Weeks operating per year | 52 |

### My worked revenue sketch

* Dinner: 46 seats × 2 turns = 92 covers per night. 92 × $88 = $8,096 per night. × 4 nights × 52 weeks = **$1,683,968 per year**.
* Lunch: 135 orders × $16.50 = $2,227.50 per day. × 5 days × 52 weeks = **$579,150 per year**.
* Total annual revenue ≈ **$2.26 million**, with dinner about three quarters of it.

Ballpark check: 90 covers × $90 ≈ $8,000 a night, × 200 nights ≈ $1.6M; lunch 135 × $16.50 ≈ $2,200 a day × 250 days ≈ $550K; total ≈ $2.2M, within 20% of the exact figure.

## 6. Step 2a: Estimate (ballpark before building)

The goal of this stage is three things that together launch the Build: a sketch of the model's structure, a **check figure** (my estimate of the answer), and a list of key assumptions.

The check figure should be within about **20% of the exact answer**. It is not the final answer; the spreadsheet produces that. Its job is to catch errors: a missing input or section, a wrongly coded formula, or forgetting to annualize or scale the result.

### The six step estimation process

1. **Sketch:** identify the structure and the simplifying formula (usually P × Q for revenue, or a sum of cost categories for expenses).
2. **Identify the inputs:** write the raw numbers from the case or my own estimates on the sketch.
3. **Compute in chunks:** work bottom up, compute small pieces, label each intermediate result.
4. **Round to compatible numbers:** round aggressively to friendly numbers built from 2s, 5s and 10s. Rounding more is better than skipping the estimate.
5. **Annualize or aggregate:** convert per period figures to the model's time frame.
6. **Sanity check:** does the final number make sense, and is it the right order of magnitude?

### Strategic rounding

Pick numbers that make the next operation easy ("compatible numbers"), not simply the nearest number. Friendly numbers: 5, 10, 20, 25, 50, 100, 200, 500, 1,000.

Examples: $5.50 × 4 becomes $5 × 5 = $25 rather than $6 × 4 = $24, because 25 is easier to reuse. $23.40 × 1,850 becomes $25 × 2,000 = $50K.

**Offset the rounding:** when I round one factor up, round the other down so errors do not compound. In the ZipCar sketch, 4 hours × $5.50 became 5 hours × $5.00 = $25, and 22 miles × $0.40 became 20 miles × $0.50 = $10. Monthly trips of 880 rounded up to 1,000, so the annual multiplier was rounded down from 12 to 10.

### Common order of magnitude mistakes

| Mistake | Example | How to spot it |
|---|---|---|
| Forgot to annualize | $4,200 per month × 15 units = $63K, but that is monthly; the annual figure is $756K | Ask: is this monthly or yearly? |
| Mixed up time periods | 220 members × 4 trips per month = 880, used as a yearly total | Label every intermediate result with its time unit |
| Added instead of multiplied | 30 students × $40 should be $1,200, not $70 | The product should have more digits |
| Dropped or added a zero | $55 entered instead of $5.50 | Is the answer exactly 10× or 0.1× the expectation? |
| Double negative | Subtracting a fee already stored as negative | After subtracting, is the result smaller? |

### Unit conversions and benchmarks

| Convert to annual | Exact | Quick math |
|---|---|---|
| Per hour | × 2,000 | × 2,000 |
| Per day | × 365 | × 350 or × 400 |
| Per week | × 52 | × 50 |
| Per month | × 12 | × 10, then adjust |
| Per quarter | × 4 | × 4 |

Benchmarks to sanity check outputs: about 2,000 hours in a work year; about 335 million people in the US; about 130 million US households; $1M of annual revenue is about $2,750 per day or $83K per month; a $100K salary is about $50 per hour.

### Mental math shortcuts

* Percentages are built from two anchors: 10% (move the decimal one place) and 1% (move it two places). 5% is half of 10%, 15% is 10% + 5%, 20% is 10% doubled, 25% is divide by 4, 12.5% is half of 25%, 75% is 100% − 25%.
* Multiplication uses the distributive property: 48 × 15 = 48 × 10 + 48 × 5 = 720. × 5 is × 10 then halve; × 25 is × 100 then divide by 4; × 12 is × 10 plus × 2; × 52 is × 50 plus × 2; × 365 is × 400 minus × 35.

### Where AI helps and fails in sketching and estimating

AI helps by reviewing a sketch for gaps, suggesting missing assumptions, checking whether a check figure is in a reasonable range, and researching benchmark numbers (ask it to cite direct sources).

AI fails because it can produce a sketch that looks complete but lacks design judgment, it will happily invent plausible numbers when I have not supplied any, and it can validate a wrong check figure because "reasonable" depends on knowing the business.

## 7. Step 2b: Build, and how "good design" is decided

The course decides what counts as good design in three ways:

1. **Context:** who uses the model and for what purpose.
2. **Principles:** domain specific guidelines for good design.
3. **Testing:** the wisdom of the crowd, for example the ZipCar scavenger hunt, where several models all reached the correct answer with very different design choices, and two of them were built with AI.

Guiding quote from John Gall, *Systemantics*: a complex system that works has invariably evolved from a simple system that worked. So we design small sections ("paragraphs") first, then full worksheets.

## 8. DFMW Style Guide, Part 1: small sections

The style guide was curated by the instructor from about a dozen modeling best practice guides, mostly from investment banking plus university and trade association guides. Where sources disagree, the course's design principles break the tie.

### Model structure

* **Calculations:** perform each calculation only once and refer back to it. Show intermediate steps instead of long formulas; "transparency should drive structure." Formulas flow left to right and top to bottom, which also helps avoid circular references.
* **Assumptions:** never hard code assumptions inside formulas; separate inputs from calculations. For small models, integrate assumptions into the story and calculation flow rather than a separate assumptions section. A separate inputs section makes sense for large, reused models such as a group wide LBO template.
* **Labels:** every input and output cell gets a clear, concise label. Avoid acronyms.

### Formatting

* **Fonts:** one font and size throughout, 10 to 12 point. Default Excel fonts: Calibri, Aptos (the current default), or Arial, unless a company brand guideline applies.
* **Colors:** royal blue font for all constants (inputs), so it is obvious what can be changed. Black font for all formulas and text. Green is reserved for later; in investment banking, green usually marks references to other sheets, and sometimes historical data.
* **Number formats:** parentheses for negatives; thousands separator always on; Currency format for money, with the dollar sign shown each time, except long currency lists may show it only on the first and last line; Percentage format for percentages; Number or General for other numbers; custom formats (for example multiples) only sparingly.
* **Alignment:** never merge cells. Center only sparingly for a page title or section. Otherwise text left, numbers right, and column headers aligned to match their data. Indent sub calculations.
* **Bold, italics, fill, borders:** bold for key section titles, summaries, results, dates and column headers. Italics only for percentages that are formula results (for example net income as a percent of sales), never for percentage inputs. No fill for small sections. Top and bottom borders, not underlines, to set off titles, summaries, dates and headers.

## 9. DFMW Style Guide, Part 2: worksheet tabs

### Decimals (Training the Street recommendations)

* No decimals: years, and $ in thousands.
* One decimal: most multiples, most percentages, $ in millions.
* Two decimals: earnings per share, some percentages, some multiples.

Aim for consistency across the worksheet unless there is a good reason to vary.

### Page layout

* Print on one page, landscape.
* Leave row 1 and column A empty as an "entry point."
* Turn off gridlines.
* Put a title in the top left of every sheet, with the time period or scenario underneath if relevant.
* Rename the worksheet tab.

### Visual hierarchy

The primary goal of formatting in larger models is visual hierarchy: letting the reader take in the model's structure at a glance. Use a limited set of styles for five elements:

1. Worksheet title
2. Section headers (major groupings such as revenue and expenses)
3. Section summaries (subtotals that close each section)
4. Worksheet summary (the final output or key takeaway)
5. "Normal" style for everything else

Expanded toolkit: font size 16, light gray fill, navy blue fill, white text on navy, ALL CAPS, and full cell borders. Any combination works if it is applied consistently. Three example combinations from the guide:

| Element | Example 1 | Example 2 | Example 3 |
|---|---|---|---|
| Worksheet title | Size 16, bold | Size 16, bold | Navy fill, white text |
| Section headers | Navy fill, white text | Bold, bottom border | Bold, ALL CAPS |
| Section summary | Light gray fill, bold | Bold, top border | Bold, ALL CAPS, top border |
| Worksheet summary | Bold, full outline | Navy fill, white text | Gray fill |

## 10. AI tools for Excel

| Tool | How it works | Best for | Limitations |
|---|---|---|---|
| Basic LLMs (ChatGPT, Gemini) | Copy and paste into a browser chat | Formula help, learning concepts, brainstorming structure | No Excel integration; cannot see my data |
| Microsoft Copilot | Native Excel sidebar in Microsoft 365 | Quick summaries, simple formatting, PivotTables | Weak on complex formula logic; needs a Copilot license |
| Shortcut AI | Excel add in that reads and writes cells | Formula generation, data cleaning, banking models | Subscription; learning curve; less suited to full builds |
| Claude for Excel | Excel add in that reads and writes cells | Structured formatting, multi step automation | Needs an Anthropic API key; newer and still evolving |

The instructor also built an agentic "fast formatting" workflow: she had Claude analyze her corpus of design materials and sample spreadsheets, draft instructions encoding her style guide, and then turned those instructions into a reusable skill that reformats a file to her design.

## 11. Formulas and frameworks for the Frame step

A starting menu of simplifying formulas, meant to generate ideas rather than serve as a definitive list.

**Revenue:** Revenue = Price × Quantity; multi stream revenue = sum of P × Q per stream; recurring revenue: ending ARR = beginning ARR + new − churn + expansion; capacity based revenue = capacity × utilization × revenue per unit (hotels, airlines, restaurants); advertising = impressions × conversion rate × revenue per conversion; cohort revenue = sum of cohort × retention × ARPU.

**Profit and unit economics:** contribution margin = price − variable cost, and CM% = CM / price; gross margin = (revenue − COGS) / revenue; operating margin = EBIT / revenue; net margin = net income / revenue; breakeven units = fixed costs / CM per unit; breakeven revenue = fixed costs / CM%; operating leverage = % change in operating income / % change in revenue; ROI = (benefit − cost) / cost; ROIC = NOPAT / invested capital.

**Operating models:** profit = revenue − variable costs − fixed costs; cash runway = cash balance / monthly net burn; EBITDA = revenue − COGS − opex excluding D&A; payback period = investment / annual cash flow (ignores time value of money); the "corkscrew": ending balance = beginning + additions − losses, used for anything that accumulates over time.

**Working capital:** DSO = average AR / revenue × 365; DIO = inventory / COGS × 365; DPO = AP / COGS × 365; cash conversion cycle = DSO + DIO − DPO.

**Valuation:** NPV = sum of discounted cash flows − investment; IRR = the rate where NPV = 0; free cash flow = NOPAT + D&A − change in working capital − capex; DCF = discounted FCF + terminal value; multiples: EV = metric × comparable multiple.

**Pricing and market sizing:** price elasticity = % change in quantity / % change in price (absolute value above 1 is elastic); markup = (price − cost) / cost, which is not the same as margin; TAM, SAM, SOM.

**Customer and SaaS metrics:** customer lifetime value = average purchase × frequency × lifespan; CAC = sales and marketing spend / new customers; CAC payback = CAC / monthly gross profit; churn = lost customers / starting customers; ARPU = revenue / users; net dollar retention = (start MRR + expansion − churn) / start MRR; Rule of 40: growth % + EBITDA margin % ≥ 40%; SaaS quick ratio = (new + expansion MRR) / (churn + contraction); viral coefficient K = referrals per customer × conversion, with K above 1 meaning viral growth.

**Funnels:** conversion rate, click through rate, AARRR (acquire, activate, retain, refer, revenue), NPS = % promoters − % detractors, with above 50 considered good.

**Risk and uncertainty:** expected value = sum of outcome × probability; scenario analysis (base, upside, downside); sensitivity analysis (vary one or two inputs, for example data tables and tornado charts); Monte Carlo simulation.

**Platforms:** marketplace revenue = GMV × take rate; network effects, value proportional to users squared (Metcalfe's Law); creator economy = followers × monetization rate × revenue per follower.

**Strategy frameworks:** Porter's Five Forces, Business Model Canvas, Ansoff Matrix, SWOT, BCG Matrix, 3Cs.

## 12. Course logistics

* Homework runs on two tracks. Part A reinforces weekly concepts: HW 1 builds two small models, HW 2A and 2B cover a housing case and a unit economics case with a partner, HW 3 revises a one tab model, HW 4 builds a multi tab cash burn model with a partner, HW 5 is a choice between a data analysis case and a multi tab model, and HW 6 on data visualization is optional.
* Part B builds my personal model: HW 1 Frame and Sketch, then research inputs and assumptions, HW 3 drafts one tab, HW 4 revises it after feedback.
* **Final deliverable, choose one path:**
  * Option 1, "Excel Expert" final quiz: individual, case based, covers Classes 1 to 6, no AI, taken in class on **October 14** through Honorlock.
  * Option 2, "AI Modeler" final project: team of 1 or 2, a 5 to 7 tab model, a 4 to 5 page reflection paper, and a 15 minute presentation with the instructor, due **October 14 at 11:59 pm**.
