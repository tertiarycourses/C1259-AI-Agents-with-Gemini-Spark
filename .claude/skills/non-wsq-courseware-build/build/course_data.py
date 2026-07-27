"""
SINGLE SOURCE OF TRUTH — C1259 AI Agents with Gemini Spark (non-WSQ).

A beginner, two-day, hands-on short course on building and running autonomous AI
agents with Google Gemini Spark across Google Workspace (Gmail, Calendar, Drive,
Docs, Sheets, Slides). Every artifact (PPT, LP, LG, LG.md) and every lab is
generated from this module + data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C1259.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI Agents with Gemini Spark (C1259)"
SHORT_TITLE  = "AI Agents with Gemini Spark (C1259)"   # used in output filenames
COURSE_CODE  = "C1259"                                 # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain what autonomous AI agents are and how Gemini Spark's background agents, approvals and controls work.",
    "LO2: Connect Gemini Spark to Google Workspace and write clear, effective instructions that an agent can act on.",
    "LO3: Create one-off agent tasks to research, organise, summarise email and draft content across Docs, Sheets and Slides.",
    "LO4: Review, approve and refine agent actions so automated work stays accurate and under your control.",
    "LO5: Build custom reusable skills and design schedules and conditional triggers that run automatically.",
    "LO6: Chain multi-step workflows across several Workspace apps and personalise your agent's behaviour and style.",
    "LO7: Automate real-world workflows — lead management, expenses and planning — with sound permission and privacy guardrails.",
    "LO8: Monitor, improve and scale your AI agents responsibly.",
]
LO_TITLES = [
    "Understand agents",
    "Connect & instruct",
    "Automate with tasks",
    "Review & approve",
    "Skills & schedules",
    "Chain & personalise",
    "Real-world automation",
    "Monitor & scale",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with AI Agents and Gemini Spark",
         subtitle="What autonomous agents are · How Spark works · Connecting Workspace · Instructing your agent",
         weighting="25%",
         concepts=[
            "Autonomous AI agents — an agent doesn't just answer; it plans and carries out multi-step tasks toward a goal you set.",
            "Gemini Spark — Google's agentic layer that works across your Workspace apps to get real tasks done for you.",
            "Background agents — Spark can work through a task on your behalf while you get on with something else.",
            "Approvals and control — Spark pauses for your approval before it sends, shares or changes anything that matters.",
            "Connecting Workspace — Spark acts through Gmail, Calendar and Drive using your existing Google account permissions.",
            "The activity log — every action an agent takes is recorded so you can see, trust and undo what it did.",
            "Effective instructing — a good instruction states the goal, the inputs, the output and the limits in plain language.",
            "Prompt vs instruction — a chat prompt asks for text; an agent instruction asks for an outcome you can check.",
         ]),
    dict(num=2, code="02",
         title="Automating Work with Gemini Spark Tasks",
         subtitle="One-off tasks · Email summaries and drafting · Docs, Sheets and Slides · Reviewing and refining",
         weighting="30%",
         concepts=[
            "One-off tasks — a single instruction Spark runs once, ideal for research, clean-up and organising work.",
            "Research tasks — ask the agent to gather, compare and summarise information into a structured result you can reuse.",
            "Inbox summaries — Spark reads a busy inbox and hands you a short, prioritised digest of what needs attention.",
            "Email drafting — the agent drafts replies in your voice and leaves them for you to review before anything is sent.",
            "Working with Docs — generate outlines, first drafts and formatted documents straight into Google Docs.",
            "Working with Sheets — turn messy inputs into a clean, structured spreadsheet the agent fills for you.",
            "Working with Slides — draft a presentation deck from a brief or a document, ready for you to polish.",
            "Reviewing and refining — you inspect each result, approve the good, and refine the instruction until it is right.",
         ]),
    dict(num=3, code="03",
         title="Building Reusable Skills and Schedules",
         subtitle="Custom reusable skills · Schedules and triggers · Chaining workflows · Personalising behaviour",
         weighting="25%",
         concepts=[
            "Reusable skills — save a proven instruction as a named skill you can run again and again without re-typing it.",
            "The Ghostwriter skill — a worked example: a skill that drafts content in a consistent, personalised style on demand.",
            "Schedules — set an agent to run on a cadence, such as a digest every weekday morning, with no manual trigger.",
            "Conditional triggers — run a skill only when a condition is met, such as a new email from a specific sender.",
            "Chaining — connect skills so the output of one becomes the input of the next, forming a multi-step workflow.",
            "Personalisation — teach the agent your preferences, tone and recurring context so its output needs less editing.",
            "Style and voice — capture how you write once, and have every draft match it automatically.",
            "Skill hygiene — name, describe and test each skill so you and your team know exactly what it does.",
         ]),
    dict(num=4, code="04",
         title="Advanced Agentic Workflows and Real-World Automation",
         subtitle="Lead, expense and planning automation · Multi-app coordination · Guardrails · Monitoring and scaling",
         weighting="20%",
         concepts=[
            "Real-world automation — assemble skills and schedules into workflows that handle everyday business tasks end to end.",
            "Lead management — capture an enquiry, log it to a sheet and draft a timely follow-up, all through the agent.",
            "Expense and planning — turn receipts and notes into a tidy record, and a rough plan into a scheduled agenda.",
            "Multi-app coordination — a single workflow that spans Gmail, Calendar, Drive and Sheets in one connected run.",
            "Guardrails — set explicit limits on what an agent may do, so automation is safe by design, not by luck.",
            "Permissions and privacy — grant least access, keep confidential data out of prompts, and know where data flows.",
            "Monitoring — read the activity log to catch mistakes early and confirm your agents are doing the right thing.",
            "Improving and scaling — refine instructions, add guardrails and roll trusted agents out to more of your work or team.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Getting started with Gemini Spark and automating your daily work with tasks",
    2: "Reusable skills and schedules, then advanced real-world agentic workflows",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. Each day totals exactly 480 training minutes
# (excluding the 1-hour lunch; tea breaks are within training time).
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ground rules and setting up your Google Workspace account for the labs"),
        ("9:50","10:40",50,"topic","TOPIC 01 — Getting Started with AI Agents and Gemini Spark: what autonomous agents are; how Spark works with background agents, approvals and control; connecting Spark to Gmail, Calendar and Drive; effective prompting and instructing (concepts + live demo)"),
        ("10:40","11:15",35,"lab","Hands-on: "+lab_titles([1])),
        ("11:15","11:30",15,"break","Tea break"),
        ("11:30","13:00",90,"lab","Hands-on: "+lab_titles([2,3])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:00",60,"topic","TOPIC 02 — Automating Work with Gemini Spark Tasks: one-off tasks for research and organisation; automating email, inbox summaries and drafting; working with Docs, Sheets and Slides through the agent; reviewing, approving and refining agent actions (concepts + live demo)"),
        ("15:00","15:45",45,"lab","Hands-on: "+lab_titles([4])),
        ("15:45","16:00",15,"break","Tea break"),
        ("16:00","18:15",135,"lab","Hands-on: "+lab_titles([5,6])),
        ("18:15","18:30",15,"recap","Day 1 recap and Q&A"),
     ]),
     2: (DAY_THEMES[2], [
        ("9:30","9:45",15,"recap","Day 1 recap and warm-up"),
        ("9:45","10:45",60,"topic","TOPIC 03 — Building Reusable Skills and Schedules: creating custom, reusable skills such as a Ghostwriter; designing schedules and conditional triggers; chaining multi-step automated workflows; personalising agent behaviour and style (concepts + live demo)"),
        ("10:45","11:30",45,"lab","Hands-on: "+lab_titles([7])),
        ("11:30","11:45",15,"break","Tea break"),
        ("11:45","13:00",75,"lab","Hands-on: "+lab_titles([8,9])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:00",60,"topic","TOPIC 04 — Advanced Agentic Workflows and Real-World Automation: automating lead management, expenses and planning; coordinating multi-app workflows across Workspace; guardrails for permissions, privacy and safe automation; monitoring, improving and scaling your agents (concepts + live demo)"),
        ("15:00","15:45",45,"lab","Hands-on: "+lab_titles([10])),
        ("15:45","16:00",15,"break","Tea break"),
        ("16:00","18:00",120,"lab","Hands-on: "+lab_titles([11,12])),
        ("18:00","18:30",30,"recap","Course wrap-up, your automation roadmap and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What an AI Agent Really Is",
    concepts=[
        "From chatbot to agent — a chatbot replies; an agent takes actions across your apps to reach a goal.",
        "You stay in charge — the agent proposes and prepares; you approve before anything leaves your account.",
        "It works where you work — Spark acts inside Gmail, Calendar, Drive, Docs, Sheets and Slides.",
        "Everything is logged — an activity trail lets you inspect, trust and undo what the agent did.",
    ],
    framework_title="The Spark Automation Loop",
    framework=[
        ("Instruct", "State the goal, the inputs, the output and the limits in plain language."),
        ("Run", "Spark plans the steps and works through them as a background agent."),
        ("Review", "You inspect what it produced against the result you expected."),
        ("Approve", "Nothing is sent, shared or changed until you give the go-ahead."),
        ("Refine", "Adjust the instruction and save the good ones as reusable skills."),
    ],
    statement=dict(
        headline="An agent is only as good as the instruction and the guardrails you give it.",
        body="This course is hands-on: you will instruct, run, review and refine real agents on your own Workspace, then save the ones that work as reusable skills and schedules.",
        kicker="THE DESIGN RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A connected agent", ["Spark linked to Gmail, Calendar and Drive", "A tested first task", "A clear instruction template"]),
        ("A task toolkit", ["Research and organisation tasks", "Inbox summary and reply drafting", "Docs, Sheets and Slides generation"]),
        ("Reusable automation", ["A named Ghostwriter skill", "A scheduled daily digest", "A conditional trigger and a chained workflow"]),
        ("Real-world workflows", ["Lead, expense and planning automations", "Multi-app coordination", "Guardrails, monitoring and a scaling plan"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the agent technique on a shared example.",
        "You build it yourself in Gemini Spark on your own Workspace (or the supplied sample data).",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review the agent's actions in the activity log and refine the instruction.",
        "You keep the working skill or schedule — it becomes part of your automation toolkit.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the AI Agents with Gemini Spark (C1259) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 12 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected 'AI operations assistant' for a small studio called "
    "Brightwave. You start it in Lab 1 and add one automation to it in every lab. Wherever you can, "
    "use your own Google Workspace so you leave the course with agents that already work for you; a "
    "supplied Brightwave sample scenario is provided for anyone who prefers not to use their own data."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a current Chrome or Edge browser.",
        "A Google account with Google Workspace access to Gmail, Calendar, Drive, Docs, Sheets and Slides.",
        "Gemini Spark available and enabled on your Google account (the trainer will confirm access at the start of Day 1).",
        "Optional: a few of your own real (non-confidential) emails, files or notes to automate — or use the supplied Brightwave sample data.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to Google, open Gemini, and see your Gmail, Calendar and Drive. If Spark is not yet visible on your account, tell the trainer.",
    verify_code="Open gemini.google.com  ·  sign in  ·  confirm Gmail, Calendar and Drive are accessible",
    conventions=[
        "Placeholders such as <YOUR NAME> or <SENDER EMAIL> are replaced with your own values.",
        "Chat/instruction text you give the agent is shown in a shaded box — type or paste it into Spark.",
        "Every lab ends with a 'Test it' step — an explicit check that the agent did the right thing before you move on.",
        "Approve nothing you have not read. If a result is wrong, refine the instruction and run it again.",
    ],
)
LAB_NOTE = (
    "Use only accounts and data you are authorised to use. Never paste real passwords, API keys or "
    "confidential personal data into an agent instruction; use the supplied sample data if in doubt."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have built a connected set of AI agents across two days — from your first supervised task to scheduled, chained, guard-railed workflows that handle real work.",
    sections=[
        dict(title="What you built", bullets=[
            "Gemini Spark connected to Gmail, Calendar and Drive, with a tested first task.",
            "A toolkit of one-off tasks for research, inbox summaries, reply drafting and Docs/Sheets/Slides.",
            "A reusable Ghostwriter skill, a scheduled daily digest, a conditional trigger and a chained workflow.",
            "Real-world automations for leads, expenses and planning, coordinated across several Workspace apps.",
            "A set of guardrails, a monitoring habit and a plan to scale trusted agents to more of your work.",
        ]),
        dict(title="What to do next", bullets=[
            "Point your best skills at a real, recurring task in your own week and measure the time saved.",
            "Review your agents' activity logs weekly and tighten any instruction that produced a wrong result.",
            "Share a proven skill with a colleague, with the guardrails documented.",
            "Add one new automation a week until your routine admin runs itself.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild your Ghostwriter skill, daily digest and a chained workflow from memory.",
    "Apply the techniques to a real recurring task in your own organisation, starting with guardrails.",
    "Review each lab's detailed steps in this guide and re-run the automations on your own Workspace.",
]
LG_GLOSSARY = [
    ("AI agent", "Software that plans and carries out multi-step tasks toward a goal you set, not just a single reply."),
    ("Gemini Spark", "Google's agentic capability that acts across Workspace apps to complete tasks on your behalf."),
    ("Background agent", "An agent that works through a task while you do other things, reporting back when done."),
    ("Approval", "The step where Spark pauses and waits for you to authorise an action before it takes effect."),
    ("Activity log", "The record of every action an agent has taken, used to review, trust and undo its work."),
    ("Instruction", "A plain-language brief that states the goal, inputs, output and limits for an agent task."),
    ("Task", "A single instruction Spark runs, once, to produce a result you can review."),
    ("Skill", "A saved, named instruction you can reuse and run again without re-typing it."),
    ("Ghostwriter", "A worked example skill that drafts content in a consistent, personalised style."),
    ("Schedule", "A setting that runs an agent automatically on a cadence, such as every weekday morning."),
    ("Conditional trigger", "A rule that runs a skill only when a stated condition occurs, such as a new email from a sender."),
    ("Chaining", "Connecting skills so the output of one becomes the input of the next in a multi-step workflow."),
    ("Guardrail", "An explicit limit on what an agent may do, set so that automation is safe by design."),
    ("Least privilege", "Granting an agent only the access it needs for the task and no more."),
    ("Workspace", "Google's suite of Gmail, Calendar, Drive, Docs, Sheets and Slides that Spark acts within."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C1259 AI Agents with Gemini Spark courseware.", TRAINER),
]
