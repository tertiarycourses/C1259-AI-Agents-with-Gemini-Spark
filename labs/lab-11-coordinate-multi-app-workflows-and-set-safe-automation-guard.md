# Lab 11 — Coordinate Multi-App Workflows and Set Safe-Automation Guardrails

**Topic 04:** Advanced Agentic Workflows and Real-World Automation  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** AI Agents with Gemini Spark (C1259)

> **Connected project:** this lab adds one more automation to the **Brightwave AI operations assistant** you began in Lab 1. If you fell behind, use the supplied Brightwave sample data to rejoin at this lab.

## Goal

Run one workflow that spans several Workspace apps, and set permission, privacy and safety guardrails.

## What you'll build

One multi-app workflow plus a written guardrails checklist applied to your agents.

**Tools and techniques:** Multi-app coordination, Gmail, Sheets, Calendar, Drive, least privilege, privacy, guardrails

## Prerequisites

- Lab 10 complete: lead, expense and planning skills saved.
- Your guardrails from earlier labs (approvals ON, draft-only defaults).

## Steps

### Step 1

Design a workflow that deliberately spans apps. Reuse skills from Lab 10 so this is coordination, not new work.

Instruction to give the agent (paste into Gemini Spark):

```text
When a 'Lead' email arrives: 1) log it to the Leads Sheet, 2) draft a follow-up, 3) add a 'Review lead' event tomorrow, 4) file the email to Drive/Leads.
```

### Step 2

Run it once on a sample lead and check each app in turn: Sheet row, Gmail draft, Calendar event, Drive file. Fix the step that failed.

### Step 3

Review permissions with least privilege in mind: does any agent have access it does not need? Remove access that is not required.

### Step 4

Set a privacy guardrail: instruct your agents never to include confidential data in outputs and to use placeholders for anything sensitive.

Instruction to give the agent (paste into Gemini Spark):

```text
Never put client financials, personal ID numbers or passwords into any draft, Sheet or Doc. Use <REDACTED> instead and flag it to me.
```

### Step 5

Set an action guardrail: nothing is sent, shared externally or deleted without explicit approval, even on scheduled runs.

### Step 6

Test a guardrail on purpose: ask the agent to do something the guardrail forbids and confirm it refuses or asks first.

### Step 7

Write a short guardrails checklist (permissions, privacy, actions, approvals) and apply it to every skill you keep.

### Step 8

Confirm in the activity log that the multi-app run is recorded as one connected workflow you can review end to end.

## Test it

Your multi-app workflow completes across Gmail, Sheets, Calendar and Drive from a single trigger, your agent refuses a forbidden action when tested, and you have a written guardrails checklist applied to your kept skills.

## Troubleshooting

- **One app in the multi-app run failed while others worked.** Run that one step alone to isolate it, fix its instruction, then re-run the whole workflow. The activity log shows which step stopped.
- **The agent didn't refuse a forbidden action in your test.** Make the guardrail explicit and specific in the instruction, then re-test. Vague guardrails ('be careful') don't hold.
- **You're unsure what access each agent has.** Review the connections/permissions panel and remove anything not needed for the task — least privilege by default.

## Challenge

Add a privacy test: feed the workflow a record containing a fake ID number and confirm the agent redacts it and flags it to you.

## Reflection

LO7 — Which single guardrail, if it failed, would cause the most harm in your workflows, and how will you verify it stays in place?

## Deliverable

Save your output — it becomes part of your **AI operations assistant**, the connected toolkit you consolidate, monitor and plan to scale in Lab 12.

---

*AI Agents with Gemini Spark (C1259) · C1259 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
