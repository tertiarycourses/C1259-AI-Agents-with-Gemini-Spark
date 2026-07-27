# C1259 — AI Agents with Gemini Spark

Put your productivity on autopilot. This two-day, hands-on course teaches you to build and run
your own autonomous AI agents with **Google Gemini Spark**, automating multi-step tasks across
Google Workspace — Gmail, Calendar, Drive, Docs, Sheets and Slides.

## Course Information

- **Course Code:** C1259
- **Course Title:** AI Agents with Gemini Spark
- **Duration:** 2 days / 15 hours
- **Level:** Beginner
- **Mode:** Instructor-led, hands-on practical labs
- **Course Registration:** [AI Agents with Gemini Spark](https://www.tertiarycourses.com.sg/ai-agents-with-gemini-spark.html)

## One Connected Project

Every lab adds one automation to a single, growing **AI operations assistant** for a fictional
creative agency, Brightwave Studio. You connect Spark in Lab 1 and finish in Lab 12 with a
monitored, guard-railed assistant and a plan to scale it. Wherever possible you use your **own**
Google Workspace, so you leave the course with agents that already work for you; a Brightwave
sample scenario is supplied for anyone who prefers not to use real data.

There is **no assessment** — this is a commercial short course. Each lab proves itself with an
explicit *Test it* verification step instead.

## What You'll Learn

| Topic | Coverage |
|---|---|
| **01 — Getting Started with AI Agents and Gemini Spark** | What autonomous agents are; background agents, approvals and control; connecting Spark to Gmail, Calendar and Drive; effective prompting and instructing |
| **02 — Automating Work with Gemini Spark Tasks** | One-off tasks for research and organisation; inbox summaries and email drafting; Docs, Sheets and Slides through the agent; reviewing, approving and refining |
| **03 — Building Reusable Skills and Schedules** | Custom reusable skills (a Ghostwriter); schedules and conditional triggers; chaining multi-step workflows; personalising agent behaviour and style |
| **04 — Advanced Agentic Workflows and Real-World Automation** | Lead, expense and planning automation; multi-app coordination; guardrails for permissions, privacy and safe automation; monitoring, improving and scaling |

## Learning Outcomes

1. Explain what autonomous AI agents are and how Gemini Spark's background agents, approvals and controls work.
2. Connect Gemini Spark to Google Workspace and write clear, effective instructions that an agent can act on.
3. Create one-off agent tasks to research, organise, summarise email and draft content across Docs, Sheets and Slides.
4. Review, approve and refine agent actions so automated work stays accurate and under your control.
5. Build custom reusable skills and design schedules and conditional triggers that run automatically.
6. Chain multi-step workflows across several Workspace apps and personalise your agent's behaviour and style.
7. Automate real-world workflows — lead management, expenses and planning — with sound permission and privacy guardrails.
8. Monitor, improve and scale your AI agents responsibly.

## Repository Layout

```
courseware/   Trainer slides (PPTX + PDF), Learner Guide (DOCX + PDF), Lesson Plan (DOCX + PDF)
labs/         12 hands-on labs (lab-NN-*.md), a labs README and tools.md
LG-*.md       Markdown mirror of the Learner Guide
.claude/      Course build engine, commands, hooks and QA agents
```

## Prerequisites

- Able to operate basic computer functions.
- A Google account with Google Workspace access; Gemini Spark enabled (confirmed on Day 1).
- Bring your own Windows or Mac laptop with a current Chrome or Edge browser.

## Building the Courseware

All artifacts are generated from a single source (`course_data.py` + `data_domainN.py`) so the
slides, Lesson Plan, Learner Guide and labs stay 100% aligned:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

---

*© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). Course code C1259.*
