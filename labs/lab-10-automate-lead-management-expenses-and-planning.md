# Lab 10 — Automate Lead Management, Expenses and Planning

**Topic 04:** Advanced Agentic Workflows and Real-World Automation  |  **Day 2**  |  **Approx. 45 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Build agent workflows that capture leads, log expenses and turn notes into a plan — end to end.

## What you'll build

Three real-world automations: lead intake, expense logging and a planning agenda — each tested once.

**Tools and techniques:** Lead management, Sheets logging, follow-up drafting, expense extraction, planning, Calendar

## Prerequisites

- Labs 1-9 complete, especially your saved skills.
- A sample enquiry email, some expense notes, and rough notes for a piece of work (or the Brightwave sample).

## Steps

### Step 1

Build the lead-intake flow. From an enquiry email, log the lead to a Sheet and draft a follow-up for approval.

Instruction to give the agent (paste into Gemini Spark):

```text
From new emails labelled 'Lead', add a row to 'Leads' Sheet (Name, Company, Ask, Date) and draft a follow-up reply. Save drafts; do not send.
```

### Step 2

Test it with one sample enquiry. Confirm the row appears with the right fields and a sensible follow-up draft is created.

### Step 3

Build the expense flow. Turn a set of expense notes (or receipt details you type) into a clean, categorised record.

Instruction to give the agent (paste into Gemini Spark):

```text
Turn these expense notes into an 'Expenses' Sheet with Date, Vendor, Category, Amount, and a running total: <paste your notes or the sample>.
```

### Step 4

Review the expense Sheet: are categories sensible and the total correct? Refine the categories in the instruction and re-run if needed.

### Step 5

Build the planning flow. Turn rough notes about a piece of work into a sequenced plan with dates.

Instruction to give the agent (paste into Gemini Spark):

```text
Turn these notes into a step-by-step plan with suggested dates this month, then draft calendar events for each step. Do not create events yet.
```

### Step 6

Review the proposed plan and events. Approve creating events only for the steps you agree with, then check Calendar.

### Step 7

Look across the three flows and note where they share data (a lead could become a planned piece of work) — a hint for Lab 11.

### Step 8

Save all three as skills so they are ready to run again and to combine next.

## Test it

You have a lead logged to a Sheet with an approved follow-up draft, an accurate categorised expense record with a correct total, and a plan whose approved steps appear as Calendar events.

## Troubleshooting

- **Leads aren't logging to the Sheet.** Name the exact Sheet and columns, and the label/condition that identifies a lead. Test with one clearly-labelled sample email.
- **Expense categories are inconsistent.** Give the agent a fixed category list to choose from, and ask it to flag anything that doesn't fit rather than guessing.
- **Calendar events were created before you approved them.** Add 'draft the events; do not create yet.' Approve the steps you want, then confirm in Calendar.

## Challenge

Add a weekly roll-up that counts new leads and total expenses for the week into a one-line summary Doc.

## Reflection

LO7 — Of lead, expense and planning automation, which would save your team the most time first, and why?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
