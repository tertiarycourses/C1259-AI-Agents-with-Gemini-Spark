# Lab 12 — Monitor, Improve and Scale Your AI Agents

**Topic 04:** Advanced Agentic Workflows and Real-World Automation  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Consolidate your assistant, monitor it from the activity log, improve weak instructions and plan to scale safely.

## What you'll build

A monitored, improved AI operations assistant and a one-page plan to scale it responsibly.

**Tools and techniques:** Monitoring, activity log review, instruction improvement, reliability, scaling, governance

## Prerequisites

- All prior labs complete — you have tasks, skills, schedules and workflows to review.
- Access to your agents' activity logs.

## Steps

### Step 1

Inventory your assistant: list every task, skill, schedule and workflow you built across the 12 labs.

### Step 2

Monitor from the activity log: review recent runs and mark any that produced a wrong, incomplete or off-tone result.

### Step 3

For each weak result, find the root cause in the instruction — usually a missing Input, Output or Limit — and fix it.

Instruction to give the agent (paste into Gemini Spark):

```text
Improve one skill: add the missing part (e.g. 'Output: a Doc named X' or 'Limit: never send') and re-run to confirm it is fixed.
```

### Step 4

Add a reliability check to your most-used skill: a line that makes the agent state what it did so you can verify at a glance.

### Step 5

Decide what is safe to run unattended and what must always pause for approval, and set each accordingly.

### Step 6

Write your scaling plan: which two automations to expand next, who else could use them, and the guardrails that must travel with them.

### Step 7

Pick one skill to hand over: document its name, purpose, inputs, output and guardrails so a colleague could run it safely.

### Step 8

Write your 30-day automation roadmap: one new automation a week, each with a 'Test it' check, starting with the highest time saver.

## Test it

You have a written inventory of everything you built, at least one instruction improved after monitoring its log, a documented hand-over for one skill, and a one-page 30-day plan to scale your agents with guardrails.

## Troubleshooting

- **An automation quietly produced a wrong result.** Trace it in the activity log to the exact instruction, find the missing Input/Output/Limit, fix it, and re-run to confirm.
- **A skill is too risky to hand over as-is.** Document its inputs, output and guardrails, and set it to require approval before you share it with a colleague.
- **You have too many automations to keep track of.** Keep the inventory list from Step 1 as your control panel; retire anything you haven't used or trusted.

## Challenge

Write a one-paragraph 'agent charter' for your team: what agents may do unattended, what needs approval, and who owns the review.

## Reflection

LO8 — What is the first automation you will put into real use next week, and how will you know it is working?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
